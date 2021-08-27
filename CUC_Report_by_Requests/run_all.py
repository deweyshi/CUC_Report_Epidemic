import os

file_list = os.listdir(os.getcwd())
print(file_list)
for filename in file_list:
    if os.path.isfile(filename) and filename.endswith('.py') and filename.find("run") == -1:
        print(filename,'\n')
        os.system('python {}'.format(filename))