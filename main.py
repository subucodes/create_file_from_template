import os


def read_file(file_name):
    with open(file_name, "r") as file_contents:
        content_string = file_contents.read()
    return content_string


def write_file(file_name, content):
    with open(file_name, "w") as open_file_in_write_mode:
        open_file_in_write_mode.write(content)


"""This is the place you need to change the name of the files (if intended)"""
file_with_data = "input.txt"
template_file = "template.txt"

resume_template_string = read_file(template_file)

for line in read_file(file_with_data).split("\n"):
    placeholder = line.split(":")[0]
    value = line.split(":")[-1].replace("\n", "")
    resume_template_string = resume_template_string.replace(
        "{" + placeholder + "}", value
    )
write_file(file_with_data, resume_template_string)
