from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify
from models import dbModel
from functools import wraps
from config import SECRET_KEY


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

db = dbModel()

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('access_token')
        if not token:
            return redirect(url_for('login_page'))
        user = db.verify_token(token)
        if not user:
            resp = make_response(redirect(url_for('login_page')))
            resp.delete_cookie('access_token')
            return resp
        request.user = user
        return fn(*args, **kwargs)
    return wrapper

@app.route('/')
def index():
    products = db.get_all_product()
    return render_template("index.html", products = products)

@app.route('/signup', methods=["GET", "POST"])
def signup_page():
    msg = ""
    if request.method == 'POST':
        msg = db.create_user(request.form)
    return render_template("signup.html", msg=msg)

@app.route('/login',  methods=["GET", "POST"])
def login_page():
    msg=""
    success = False
    result = ""
    if request.method == "POST":
        success, result = db.authenticate_user(request.form)
    
    if success:
        resp = make_response(redirect(url_for("index")))
        resp.set_cookie("access_token", result, httponly=True, samesite="Lax")
        return resp
    else:
        msg = result
    return render_template("login.html", msg=msg)

@app.route('/cart',  methods=["GET", "POST"])
@jwt_required
def cart_page():
    user_id = request.user['id']

    if request.method == "POST":
        product_id = request.form.get("product_id")
        db.add_to_cart(user_id, product_id)
        return redirect(url_for("cart_page"))
    
    products = db.get_cart_items(user_id)
    return render_template("cart.html", products=products)

@app.route('/cart/delete',  methods=["POST"])
@jwt_required
def cart_delete():
    user_id = request.user['id']
    product_id = request.form.get("product_id")
    db.delete_from_cart(user_id, product_id)
    return redirect(url_for("cart_page"))

@app.route('/order', methods=['GET', 'POST'])
@jwt_required
def order_page():
    if request.method == 'GET':
        return render_template('order.html')
    user_id = request.user['id']
    db.clear_cart(user_id)
    return render_template('success.html', message="Order placed successfully!")