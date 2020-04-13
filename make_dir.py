#!/usr/bin/python36

import os

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

#define the name of the directory to be created
path = input("Enter the path of the directory you want to make\n")

# define the access rights
access_rights = 0o755

try:
	os.mkdir(path, access_rights)
except OSError:
	print ("Creation of the directory %s failed" % path)
else:
	print ("Successfully created the directory %s" % path)

