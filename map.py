from numerology import create_app, db
from numerology.models import User, Post
#from numerology.models import User, Post, Notification, Message,Task

app = create_app()



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}