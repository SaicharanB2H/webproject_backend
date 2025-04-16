from flask import Flask, render_template,request, redirect, url_for, session, flash

app = Flask(__name__)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # You can validate login here
        return f"Welcome, {email}!"
    return render_template('login.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
