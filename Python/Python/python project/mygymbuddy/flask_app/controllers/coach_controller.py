from flask_app import app
from flask import redirect, render_template, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.requests import Request
from flask_app.models.coachs import Coach
from flask_app.models.clients import Client
from flask_app.models.sessions import Session

@app.route('/coachdashboard')
def coach():
    if not 'user_id' in session:
        return redirect('/')
    
    coach_id= session['user_id']
    print("****************",coach_id)
    coach_instance=Coach.get_coach_by__user_id({'id':coach_id})
    print("======================",coach_instance.id)
    coach=Request.get_coach_all_requests({'id':coach_instance.id})
    return render_template('dashboard.html',coach=coach)

@app.route('/accept/<int:id>')
def accept_request(id):
    Request.update_status({'status':"accepted","id":id})
    return redirect ('/coachdashboard')

@app.route('/decline/<int:id>')
def decline_request(id):
    Request.update_status({'status':"declined","id":id})
    return redirect ('/coachdashboard')


@app.route('/coach/<int:id>')
def one_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    this_coach=Coach.get_coach_by_id({"id":id})
    return render_template('one_coach.html',this_coach=this_coach)



@app.route("/requests")
def requestes():
    if not 'user_id' in session:
        return redirect('/')
    coach_id= session['user_id']
    print("****************",coach_id)
    coach_instance=Coach.get_coach_by__user_id({'id':coach_id})
    print("======================",coach_instance.id)
    coach=Request.get_coach_all_requests({'id':coach_instance.id})
    return render_template ("request.html",coach=coach)


@app.route("/add/session")
def new_session():
    if not 'user_id' in session:
        return redirect('/')
    coach_id= session['user_id']
    coach=Coach.get_coach_by__user_id({'id':coach_id})
    return render_template("new_session.html", coach=coach)

@app.route("/session/new", methods=['post'])
def create_session():
    print(request.form)
    Session.create_session(request.form)
    return redirect('/coachdashboard')




@app.route("/members")
def members():
    if not 'user_id' in session:
        return redirect('/')
    all_clients=Client.show_all_clients({'id':session['user_id']})
    return render_template("members.html",all_clients=all_clients)






