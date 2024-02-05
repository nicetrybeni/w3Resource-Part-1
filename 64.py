# retrieve data and time of file creation 

import os.path, time

print(time.ctime(os.path.getmtime("60.py")))

print(time.ctime(os.path.getctime("60.py")))