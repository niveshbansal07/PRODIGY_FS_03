from flask import Flask, jsonify
from config import dbconfig, JWT_SECRET, JWT_EXP_HOURS
import mysql.connector
import bcrypt
from datetime import datetime, timedelta
import jwt

class dbModel:
    def __init__(self):
        self.dbconfig = dbconfig
        self.jwt_secret = JWT_SECRET
        self.jwt_hours = JWT_EXP_HOURS
        try:
            self.con = mysql.connector.connect(
                host=dbconfig['host'],
                user=dbconfig['user'],
                password=dbconfig['password'],
                database=dbconfig['database'],
                auth_plugin='mysql_native_password'
            )
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True, buffered=True)
            print("Connection Successful :)")
        
        except Exception as e:
            print("Some Error in Connection of DB :(")
            print(e)

    def get_all_product(self):
        self.cur.execute("SELECT id, name, description, price, image, stock FROM products_table ORDER BY id DESC")
        return self.cur.fetchall()
    
    def hashed_password(self, plain):
         return bcrypt.hashpw(plain.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain, hashed):
        return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))
    
    def generate_token(self, user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(hours=self.jwt_hours),
            "iat": datetime.utcnow()
        }
        token = jwt.encode(payload, self.jwt_secret, algorithm="HS256")
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        return token
    
    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=["HS256"])
            user_id = payload.get('user_id')
            self.cur.execute("SELECT id, name, email FROM user_table WHERE id=%s", (user_id,))
            user = self.cur.fetchone()
            return user
        except Exception:
            return None
    
    def create_user(self, data):
        email = data['email']
        self.cur.execute("SELECT id FROM user_table WHERE email=%s", (email,))
        if self.cur.fetchone():
            return "Email already exists"
        
        hashed = self.hashed_password(data['password'])
        self.cur.execute(f"INSERT INTO user_table(name, email, password) VALUES('{data['name']}', '{data['email']}','{hashed}')")
        return "Created"
    
    def authenticate_user(self, data):
        email = data['email']
        self.cur.execute("SELECT id, name, email, password FROM user_table WHERE email=%s", (email,))
        user = self.cur.fetchone()
        if not user:
            return False, "Email not exist"
        if not self.check_password(data['password'], user['password']):
            return False, "Wrong Password"
        user_id = user['id']
        token = self.generate_token(user_id)
        return True, token

    def get_product(self, product_id):
        self.cur.execute("SELECT id, name, description, price, image, stock FROM products_table WHERE id=%s", (product_id,))
        return self.cur.fetchone()
    
    def add_to_cart(self, user_id, product_id):
        self.cur.execute(
        "SELECT id FROM cart_table WHERE user_id=%s AND product_id=%s",
        (user_id, product_id))

        if self.cur.fetchone():
            self.cur.execute(
            "UPDATE cart_table SET quantity = quantity + 1 WHERE user_id=%s AND product_id=%s",
            (user_id, product_id))
        else:
            self.cur.execute(
            "INSERT INTO cart_table(user_id, product_id, quantity) VALUES(%s, %s, 1)",
            (user_id, product_id))
            
    def get_cart_items(self, user_id):
        self.cur.execute("""
        SELECT 
            c.product_id,
            c.quantity,
            p.name,
            p.price
        FROM cart_table c
        JOIN products_table p ON c.product_id = p.id
        WHERE c.user_id = %s
    """, (user_id,))
        return self.cur.fetchall()

    def delete_from_cart(self, user_id, product_id):
        self.cur.execute("DELETE FROM cart_table WHERE user_id=%s AND product_id=%s", (user_id, product_id))
        return True
    
    def clear_cart(self, user_id):
        self.cur.execute("DELETE FROM cart_table WHERE user_id=%s", (user_id,))
        return True