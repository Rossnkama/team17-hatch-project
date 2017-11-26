from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from flask import render_template

import cgi

app = Flask(__name__)


form = cgi.FieldStorage()


stuff = []

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()

    for thing in stuff:
	    resp.say(thing)

    return str(resp)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	stuff.append('Something')
	print request.GET['username']
	print request.POST['username']
	return render_template('./index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)