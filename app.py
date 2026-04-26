from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Each task will be a dictionary now
tasks = []

@app.route('/')
def index():
    html = "<h1>To-Do List</h1>"

    for i, task in enumerate(tasks):
        status = "✅" if task['done'] else "❌"
        
        html += f"""
        {status} {task['text']} 
        <a href='/complete/{i}'>Toggle Complete</a> 
        <a href='/delete/{i}'>Delete</a><br>
        """

    html += """
        <form method='POST' action='/add'>
            <input type='text' name='task' required>
            <input type='submit' value='Add'>
        </form>
    """

    return html


@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    
    # Store task as dictionary
    tasks.append({
        'text': task_text,
        'done': False
    })
    
    return redirect(url_for('index'))


@app.route('/complete/<int:index>')
def complete(index):
    # Toggle complete status
    tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



