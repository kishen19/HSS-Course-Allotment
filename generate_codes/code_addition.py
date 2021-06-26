'''
In case you need to generate a unique code for a student manually, you can use this file. This file outputs a new code different from all the codes present in the input file. The output is printed on the Terminal.

'''

from random import sample
import pandas as pd

# Input Path
# CHANGE THESE AS PER REQUIREMENT #
INPUT_PATH = './Students_Unique Codes.xlsx' #Input file path (Excel file containing students information)
CODE_LENGTH = 8 #Length of unique code

# Allowed characters - Lower and Upper case letters [a-z,A-Z] and Numbers [0-9]
small_alphs = [chr(ord('a')+i) for i in range(26)]
big_alphs = [chr(ord('A')+i) for i in range(26)]
nums = [str(i) for i in range(10)]
options = small_alphs+big_alphs+nums

# Reading Input
df = pd.read_excel(INPUT_PATH)

codes = set(df["Unique Code"]) #All existing codes

# Generating New Code
code = ""
while True:
    for j in range(8):
        w = sample(options,1)[0]
        code+=w
    if code not in codes:
        codes.add(code)
        break
    code = ""

# Output
print("New Code:",code)