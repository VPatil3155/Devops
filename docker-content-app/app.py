from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

# Load posts
def load_posts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Save posts
def save_posts(posts):
    with open(DATA_FILE, 'w') as f:
        json.dump(posts, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = load_posts()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_post = {
            "id": len(posts) + 1,
            "title": title,
            "content": content,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        posts.append(new_post)
        save_posts(posts)
        return redirect('/')

    return render_template('index.html', posts=posts)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()
    posts = [p for p in posts if p["id"] != post_id]
    save_posts(posts)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)