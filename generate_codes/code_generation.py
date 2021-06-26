'''
Generating Unique Codes for students. These codes are used for authentication when collecting student preferences.
Codes are sent to students by email. Students are required to enter this unique code when submitting the form.
Each unique code contains 8 characters, alphanumeric. 'Case Sensitive'.

'''
from random import sample
import pandas as pd
import yaml

###################################################################################################
# reading config file for fetching paths
paths = open("../config.yaml", 'r')
paths_dictionary = yaml.load(paths)

# path to the file containing the unique codes shared to the students for authentication


# Input and Output Path
# CHANGE THESE AS PER REQUIREMENT #
STUDENT_LIST = paths_dictionary["STUDENT_LIST"] #Input file path (Excel file containing students information)
STUDENT_UNIQUE_CODES = paths_dictionary["STUDENT_UNIQUE_CODES"]
CODE_LENGTH = 8 #Length of unique codes
# Note: You can change the output format if you like


# Allowed characters - Lower and Upper case letters [a-z,A-Z] and Numbers [0-9]
small_alphs = [chr(ord('a')+i) for i in range(26)]
big_alphs = [chr(ord('A')+i) for i in range(26)]
nums = [str(i) for i in range(10)]
options = small_alphs+big_alphs+nums

# Reading Input
df = pd.read_excel(STUDENT_LIST)
num_studs = df.shape[0] # Num of students

# Generating codes
codes = set()
for i in range(num_studs):
    code = ""
    while True:
        for j in range(CODE_LENGTH):
            w = sample(options,1)[0]
            code+=w
        if code not in codes:
            codes.add(code)
            break
        code = ""
codes = list(codes)

# Writing Output
df["Unique Code"] = codes
df.to_excel(STUDENT_UNIQUE_CODES)