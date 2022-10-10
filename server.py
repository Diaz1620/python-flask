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

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":
    app.run(debug=True)