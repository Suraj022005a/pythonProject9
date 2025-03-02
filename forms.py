from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Milk', 'Milk'),
        ('Cheese', 'Cheese'),
        ('Yogurt', 'Yogurt'),
        ('Butter', 'Butter'),
        ('Cream', 'Cream')
    ], validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])

    submit = SubmitField('Submit')
