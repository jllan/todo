from app import app
from app.models import Todo
from flask_script import Manager

manage = Manager(app)

@manage.command
def save():
    todo = Todo(content='testtest')
    todo.save()
    print('插入成功')

if __name__ == '__main__':
    manage.run()