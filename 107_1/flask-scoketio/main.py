from flask import Flask, render_template
from flask_socketio import SocketIO
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@socketio.on('my event')
def handle_my_custom_event(JJ):
  print('received json: '+str(JJ))
@app.route('/')
def get_index():
  return render_template('index.html')
if __name__ == '__main__':
    socketio.run(app,port=3000)