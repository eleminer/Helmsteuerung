from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/SB')
def SB():
    AppData = request.args.get('Data')
    print(AppData)
    return "ok!"

app.run(host='0.0.0.0', port= 8090)