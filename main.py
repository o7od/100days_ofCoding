from flask import Flask, render_template
import requests
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)
all_blogs = requests.get(BLOG_URL).json()
print(all_blogs)


@app.route('/')
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    print(blog_id)
    return render_template("post.html", posts=all_blogs, id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
