import re
def print_baby_names(html_file):
    name_list = []
    with open(html_file,'r') as NameFile:
        file_content = NameFile.readlines()
        for name in file_content:
            baby_name = re.findall(r"<li>(.*)</li>",name)
            if baby_name:
                name_list.append(baby_name[0])
    return name_list
print(print_baby_names('baby_names.html'))
