from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

posts=[{ "author":"Joe" ,"title" :"Blog post 1","content":"This is my first blog post","date_posted":"12/3/2020"},{"author":"minnies","title":"Mouse","content":"I swear i am the real minnie mouse !","date_posted":"15/6/2020"}]

app = Flask(__name__)

app.config["SECRET_KEY"]= "05f9d68146e9379ac7ce72f92b0ecc2c"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",post=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!",category="success")
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@blog.com" and form.password.data=="password":
            flash(f'Succesful login !',category="success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccesful. Please check password and email !",category="danger")
    return render_template("login.html",title="Login",form=form)

if __name__=="__main__":
    app.run(debug=True)

