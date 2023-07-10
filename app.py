from flask import render_template,url_for,flash, redirect,request
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm


app = Flask(__name__)

#############################################################################
############ CONFIGURATIONS (CAN BE SEPARATE CONFIG.PY FILE) ###############
###########################################################################

# Remember you need to set your environment variables at the command line
# when you deploy this to a real website.
# export SECRET_KEY=mysecret
# set SECRET_KEY=mysecret
app.config['SECRET_KEY'] = 'mysecret'

#################################
### DATABASE SETUPS ############
###############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
db.app=app

#----------------------------------------------------------------#


class User(db.Model):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    Slno=db.Column(db.String(1280))
    Demand_Id = db.Column(db.Integer)
    L5_Manager = db.Column(db.String(64))   # manager may not be unique
    Skill_required = db.Column(db.String(128))
    Experience = db.Column(db.String(64))
    Profile_shared = db.Column(db.String(64))
    Comments = db.Column(db.String(128))
    Demand_status = db.Column(db.String(64))

    

    def __init__(self, Slno,Demand_Id,L5_Manager,Skill_required,Experience,Profile_shared,Comments,Demand_status):
        self.Slno=Slno
        self.Demand_Id = Demand_Id
        self.L5_Manager = L5_Manager
        self.Skill_required = Skill_required
        self.Experience= Experience
        self.Profile_shared = Profile_shared
        self.Comments = Comments
        self.Demand_status = Demand_status

   
    def __repr__(self):
        return f"Demandid: {self.Demand_Id}, L5_manager:{self.L5_Manager}, Skillrequired: {self.Skill_required}, Experience:{self.Experience}, Profileshared:{self.Profile_shared}, comments:{self.Comments}, demandstatus:{self.Demand_status}"



#-----------------------------------------------------------------#


@app.route('/',methods=['GET','POST'])
def index():
    form = AddForm()
    posts = User.query.all()

    
    return render_template('index.html',posts=posts,form=form)


@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    
    

    if form.validate_on_submit():

        add_post = User(Slno=form.Slno.data, Demand_Id=form.Demand_Id.data, L5_Manager =form.L5_Manager.data, Skill_required=form.Skill_required.data,Experience=form.Experience.data,
                            Profile_shared =form.Profile_shared.data,Comments=form.Comments.data,Demand_status=form.Demand_status.data
        )
        db.session.add(add_post)
        db.session.commit()
        flash("Post is added or Created")
        return redirect(url_for('index'))

    return render_template('add_post.html',form=form)

     
    

@app.route("/<int:id>/update", methods=['GET', 'POST'])
def update(id):
    
    
    posts = User.query.get_or_404(id)

    form = AddForm()
    if form.validate_on_submit():
        posts.Slno=form.Slno.data
        posts.Demand_Id = form.Demand_Id.data
        posts.L5_Manager = form.L5_Manager.data
        posts.Skill_required = form.Skill_required.data
        posts.Experience = form.Experience.data
        posts.Profile_shared = form.Profile_shared.data
        posts.Comments = form.Comments.data
        posts.Demand_status = form.Demand_status.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('index'))
    # Pass back the old blog post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.Slno.data=posts.Slno
        form.Demand_Id.data = posts.Demand_Id 
        form.L5_Manager.data = posts.L5_Manager 
        form.Skill_required.data = posts.Skill_required
        form.Experience.data = posts.Experience 
        form.Profile_shared.data = posts.Profile_shared
        form.Comments.data = posts.Comments 
        form.Demand_status.data = posts.Demand_status
        
    return render_template('add_post.html',form=form)


@app.route("/<int:del_id>/delete", methods=['POST'])
def delete(del_id):
    posts = User.query.get_or_404(del_id)
    db.session.delete(posts)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)


