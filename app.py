from flask import Flask, render_template, request, jsonify, Response
from flask.ext.scss import Scss
from flask.ext.socketio import SocketIO, emit

#cleanup needed here
from time import sleep
from threading import Thread, Event
from random import random

from backend import fetch
from subprocess import PIPE, Popen
from threading  import Thread
import sys
from Queue import Queue, Empty
ON_POSIX = 'posix' in sys.builtin_module_names

app = Flask(__name__, static_folder='static', template_folder='assets/views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def get_root():
    return render_template('index.jade')

@app.route('/query')
def get_gif():
    request.args.get('url')
    return Response(status=200)

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
                if (counter == 20):
                        socketio.emit('done', {'data': 'Connected'},namespace='/test')
                        counter = 0
                        break
                number = round(random()*10, 3)
                print number
                print counter
                counter = counter +1
                socketio.emit('my response', {
                        'data': number,
                        'message': 'Commit message!',
                        'hash': number,
                        'url': 'http://andyzg.github.io',
                    }, namespace='/test')
                sleep(self.delay)
    def run(self):
        self.randomNumberGenerator()

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    fetch_gif('https://github.com/markprokoudine/mchacks')
    global thread
    global counter
    print ('Client connected')
   # makegif()
    if not thread.isAlive() and counter < 50:
        counter = counter +1
        print "Starting Thread"
        thread = RandomThread()
        thread.start()
        print("rE")
    if counter > 8:
        print("finito")
        emit('done', {'data': 'finito'})

@socketio.on('commit')
def handle_message(commit):
    print('received message: ' + commit)

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

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def fetch_gif(repo):

    # spawn child thread and serve 
    p = Popen(['python', 'backend/fetch.py', repo] , stdout=PIPE, stderr=PIPE, bufsize=1, close_fds=ON_POSIX)
    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()

    # parse output
    while True:
        # read line without blocking
        try:  line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            continue
        else: # got line
            parsed = line.split(' ')
            if parsed[0] == "commit":
                commit_id = parsed[1]
                pic_path = parsed[2]
                repo = parsed[3]
                comment = ' '.join(parsed[3:])






if __name__ == '__main__':
    socketio.run(app,'0.0.0.0')
