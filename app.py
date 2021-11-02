from flask import Flask, render_template, redirect, request
from wtforms import meta

import os
import pandas as pd
import numpy as np

# import machine learning modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import sklearn.externals
import joblib


# instantiate flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

if __name__=='__main__':
    app.run(debug=True)