from app import db


class Task(db.Model):
    id_task = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(64))
    task_dif = db.Column(db.String(120))

    def __repr__(self):
        return '<Task {}>'.format(self.task_name)


