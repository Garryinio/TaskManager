from app import app, db
from flask import render_template, flash, redirect
from app.forms import TaskForm
from app.models import Task

listaTaskuri = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()

    # if form.task.data == "":
    #     return "trebuie completat!"
    if form.validate_on_submit():
        flash('Added task:{}'.format(
            form.task.data))
        tasks = Task(task_name=form.task.data, task_dif = form.task_assignment.data)
        db.session.add(tasks)
        db.session.commit()
        return redirect("/")

    else:
        tasks = Task.query.order_by(Task.task_dif).all()

    return render_template('index.html', title='Home', form=form, tasks=tasks)


@app.route('/delete/<int:id_task>')
def delete(id_task):
    task_to_delete = Task.query.get_or_404(id_task)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "A intervenit o eroare la stergerea task-ului"


@app.route('/update/<int:id_task>', methods=['GET', 'POST'])
def update(id_task):
    task_to_update = Task.query.get_or_404(id_task)
    form = TaskForm()
    form.submit.label.text = "Update"

    if form.validate_on_submit():
        task_to_update.task_name = form.task.data
        task_to_update.task_dif = form.task_assignment.data
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "A aparut o problema la modificarea task-ului :("
    else:
        return render_template('update.html', task=task_to_update, form = form)
