from flask import render_template,url_for,flash,redirect,request
from flask_blog.forms import RegistrationForm,LoginForm
from flask_blog import app,db,bcrypt
from flask_blog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required

posts=[{ "author":"Joe" ,"title" :"Blog post 1","content":"This is my first blog post","date_posted":"12/3/2020"},{"author":"minnies","title":"Mouse","content":"I swear i am the real minnie mouse !","date_posted":"15/6/2020"}]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",post=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)                                                                           
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created. Now you are able to login",category="success")
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash("You loged in succesfully! We are redirecting you to your homepage...",category="success")
            next_page=request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccesful. Please check password and email !",category="danger")
    return render_template("login.html",title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
    
@app.route("/my_account")
@login_required
def account():
    return render_template("account.html",title="My Account")