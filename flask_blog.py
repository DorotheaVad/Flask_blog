from flask import Flask,render_template,url_for


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

if __name__=="__main__":
    app.run(debug=True)

