from flask import Flask,render_template,request,session,redirect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os 
from werkzeug.utils import secure_filename
from flask_sqlalchemy import pagination


with open("templates/config.json","r") as c:        #configurable parameters from json file to change without touching the code

    params=json.load(c)["params"]


local_server=True #---

app=Flask(__name__)




app.secret_key=params['secret_key']                     #key for managing the login session

#for sending form data on mail
app.config.update(

    MAIL_SERVER= "smtp.gmail.com",
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME =params['mail_username'],
    MAIL_PASSWORD=params['mail_password'],
)

mail=Mail(app)


if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri'] #---

else:
     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri'] #---


db=SQLAlchemy(app)

class Contacts(db.Model) :  #for contact database

#sno,name,phone_num,msg,date,email  names of columns in database nerdycoder

    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    phone_num=db.Column(db.String(12),nullable=False)
    msg=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(120),nullable=True)
    email=db.Column(db.String(120),nullable=False)



class Posts(db.Model) :  #for post database

#sno,name,phone_num,msg,date,email  names of columns in database nerdycoder

    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),nullable=False)
    slug=db.Column(db.String(21),nullable=False)
    content=db.Column(db.String(120),nullable=False)
    tagline=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(120),nullable=True)
    img_file=db.Column(db.String(25),nullable=False)
    
    


@app.route("/")
def home():
    page = request.args.get('page', default=1, type=int)
    per_page = 5  # Number of posts to display per page
    posts = Posts.query.order_by(Posts.date.desc()).paginate(page, per_page, False)

    return render_template('index.html', params=params, posts=posts)

    # posts = Posts.query.order_by(Posts.date.desc()).all()
    # # posts = Posts.query.order_by(Posts.date.desc()).limit(params['no_of_posts']).all()
    # # posts=Posts.query.filter_by().all()[0:params['no_of_posts']]
    
    # return render_template('index.html',params=params,posts=posts)

@app.route("/about")
def about():

    return render_template('about.html',params=params)

@app.route("/contact",methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        #adding these all to database

        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry=Contacts(name=name,phone_num=phone,msg=message,email=email,date=datetime.now())

        db.session.add(entry)
        db.session.commit()

        #sending mail to the dev after commiting in db 
        mail.send_message(f'New Message From Blog By {name}',
                          sender=params['mail_username'],
                          recipients=[params['mail_recipient']],
                          body="Message : "+message+"\n\ncontact : "+phone+'\n\nemail:'+email




                        )
        

    return render_template('contact.html',params=params)





@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):

    post=Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html',params=params,post=post)



@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user']==params['admin_user']):
        posts=Posts.query.all()
        return render_template('dashboard.html',params=params,posts=posts)

    elif request.method=='POST':
        username = request.form.get('username')
        password= request.form.get('password')

        if username==params['admin_user'] and password==params['admin_pass']:
            #set the session variable
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params,posts=posts)


    return render_template('login.html',params=params,)



@app.route("/edit/<string:sno>", methods = ['GET','POST'])
def edit(sno):

    if ('user' in session and session['user']==params['admin_user']):
        
        if request.method == 'POST':
                
            
            box_title= request.form.get('title')
            slug= request.form.get('slug')

            if not slug:
            # Use the secure_filename function to create a URL-safe slug
                slug = secure_filename(box_title)

            tagline= request.form.get('tagline')
            content= request.form.get('content')
            img_file= request.form.get('img_file')
            date=datetime.now() 
                     
            if sno=='0':
                post = Posts(title=box_title,slug=slug,tagline=tagline,content=content,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=slug
                post.tagline=tagline
                post.content=content
                post.img_file=img_file
                post.date=date
                db.session.commit()
                return redirect('/edit/'+sno)
            
    post=Posts.query.filter_by(sno=sno).first()
                    
    return render_template('edit.html',params=params,post=post,sno=sno)


@app.route("/delete/<string:sno>")
def delelte(sno):
    if ('user' in session and session['user']==params['admin_user']):
         post = Posts.query.filter_by(sno=sno).first()
         db.session.delete(post)
         db.session.commit()
    return redirect('/dashboard')



@app.route("/uploader", methods = ['POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_user']):
        if request.method=='POST':
            f=request.files['file1']
            f.save(os.path.join(params['upload_folder'],secure_filename(f.filename)))

            return "file uploaded successfully"

    

                
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')





if __name__=="__main__":
    app.run(debug=True)
