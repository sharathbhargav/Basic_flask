from crypt import methods
from flask import Flask,render_template, request,redirect
import os
from flask_sqlalchemy import SQLAlchemy
from models import Users, publications
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

if __name__ == '__main__':
    app.run()


@app.route('/student/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student = Users(email=email,f_name=first_name,l_name=last_name)
        db.session.add(student)
        db.session.commit()
        return redirect('/')


@app.route('/publication/read', methods=['GET'])
def read_all():
    p1 = db.engine.execute("select * from publications p join users u on p.student_id=u.id ")
    pubs = [row for row in p1]
    res=[]
    for each in pubs:
        e=[each[2],each[3],each[6],each[7]]
        res.append(e)

    return render_template('display_pub.html',res=res)




@app.route('/publication/create' , methods = ['GET','POST'])
def create_pub():
    if request.method == 'GET':
        q = Users.query.all()
        users=[u for u in q]
        res=[]
        for each in users:
            res.append([each.id,each.first_name])
        print(res)
        return render_template('createpage_pub.html',users=res)
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        title = request.form['title']
        year = request.form['year']
        pub=publications(student_id,title,year)
        db.session.add(pub)
        db.session.commit()
        return redirect('/')





@app.route('/publication/update' , methods = ['GET','POST'])
def update_pub():
    if request.method == 'GET':
        q = publications.query.all()
        pubs=[u for u in q]
        res=[]
        for each in pubs:
            res.append([each.id,each.title])
        return render_template('update_pub.html',pubs=res)
 
    if request.method == 'POST':
        pub_id = request.form['pub_id']
        student_id = request.form['student_id']
        title = request.form['title']
        year = request.form['year']
        q = db.session.query(publications)
        q = q.filter(publications.id==pub_id)
        pub = q.one()
        print(pub)
        pub.student_id=student_id
        pub.title=title
        pub.year=year
        db.session.commit()
        return redirect('/')



@app.route('/publication/delete' , methods = ['GET','POST'])
def delete_pub():
    if request.method == 'GET':
        q = publications.query.all()
        pubs=[u for u in q]
        res=[]
        for each in pubs:
            res.append([each.id,each.title])
        print(res)
        return render_template('delete_pub.html',pubs=res)
 
    if request.method == 'POST':
        pub_id = request.form['pub_id']
        q = db.session.query(publications)
        q = q.filter(publications.id==pub_id)
        pub = q.one()
        db.session.delete(pub)
        db.session.commit()
        return redirect('/')

@app.route("/")
def hello():
    
    return render_template('index.html')
    