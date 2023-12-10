# create_file_from_template
A simple logic where you define the input in one text file called 'input.txt' and template defined in another called 'template.txt. 
Running this code would overwrite the 'input.txt' with contents of template file replacing the placeholders with input data you provided in 'input' text file.

## Before you run the main.py:
#### input.txt
name: Subbu<br>
role: Python Developer<br>
company: Google<br>

#### template.txt
Hi,<br> 
This is {name} and I currently work as {role} in {company}.


## After you run the main.py:
#### input.txt
Hi,<br> 
This is Subbu and I currently work as Python Developer in Google.
