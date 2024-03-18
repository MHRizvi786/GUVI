import glob
import os
from datetime import datetime
"""
1)Write a  Python Program using function which will do the following.
a)Th function will create a text file with current timestamp.
b)The file  should have the content of the current timestamp.
"""
# import module
from datetime import datetime

# get current date and time
def file_create():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)

    # convert datetime object to string
    str_current_datetime = str(current_datetime)

    # create a file object along with extension
    file_name = "D://SeleniumProjects//"+str_current_datetime + ".txt"
    file = open(file_name, 'w')
    print("File created : ", file.name)
    #writing the current timestamp into file.
    file.write(str_current_datetime)
    file.close()
file_create()


"""
2)Write another Python Program to read from a text file.The function will take the name of the file  and display the content of file on console.

"""
    #func_read()
def file_read():
    #reading file with latest timestamp
    files=glob.glob("D://SeleniumProjects//*")
    latest_file=max(files,key=os.path.getctime)
    #opening the latest file with the timestamp and printing it.
    f1=open(latest_file,'r+')
    print(f1.read())
file_read()


