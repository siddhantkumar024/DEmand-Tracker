from demand_tracker import db
from datetime import datetime

# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()

# The user_loader decorator allows flask-login to load the current user
# and grab their id.



class User(db.Model):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    Demand_Id = db.Column(db.Integer(64), unique=True, index=True)
    L5_Manager = db.Column(db.String(64), unique=True, index=True)   # manager may not be unique
    Skill_required = db.Column(db.String(128), unique=True, index=True)
    Experience = db.Column(db.String(64), unique=True, index=True)
    Profile_shared = db.Column(db.String(64), unique=True, index=True)
    Comments = db.Column(db.String(128), unique=True, index=True)
    Demand_status = db.Column(db.String(64), unique=True, index=True)

    

    def __init__(self, Demand_Id,L5_Manager,Skill_required,Experience,Profile_shared,Comments,Demand_status):
        self.Demand_Id = Demand_Id
        self.L5_Manager = L5_Manager
        self.Skill_required = Skill_required
        self.Experience= Experience
        self.Profile_shared = Profile_shared
        self.Comments = Comments
        self.Demand_status = Demand_status

   
    def __repr__(self):
        return f"Demandid: {self.Demand_Id}, L5_manager:{self.L5_Manager}, Skillrequired: {self.Skill_required}, Experience:{self.Experience}, Profileshared:{self.Profile_shared}, comments:{self.Comments}, demandstatus:{self.Demand_status}"

