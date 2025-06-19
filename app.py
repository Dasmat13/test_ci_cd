import nummpy as np
import pandas as pd
from flask import Flask, request,jsonify
from sklearn.linear_model import LinearRegression
import joblib
import os
print(os.getcwd())  # Prints the current working directory

import logginga