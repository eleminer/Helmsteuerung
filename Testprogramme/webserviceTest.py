from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():

    return "hello from the Raspberry Pi!"

app.run(host='0.0.0.0', port= 8090)