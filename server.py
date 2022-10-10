from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<name>')
def greeting(name):
    return f"Hello {name}"

@app.route('/salutations/<name>/<int:num>')
def salutations(name, num):
    return f"Salutations {name}! I could say it {num} more times or do {name * num}"



if __name__=="__main__":
    app.run(debug=True)