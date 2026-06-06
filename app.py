from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__)
app.secret_key='secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
    print("Database created successfully!")

@app.route("/register", methods=["GET", "POST"])#register
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists!")
            return redirect("/register")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!")
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])#login
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect("/")
        else:
            flash("Invalid username or password")
            return redirect("/login")
    return render_template("login.html")

@app.route("/logout")#logout
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect("/login")

@app.route("/")#home
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])#add
@login_required
def add_task():
    task_content = request.form["task"]
    if task_content:
        new_task=Task(content=task_content, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()

    return redirect("/")

@app.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
         db.session.delete(task)
         db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)