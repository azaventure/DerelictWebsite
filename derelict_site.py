from flask import Flask, render_template
from post_model import Post
import json

app = Flask(__name__)

def load_posts(type, json):
    posts = []
    post_count = 0
    for post in json:
        print("Loading reply from " + post['author'])
        posts.append(
            Post(
                post_count, 
                post['title'], 
                post['author'], 
                post['messagetype'], 
                post['time'],
                post['content'], 
                load_posts("reply", post['replies'])
            )
        )
        post_count += 1
    return posts

post_list = load_posts("post", json.load(open('posts.json')))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/threads')
def threads():
    return render_template('threads.html', posts=post_list)

@app.route('/thread/<int:post_id>')
def thread(post_id):
    return render_template('thread.html', post=post_list[post_id])

@app.route('/users')
def users():
    return render_template('users.html')


if __name__ == '__main__':
    app.run()