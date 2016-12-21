from .duty_app import app
from .db import db
from .user import User
from .user import user
from .duty import Duty
from .duty import duty
from .extensions import login_manager


def configure_login(app):
    login_manager.login_view = 'user.user_signin'
    login_manager.refresh_view = 'user.user_signin'
    login_manager.login_message = '请先登陆'
    login_manager.session_protection = 'basic'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    login_manager.setup_app(app)

app.register_blueprint(duty)
app.register_blueprint(user)
configure_login(app)