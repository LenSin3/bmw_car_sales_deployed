import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms import validators
from wtforms.fields.core import DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError
import helpers
from helpers import MaxYear

# import data
df = pd.read_csv('data/bmw_clean.csv')
df_cols = df.columns.tolist()
#list to hold unique values
model = helpers.get_unique_vals(df, 'model')
transmission = helpers.get_unique_vals(df, 'transmission')
fueltype = helpers.get_unique_vals(df, 'fuelType')

# instantiate MaxYear
max_yr = MaxYear()
# create a FlaskForm class:CarSalesVars
class CarSalesVars(FlaskForm):
    model = SelectField('Model', choices=model, validators=[DataRequired()])
    transmission = SelectField('Transmission', choices=transmission, validators=[DataRequired()])
    fueltype = SelectField('Fuel Type', choices=fueltype, validators=[DataRequired()])
    mileage = DecimalField('Mileage', validators=[DataRequired()])
    tax = DecimalField('Tax', validators=[DataRequired()])
    mpg = DecimalField('MPG', validators=[DataRequired()])
    engine_size = DecimalField('Engine Size', validators=[DataRequired()], rounding=None)
    year = DecimalField('Year', validators=[DataRequired()])
    

    submit = SubmitField('Get Price')
    # def validate_year(form, year):
    #     if year.data > 2020:
    #         raise ValidationError("Year must be less than or equal to 2020!")

    
