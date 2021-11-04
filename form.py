import pandas as pd
from flask import flash
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms import validators
from wtforms.fields.core import DecimalField, FloatField
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
    mileage = DecimalField('Mileage', validators=[DataRequired(), NumberRange(min=0, message="Mileage must be positive number!")])
    tax = DecimalField('Tax', validators=[DataRequired(message="Please enter a numeric value for Tax!"), NumberRange(min=0, message="Tax must be positive number!")])
    mpg = DecimalField('MPG', validators=[DataRequired(), NumberRange(min=0, message="MPG must be numeric!")])
    engine_size = DecimalField('Engine Size', validators=[DataRequired(), NumberRange(min=0, message="Engine Size must be numeric!")])
    year = DecimalField('Year', validators=[DataRequired(), NumberRange(max=2020, message="Year must not be greater than 2020!")])
    

    submit = SubmitField('Get Price')

    # def validate_tax(self, tax):
        # int_tax = int(self.tax)
        # if not self.tax.data:
        #     raise ValidationError("Tax must be numeric!")
        # if self.tax.data < 0:
            # raise ValidationError("Tax must be a positive number!")

    # def validate_tax(self,tax):
    #     if type(self.tax.data) != int or type(self.engine_size.data) != float:
    #         raise ValidationError("Tax must be numeric!")

    # def validate_mpg(self, mpg):
    #     if type(self.mpg.data) != int or type(self.engine_size.data) != float:
    #         raise ValidationError("MPG must be numeric!")

    # def validate_engine_size(self, engine_size):
    #     if type(self.engine_size.data) != int or type(self.engine_size.data) != float:
    #         raise ValidationError("Engine Size must be numeric!")

    # def validate_year(self, year):
    #     if self.year.data > 2020:
    #         raise ValidationError("Year must be less than or equal to 2020!")

    
