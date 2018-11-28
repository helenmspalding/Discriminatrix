import pandas as pd
import numpy as np
from flask import Flask
app = Flask(__name__)


dataset = pd.read_csv('Gender_pay_gap.csv')
# print dataset

#setting preview of top ten csv lines for ease
dataset = pd.read_csv('Gender_pay_gap.csv')
dataset = dataset.head(10)

# function to return company name
employernames = dataset["EmployerName"]
employernames = employernames.str.replace(" ", "_", regex=True)

dataset.index = employernames
print dataset

@app.route('/<name>/')
def name(name):
    # company_name = raw_input("What company are you interested in? ")
    location = dataset.loc[name]
    return str(location)

# name(company_name)
#
app.run(debug=True)



