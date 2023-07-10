from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    Id=IntegerField('Id')
    Slno=StringField('SlNo',validators=[DataRequired()])
    Demand_Id = IntegerField('Demand_Id', validators=[DataRequired()])
    L5_Manager = StringField('L5_Manager',validators=[DataRequired()])
    Skill_required = StringField('Skill_required',validators=[DataRequired()])
    Experience = StringField('Experience',validators=[DataRequired()])
    Profile_shared = StringField('Profile Shared',validators=[DataRequired()])
    Comments = StringField('Comments',validators=[DataRequired()])
    Demand_status = SelectField('Demand Status',choices=[('Done','Done'),('Pending','Pending'), ('Not Applicable','Not Applicable')])
    submit = SubmitField('Add')


