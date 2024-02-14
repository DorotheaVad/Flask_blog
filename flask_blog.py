from flask import Flask,render_template

posts=[{ "author":"Joe" ,"title" :"Blog post 1","content":"This is my first blog post"},{"author":"minnies","title":"Mouse","content":"I swear i am the real minnie mouse !"}]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",post=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)

