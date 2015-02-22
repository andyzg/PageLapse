from flask import Flask, render_template, request, jsonify, Response
from flask.ext.scss import Scss
from flask.ext.socketio import SocketIO, emit

#cleanup needed here
from time import sleep
from threading import Thread, Event
from random import random


app = Flask(__name__, static_folder='static', template_folder='assets/views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def get_root():
    return render_template('index.jade')

@app.route('/query')
def get_gif():
    url = request.args.get('url')
    history = [1, 2, 3, 4, 5];
    return jsonify(url=url, commitHistory=history)
    # return Response(status=300)



#======Fan's socket routes======
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()
counter = 0

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print "Making random numbers"
        while not thread_stop_event.isSet():
                global counter
                #if counter == 8:
                #       emit('done', {'data': 'finito'})
                #       break
                if (counter == 8):
                        socketio.emit('done', {'data': 'Connected'},namespace='/test')
                        counter = 0
                        break
                number = round(random()*10, 3)
                print number
                print counter
                counter = counter +1
                socketio.emit('my response', {'data': number}, namespace='/test')
                sleep(self.delay)
    def run(self):
    	self.randomNumberGenerator()

@app.route('/page_lapse')
def index():
	return render_template('mainapp.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
        global thread
        global counter
        print ('Client connected')
       # makegif()
        if not thread.isAlive() and counter < 8:
                counter = counter +1
                print "Starting Thread"
                thread = RandomThread()
                thread.start()
                print("rE")
        if counter > 8:
        	print("finito")
                emit('done', {'data': 'finito'})
    # emit('my response', {'data': 'Connected'},)
    # makegif()
    # print "connect"
    # time.sleep(2)
    # emit('my response', {'data': 'Connected'})
    # print "first pic"
    # time.sleep(1)
    # emit('my response', {'data': 'Connected'})
    # print "second pic"
    # time.sleep(2)
    # print "third pic"
    # time.sleep(4)
    # emit('done', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app,'0.0.0.0')
