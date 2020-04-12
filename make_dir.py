#!/usr/bin/python36

import os
print('''
	Press 1 to make a file/directory \n
	Press 2 to delete a file/directory\n
	''')
user_input=input()
if user_input=='1':

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

else:
	# define the name of the directory to be deleted
	path = input("Enter the file you want to delete\n")

	try:
	    os.rmdir(path)
	except OSError:
	    print ("Deletion of the directory %s failed" % path)
	else:
	    print ("Successfully deleted the directory %s" % path)
