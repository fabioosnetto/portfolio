from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__) # app
app.config['SECRET'] = 'pumpkingenericeveryoddallowssoundbigdemonsays' # for cookies and sensitive data
app.config['DEBUG']  = True # debug mode
io = SocketIO(app, cors_allowed_origins='*') # io instance

# app init
@app.route('/')
def msgApp():
   return render_template('msg-app.html')

# when message received, broadcast
@io.on('message')
def onMessage(msg):
   print(f'Message: {msg}')
   send(msg, broadcast=True)

# says where io will broadcast
if __name__ == '__main__':
   io.run(app, host='192.168.15.107')


"""
set FLASK_APP="mainfilename.py"
set FLASK_DEBUG=1
python -m flask run --host=0.0.0.0
"""