# IIT Gandhinagar - HSS Course Allotment Tool
Welcome to the HSS Course Allotment Tool. 

### Requirements
This tool requires Python3. Run the following command to get all the required libraries.
<pre>
pip install -r requirements.txt
</pre>

This tool involves three major components, which are required to be executed in the following order:
- Unique Codes Generation
- Student Preferences Input Form
- Allocation

## Unique Code Generation
Folder: `/generate_codes`

This component deals with generating unique codes that act as a basic student authentication. These codes are shared to students by email and they are required to submit this code when they fill their preferences in the Student Preferences Input Form.

*This requires an excel file containing Students Information. This path information must be mentioned in `config.yaml`.*

Run the following command (inside the `/generate_codes` folder).
<pre>
python code_generation.py
</pre>

In case you need to generate a new code for a student for whom the code was not generated before, you can run use the `code_addition.py` file.
<pre>
python code_addition.py
</pre>

## Student Preferences Input Form
Folder: `/form`

This component deals with the UI and Backend of the form used to collect student preferences.
### User Interface
- To make changes to the User Interface, make changes in `index.html`. CSS and JS files and images can be found in the folder `assets`.
- The file `index_done.html` can be used when the form is closed.

### Form Validation
The form validation can be found in `index.js`. Go through this file to understand how the validations work. *Also, to add courses as options in the dropdown, you have to add the courses data to `index.js` as a `json` object. You can use [this](https://beautifytools.com/excel-to-json-converter.php) tool for this purpose.*

### Collecting Form Responses
We used Google App Script for this purpose. 
- Create a spreadsheet on Google Sheets.
- Go to `Tools`, then `Script Editor`
- Copy the code prsent in `form/code.gs` and paste it in the script editor.
- In the toolbar, select the function `setup` and click `Run`.
- Select `Deploy`, then `New Deployment`. Under `Web app`, choose `Me` option under `Execute as`, and `Anyone` under `Who has access`. Then, Deploy.
- Copy the URL of the Web app and paste it in `index.js` (at the variable `scriptURL`).

Once you complete the above steps, the responses from the form are stored in the Google Sheets.

## Final Allocation
Folder: `/code`

The final component is the Course Allocation. This step is to be executed after receiving the final responses from students. The details of the algorithm used for student-course allocation is described [here](link).

To run the allocation code, below are the requirements.

### Instructions to run the code
- Edit `config.yaml` to provide paths of the input and output files or just replace the files in courses_data, students_data folders and output files will be generated in output folder.
- On the Terminal, run the following command
<pre>
python main.py
</pre>
- The Output allocation is stored at the Output file path specified in `config.yaml`.
- Insights, if required, can also be modified as per requirement. The output folder path must be specified in `config.yaml`.