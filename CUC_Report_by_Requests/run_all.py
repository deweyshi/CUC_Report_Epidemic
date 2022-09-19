import os
import logging

# Save logs
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

tgt_dir_nm = "CUC_Report"

os.chdir(os.getcwd() + '/' + tgt_dir_nm)
file_list = os.listdir(os.getcwd())
for filename in file_list:
  if os.path.isfile(filename) and filename.endswith('.py') and filename.find("run") == -1:
      logging.info(filename)
      os.system(f'python {filename}')