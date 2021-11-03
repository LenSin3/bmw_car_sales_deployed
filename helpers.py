from pandas.core.frame import DataFrame
import pandas as pd
from wtforms.validators import ValidationError, InputRequired, DataRequired
from flask_wtf import FlaskForm
import utils

def get_unique_vals(df, col):

    if isinstance(df, pd.DataFrame):
        df_cols = df.columns.tolist()
        if col in df_cols:
            if df[col].dtype == 'object' or df[col].dtype == bool:
                uniques = df[col].unique().tolist()
            else:
                raise utils.InvalidDataType(col)
        else:
            raise utils.InvalidColumn(col)
    else:
        raise utils.InvalidDataFrame(df)
    return uniques

def max_year_check(form, field):
    if field.data > 2020:
        raise ValidationError("Year must be less than or equal to 2020!")

class MaxYear(object):
    def __init__(self, max_yr = 2020, message=None):
        self.max_yr = max_yr
        if not message:
            message = "Year must be less than or equal to 2020! Predictor will use a 2020 for values greater than 2020."
        self.message = message
    
    def __call__(self, form, field):
        yr = field.data
        if yr > self.max_yr:
            raise ValidationError(self.message)
        