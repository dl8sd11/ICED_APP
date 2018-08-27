from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


with open("data.json","r") as f:
    message_object = json.load(f)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('get_data')
def handle_my_custom_event(data, methods=['GET', 'POST']):
    emit('data_update',json.dumps(message_object))
    # socketio.emit('my response', json, callback=messageReceived)

@socketio.on('new_message')
def new_message(data,methods=['GET','POST']):
    message_object["message"].append(data)
    socketio.emit('data_update',json.dumps(message_object))
    with open("data.json","w") as f:
        json.dump(message_object,f)

if __name__ == '__main__':
    socketio.run(app)