from flask import Flask, flash, render_template, redirect, request
from wtforms import meta

import os
import pandas as pd
import numpy as np
from form import CarSalesVars, df_cols


# import machine learning modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import sklearn.externals
import joblib

# extract pickled car price predictor model
bmw_price_predictor = joblib.load('models/best_regressor_dump.pkl')

# instantiate flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/", methods=["GET", "POST"])
def index():
    # instantiate form
    form = CarSalesVars(meta = {'csrf': False})
    # get field names
    field_names = ['model', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize', 'num_year']
    pred_results = []
    if form.validate_on_submit():
        # get form data
        form_data = [form.model.data, form.transmission.data, form.mileage.data, form.fueltype.data, form.tax.data, form.mpg.data, form.engine_size.data, form.year.data]
        # get number of years
        num_year = 2020 - form_data[7]
        # update years with number of years
        form_data[7] = num_year
        # construct dataframe to predict
        pred_df = pd.DataFrame([form_data], columns = field_names)
        # predict price
        pred_result = bmw_price_predictor.predict(pred_df)
        pred_results.append(round(pred_result[0], 2))

    return render_template('index.html', form=form, pred_results=pred_results)

if __name__=='__main__':
    app.run(debug=True)