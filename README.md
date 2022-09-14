# TaskManager
A really simple Task Manager build using Python and Flask.

NOTE: The project it's made in Romanian Language, so it might not make any sense for english speakers.


Background is a css animation using @keyframes.

Tasks are added by a name and the importance of it. For exemple, it's build using The Eisenhower Matrix.
------------------------------------------------------------------------------------------------------------
There are 4 types of tasks, as:

de baza = urgent and important

important = not urgent but important

poate astepta = 'could wait'

neimportant = not important

------------------------------------------------------------------------------------------------------------
tasks can be deleted or updated.

tasks are ordered by the importance( most important on the top )

tasks are saved using sqlAlchemy ( ORM ) and it contains one table with 3 columns(id_task,task_name and task_dif)

To run:
1. First, pip install requirements.txt into a new or existing virtual environment.
2. Open terminal at the project folder and type "flask run"
3. Done! You can use the app.

pics:
![image](https://user-images.githubusercontent.com/73346539/190203093-f43441cd-a06c-4752-9e18-7949baafe50b.png)
![image](https://user-images.githubusercontent.com/73346539/190203121-a1e66acb-80de-4471-9206-7c113922480b.png)
![image](https://user-images.githubusercontent.com/73346539/190203214-40147204-7ade-468c-8753-caa82cd3b794.png)
![image](https://user-images.githubusercontent.com/73346539/190203246-39b92b13-be62-41bf-9adc-c813b337621c.png)
