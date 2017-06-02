from flask import session, redirect, url_for, render_template, request
from .. import chat_blueprint
from .forms import LoginForm


@chat_blueprint.route('/chat_login', methods=['GET', 'POST'])
def chat_login():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('chat_login.html', form=form)


@chat_blueprint.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.chat_login'))
    return render_template('chat.html', name=name, room=room)
