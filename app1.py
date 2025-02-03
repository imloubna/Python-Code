from flask import Flask, request

app = Flask(__name__)

@app.route('/loubs')
def home():
    return "Welcome to Flask!"

@app.route('/data', methods=['POST'])
def data():
    return {
        "name":"Alice",
        "age":24,
        "loubs" : request.json
    }

@app.route('/hello/<id>', methods=['POST'])
def hello(id):
    return {
        "status":True,
        "data":request.json
    }

if __name__ == '__main__':
    app.run(debug=True) 
