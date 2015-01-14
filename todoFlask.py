import os
from flask import Flask, render_template
from flask import url_for, redirect
from flask import request,json
from datetime import datetime
# return redirect(url_for('static', filename='todo.html'))
app = Flask(__name__)

hashmap = {}

@app.route('/', methods=['GET','POST', 'DELETE'])
def index():
	if request.method == 'GET':
		return render_template('todoAJAX.html')
	
	elif request.method == 'POST':
		content = request.form['userInput']; # [] !!! not ()
   	timeAsID = str(datetime.now());
   	hashmap[timeAsID] = content;
   	return json.dumps({'Status':'OK', 'content': content, 'ID': timeAsID});
  
if __name__ == '__main__':
    app.debug = True;
    app.run();