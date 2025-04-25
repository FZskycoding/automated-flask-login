from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "users.db"

# 初始化 SQLite 資料庫
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

# 註冊
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash("此 Email 已被註冊", "danger")
            else:
                cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
                conn.commit()
                flash("註冊成功，請登入", "success")
                return redirect(url_for("login"))

    return render_template("register.html")

# 登入
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
            user = cursor.fetchone()

            if user:
                session["user"] = email
          
                return redirect(url_for("dashboard"))
            else:
                flash("Email 或密碼錯誤", "danger")

    return render_template("login.html")

#登入成功畫面
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("請先登入", "warning")
        return redirect(url_for("login"))
    
    return render_template("dashboard.html", user=session["user"])

#登出
@app.route("/logout")
def logout():
    session.pop("user", None)
   
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
