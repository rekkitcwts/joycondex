from flask import Flask, render_template

app = Flask(__name__)

'''
No parameters. This returns the list of controller platforms supported, e.g. switch-joycons, switch-procon, ps4, ps5, xbox, etc
'''
@app.route('/api/getshells/')
def get_shells_platform():
	return 'Show platforms here'

'''
Homepage.
Self explanatory.
'''
@app.route('/')
def hello():
	return render_template('main.html', title="Datastruct's Reshell Dex")