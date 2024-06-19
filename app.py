from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    send({'msg': data['msg'], 'username': data['username']}, room=data['room'])

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send({'msg': f"{username} has entered the room."}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send({'msg': f"{username} has left the room."}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
