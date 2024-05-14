from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder=r"C:\Users\MALA\Desktop\to-do")

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if index < len(todos):
        todo = todos[index]
        if request.method == 'POST':
            new_todo = request.form.get('todo')
            if new_todo:
                todo['task'] = new_todo
            return redirect(url_for('index'))
        else:
            return render_template('edit.html', todo=todo, index=index)
    else:
        return redirect(url_for('index'))

@app.route('/check/<int:index>')
def check(index):
    if index < len(todos):
        todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(todos):
        del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
