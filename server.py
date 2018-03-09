from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/') #This is the root
def index():
	if not 'counter' in session:
		session['counter'] = 0
	else:
		session['counter'] += 1
	return render_template('index.html', number = session['counter'])

app.run(debug=True)