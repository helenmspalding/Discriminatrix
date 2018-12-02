import pandas as pd
import numpy as np
from Industry_Codes import *
from flask import *
app = Flask(__name__)
########################################
# TASK: create function to list all the company names (strings)
#
### Dataset set up
dataset = pd.read_csv('Gender_pay_gap.csv')

dataset= dataset[["EmployerName","SicCodes","DiffMedianHourlyPercent"]]
dataset = dataset.head(50) # define test length of dataset eg top X employer names


employernames = dataset["EmployerName"] # creates series based on employer name column
# employernamenewlist = employernames.tolist() #turns employee name series into list

#### replacing all Sic codes with the first sic code
sic_code = dataset["SicCodes"] #creates a series based on SicCodes column
for i in range(len(dataset)):
    code = str(sic_code[i])
    if code.find(",") > 0:
        comma = code.find(",")
        # print code, " ", code.find(","), " new code is ", code[:comma]
        dataset.loc[i,"SicCodes"] = code[:comma] #replaces with all values of string up to the comma

########################################
#### Industry sorting in Industry_Codes.py
##### searches Sic Code in industry csv and assigns industry
dataset["Industry"] = np.NaN
##### print dataset
# industry = pd.read_csv('Industry.csv')
# codenumber= industry["Code"]
# sectionrow = industry.loc[codenumber.str.startswith("Secti")].index.values.astype(int)#[0]
# # print sectionrow
# industrynames = industry["Description"].iloc[sectionrow].tolist()
# industrydict = {}
# industryaverages = {}
#


print "******************"
#
#
# for i in range(len(industrynames)):  #creates dictionary with key = industry and values = codes
#     if i == len(sectionrow)-1:
#         industrydict['%s' % industrynames[i]] = codenumber[sectionrow[i] + 1:].tolist()
#
#     else:
#         industrydict['%s' % industrynames[i]] = codenumber[sectionrow[i]+1:sectionrow[i+1]].tolist()

for i in range(len(dataset)): #asigns industry depending on sic code
    for item in industrydict: #searches for each industry name (item)
        if str(sic_code[i]) in industrydict[item]: #if sic code is in the values in the industry name dictionary
            dataset.loc[i,"Industry"] = item #Industry name saved in industry column
print dataset
print "*******************"

for i in range(len(industrydict)):
    industryname = industrynames[i]
    industry_list = dataset.loc[dataset['Industry'] == industryname].index.values.tolist()
    industry_av = dataset.loc[industry_list,["DiffMedianHourlyPercent"]].values.mean().astype(float)
    industryaverages['%s' % industryname] = industry_av
    print industryname, " ", industry_list, " ", industry_av
print industryaverages

#######################################


employernames = employernames.str.replace(" ", "_", regex=True) # replaces all spaces in employer names with underscore - for flask routing
dataset.index = employernames #defines index of dataset to equal employer names with underscores.

# FLASK help haha
#
# @app.route("/list/")
# def listofcompanies():
#     # return str(employernamenewlist)
#     # for employername in employernamenewlist:
#     #     return str(employername)
#     my_list = employernamenewlist
#     hyperlink_list = employernames
#     return render_template("testview.html", linktext=my_list,hyperlink = hyperlink_list)
#
# @app.route('/<name>/')
# def name(name):
#     # company_name = raw_input("What company are you interested in? ")
#     location = dataset.loc[name]
#     return str(location)
#
# app.run(debug=True)

######################################
# TASK: sorting by industry
# for i in range(len(dataset)):
#     print dataset.loc[employernames[i]]

