from flask import Flask, render_template,request, redirect, url_for, session, flash
import sqlite3 
from werkzeug.security import generate_password_hash ,check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/valentineday')
def valentine():
    return render_template('valentineday.html')

@app.route('/diamonds')
def Diamonds():
    return render_template('diamonds.html')

@app.route('/loginpage')
def account():
    return render_template('login.html')

@app.route('/newuser')
def userReg():
    return render_template('user_registration.html')

@app.route('/tobuy')
def buy():
    return render_template('buyingpage.html')

@app.route('/orderplaced')
def orderplaced():
    return render_template('confirmpage.html')


# Route to show the registration form
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Hash the password before storing
        hashed_password = generate_password_hash(request.form["password"])

        data = {
            "first_name": request.form["firstName"],
            "last_name": request.form["lastName"],
            "email": request.form["email"],
            "password": hashed_password,  # store hashed password
            "phone": request.form["phone"],
            "address": request.form["address"],
            "city": request.form["city"],
            "state": request.form["state"],
            "zip": request.form["zip"],
            "newsletter": 1 if request.form.get("newsletter") == "on" else 0,
            "terms": 1 if request.form.get("terms") == "on" else 0
        }

        try:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute('''
                INSERT INTO users (
                    first_name, last_name, email, password, phone,
                    address, city, state, zip, newsletter, terms
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', tuple(data.values()))
            conn.commit()
            conn.close()
            flash("Account successfully created!", "success")
            return redirect(url_for("register"))
        except sqlite3.IntegrityError:
            flash("Email already exists. Try a different one.", "danger")
        except Exception as e:
            flash(f"Error: {e}", "danger")

    return render_template("user_registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        conn.close()

        if user:
            stored_password = user[4]  
            if check_password_hash(stored_password, password):
                session["user_id"] = user[0]
                session["email"] = user[3]
                flash("Login successful!", "success")
                return redirect(url_for("home"))  
            else:
                flash("Incorrect password.", "danger")
        else:
            flash("Email not found.", "danger")

    return render_template("login.html") 



if __name__ == '__main__':
    app.run(debug=True)
