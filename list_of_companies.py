import pandas as pd
import numpy as np
import json
from flask import *
app = Flask(__name__)
########################################
# TASK: create function to list all the company names (strings)

### Dataset set up
dataset = pd.read_csv('Gender_pay_gap.csv')
dataset = dataset.head(15) # define test length of dataset eg top X employer names
employernames = dataset["EmployerName"] # creates series based on employer name column
employernamenewlist = employernames.tolist() #turns employee name series into list
# for employername in employernamenewlist:
#     print "after turning into list", str(employername)

employernames = employernames.str.replace(" ", "_", regex=True) # replaces all spaces in employer names with underscore - for flask routing
dataset.index = employernames #defines index of dataset to equal employer names with underscores.

########################################
industry = pd.read_csv('Industry.csv')

print industry




########################################



# FLASK help haha
#
@app.route("/list/")
def listofcompanies():
    # return str(employernamenewlist)
    # for employername in employernamenewlist:
    #     return str(employername)
    my_list = employernamenewlist
    return render_template("testview.html", foobar=my_list)




# @app.route("/<name>/")
# def companypage(name):
#     companystat = dataset.loc["{}".format(name)]
#     return str(companystat)
app.run(debug=True)

######################################
# TASK: sorting by industry
# for i in range(len(dataset)):
#     print dataset.loc[employernames[i]]

# sic_code = dataset["SicCodes"] #creates a series based on SicCodes column
# # print sic_code
# # # print sic_code.str.find(",")
# # for i in range(len(dataset)):
# #     code = sic_code[i]
# #     if code.find(",") > 0:
#         comma = code.find(",")
#         print code, " ", code.find(","), " new code is ", code[:comma]
#         sic_code[i] = code[:comma]
#     else:
#         print code
#
# print "new codes are", sic_code
#
# for value in dataset.values:


#     emp_name = value[0]
#     sic_code = value[3]
#
# #
# # # sic_code_array = []
# #
# # for i in range(5):
# #     if int(sic_code[i]) in range(10):
# #         print  i, " ", sic_code[i], type(sic_code[i])
# #     # elif int(sic_code[i]) not in range(10):
# #     else:
# #         print sic_code[0:i]
# #         # sic_code_array.append(sic_code[i])
# #         # print sic_code_array
#
#     return emp_name# , " and SIC Code ", sic_code


