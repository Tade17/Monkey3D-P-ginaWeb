from flask import Flask,render_template,request



app=Flask(__name__)





@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def login_admin():
    return render_template("/admin/dashboard.html")
if __name__ == '__main__':
    app.run(debug=True)
