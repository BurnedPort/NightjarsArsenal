from flask import Flask, request, render_template_string

app = Flask(__name__)

# Basic dummy login form (embedded HTML)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "hunter2":
            return "Login successful!"
        return "Invalid"

    return render_template_string("""
        <h2>Test Login Form</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username"/><br>
            <input type="password" name="password" placeholder="Password"/><br>
            <input type="submit" value="Login"/>
        </form>
    """)

if __name__ == "__main__":
    app.run(debug=False)
