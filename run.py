from flask import Flask, render_template, request
from twilio.twiml.voice_response import VoiceResponse
app = Flask(__name__)

@app.route('/')
def buyer():
    return render_template('buyer.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      global result
      result = request.form
      return render_template("result.html",result = result)

@app.route('/twilio', methods = ['POST', 'GET'])
def twilio():
    resp = VoiceResponse()
    resp.say("Hello there. A request has been submitted for " + result['Quantity'] + " kilograms of " + result['Product']+ ". Please contact " + result['Phone'] + " to arrange a deal.")
    return str(resp)

if __name__ == '__main__':
   app.run(debug = True)