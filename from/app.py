from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    show_alert = False

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            message = "Both fields are required!"
            show_alert = True
        elif username == "iqra" and password == "123459":
            message = f"Welcome, {username}!"
            show_alert = True
        else:
            message = "Invalid username or password!"
            show_alert = True

    return render_template('login.html', message=message, show_alert=show_alert)

if __name__ == '__main__':
    app.run(debug=True)