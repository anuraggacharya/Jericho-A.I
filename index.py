# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, url_for, request, jsonify
from logic import text_to_speech, controlLed
#from pyfirmata import Arduino, util
from time import sleep



# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.



@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html')


@app.route('/sayHello', methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        name = request.json['name']
        text_to_speech("Hello, Gayatri!","Female")
    return jsonify({"name": "gayatri"})

@app.route('/controlLed', methods=['GET', 'POST'])
def LED():
    if request.method == "POST":
        command = request.json['command']
        controlLed(command)
    return jsonify({"status": "Command executed"})


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, port=80, host='0.0.0.0')
