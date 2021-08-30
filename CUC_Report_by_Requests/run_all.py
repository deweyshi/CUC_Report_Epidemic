import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

file_list = os.listdir(os.getcwd())
logging.info(file_list)
for filename in file_list:
    if os.path.isfile(filename) and filename.endswith('.py') and filename.find("run") == -1:
        logging.info(filename)
        os.system('/root/anaconda3/bin/python {}'.format(filename))
