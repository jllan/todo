from flask import Blueprint, render_template, url_for, request, flash, redirect, session, jsonify, current_app
from flask_login import current_user, login_required
import time
from ..db import db
from .models import Duty

duty = Blueprint('duty', __name__, url_prefix='')

@duty.route('/', methods=['GET'])
def index():
    todo_list = Duty.query.filter().all()
    return render_template('index.html', duty_list=todo_list)
    # return render_template('duty.html', duty_list=todo_list)

@duty.route('/duty/my', methods=['GET'])
@login_required
def duty_my():
    # if not current_user.is_authenticated:
    #     flash('请先登陆')
        # raise Exception('请先登陆')
        # return redirect(url_for('user.user_signin'))
        # return jsonify(status='error', info='请先登陆')
    todo_list = Duty.query.filter(Duty.author_id == current_user.id).all()
    return render_template('duty.html', duty_list=todo_list)

@duty.route('/duty/add',methods=['GET','POST'])
@login_required
def duty_add():
    try:
        if request.method == 'POST':
            # if not current_user.is_authenticated:
            #     flash('请先登陆')
            #     raise Exception('请先登陆')
                # return jsonify(status='error', info='请先登陆')
            duty_instance = Duty.query.filter(Duty.title == request.form['title']).first()
            if duty_instance:
                flash('该问题已存在')
                raise Exception('该问题已存在')
                # return jsonify(status='error', info='该问题已存在')
            else:
                print('no')
                duty_instance = Duty()
                duty_instance.author_id = current_user.id
                print(current_user.name)
                duty_instance.title = request.form['title']
                # duty_instance.content = request.form['content']
                duty_instance.status = request.form['status']
                duty_instance.is_show = request.form['is_show']
                db.session.add(duty_instance)
                db.session.commit()
                flash('问题创建成功')
                return redirect(url_for('duty.index'))
                # return jsonify(status='success', info='问题创建成功')
        else:
            # duty_list = Duty.query.filter().all()
            return render_template('duty_add.html')
    except Exception as e:
        current_app.logger.error(e)
        return render_template('duty_add.html')

@duty.route('/duty/modify/<int:id>')
@login_required
def duty_modify(id):
    duty = Duty.query.filter(Duty.id == id).first()
    if duty:
        duty.status = 0 if duty.status else 1
        db.session.add(duty)
        db.session.commit()
    else:
        flash('该条数据不存在')
    return redirect(url_for('duty.duty_my'))

@duty.route('/duty/delete/<int:id>')
@login_required
def duty_delete(id):
    duty = Duty.query.filter(Duty.id==id).first()
    if duty:
        db.session.delete(duty)
        db.session.commit()
    else:
        flash('该条数据不存在')
    return redirect(url_for('duty.duty_my'))