__author__ = 'Konovalov Alexaknder <aleksaander@ya.ru>'

import os

# count code stat in the path
def count_stat_for_path(dir, file_extentions):
    files = os.listdir(dir)
    for file in files:
        file_full_name = dir + '/' + file
        if os.path.isfile(file_full_name):
            for file_extention in file_extentions:
                if file.endswith(file_extention):

                    # all lines
                    lines = [line for line in open(file_full_name, 'r')]

                    # exclude empty lines
                    lines = [line for line in lines if not line.isspace()]

                    # exclude comments
                    lines = [line for line in lines if not line.strip().startswith('#')]

                    code_counter['total lines'] += len(lines)
                    code_counter['total files'] += 1
        else:
            count_stat_for_path(file_full_name, file_extentions)

# you may edit that variables
file_extensions = ['.py', '.sh']
current_dir = os.getcwd()

# initialize statistics
code_counter = {'total lines': 0, 'total files': 0}

count_stat_for_path(current_dir, file_extensions)
print(code_counter)