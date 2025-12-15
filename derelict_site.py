from flask import Flask, render_template, send_file
from post_model import Post
import json

app = Flask(__name__)

def load_posts(json):
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
                load_posts(post['replies'])
            )
        )
        post_count += 1
    return posts

post_list = load_posts(json.load(open('posts.json')))
speculation_post_list = load_posts(json.load(open('speculation_posts.json')))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/speculation')
def speculation():
    return render_template('speculation.html', posts=speculation_post_list)

@app.route('/threads')
def threads():
    return render_template('threads.html', posts=post_list)

@app.route('/thread/<int:post_id>')
def thread(post_id):
    return render_template('thread.html', post=post_list[post_id])

@app.route('/spec_thread/<int:post_id>')
def spec_thread(post_id):
    return render_template('thread.html', post=speculation_post_list[post_id])

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/origin')
def origin():
    return render_template('origin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/download')
def download():
    return send_file('derelict_game.zip', as_attachment=True)


if __name__ == '__main__':
    app.run()