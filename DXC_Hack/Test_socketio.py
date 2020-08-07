import os
from flask import Flask,redirect,url_for,render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] =os.environ.get('SECRET')
socketio= SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template("index_socket_test.html")

@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)
    send(msg , broadcast =True)

if __name__ == '__main__':
    app.run()