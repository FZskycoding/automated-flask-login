from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from config import Config
import os

# 載入環境變數
load_dotenv()

app = Flask(__name__)

# 載入基本配置
app.config.from_object(Config)

# 從環境變數載入敏感配置
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

# 註冊
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        
        # 檢查是否已存在相同 email
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            flash("此 Email 已被註冊", "danger")
        else:
            cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            mysql.connection.commit()
            cur.close()
            flash("註冊成功，請登入", "success")
            return redirect(url_for("login"))
        
        cur.close()

    return render_template("register.html")

# 登入
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            flash("Email 或密碼錯誤", "danger")

    return render_template("login.html")

# 登入成功畫面
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("請先登入", "warning")
        return redirect(url_for("login"))
    
    return render_template("dashboard.html", user=session["user"])

# 登出
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
