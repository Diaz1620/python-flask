from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<name>/<int:num>')
def greeting(name, num):
    return render_template("hello.html", nombre= name, numero= num)

@app.route('/salutations/<name>/<int:num>')
def salutations(name, num):
    return f"Salutations {name}! I could say it {num} more times or do {name * num}"



if __name__=="__main__":
    app.run(debug=True)