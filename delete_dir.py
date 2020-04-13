#!/usr/bin/python36
import os
# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)


 
# define the name of the directory to be deleted
path = input("Enter the file you want to delete\n")

try:
	os.rmdir(path)
except OSError:
	print ("Deletion of the directory %s failed" % path)
else:
	print ("Successfully deleted the directory %s" % path)

