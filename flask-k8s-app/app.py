from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template('index.html', hostname=hostname)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    event = request.form['event']
    
    return f"""
    <h2>Registration Successful</h2>
    Name: {name}<br>
    Email: {email}<br>
    Event: {event}<br>
    Served from: {socket.gethostname()}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)