from flask_wtf import FlaskForm, validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    task = StringField('Task:', validators=[DataRequired()])
    submit = SubmitField('Adauga task')
    task_choices = ("De baza", "Important", "Poate astepta", "Neimportant")

    task_assignment = SelectField("Importanta task-ului", choices=task_choices)


