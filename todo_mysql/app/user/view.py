from flask import Blueprint, request, current_app, redirect, url_for, jsonify, flash, render_template
from .models import User
from sqlalchemy import or_
from ..db import db
from flask_login import login_user, logout_user, login_required

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/signup', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'POST':
        try:
            user_instance = User.query.filter(or_(User.name==request.form['name'],
                                                  User.email==request.form['email'])
                                              ).first()
            if user_instance:
                flash('该用户名或邮箱已存在')
                raise Exception('该用户名或邮箱已存在')
                # return jsonify(status='error', info='该用户名或邮箱已存在')
            else:
                user_instance = User()
                user_instance.name = request.form['name']
                user_instance.email = request.form['email']
                user_instance.set_password(request.form['password'])
                db.session.add(user_instance)
                db.session.commit()
                flash('创建成功')
                # return jsonify(status='success', info='创建成功')
                return redirect(url_for('duty.index'))
        except Exception as e:
            current_app.logger.error(e)
            return render_template('signup.html')
            # return redirect(url_for('duty.index'))
    else:
        return render_template('signup.html')


@user.route('/signin', methods=['GET', 'POST'])
def user_signin():
    if request.method == 'POST':
        try:
            user_instance = User.query.filter(User.name==request.form['name']).first()
            if user_instance:
                if user_instance.verify_password(request.form['password']):
                    login_user(user_instance)
                    flash('登陆成功')
                    return redirect(url_for('duty.index'))
                else:
                    flash('密码错误')
                    raise Exception('密码错误')
            else:
                flash('用户名不存在')
                raise Exception('用户名不存在')
            # return redirect(url_for('duty.index'))
        except Exception as e:
            current_app.logger.error(e)
            return render_template('signin.html')
    else:
        return render_template('signin.html')

@user.route('/logout', methods=['GET'])
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('duty.index'))