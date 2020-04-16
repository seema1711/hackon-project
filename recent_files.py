#!/usr/bin/python36

import os
import os.path,time
path=os.getcwd()
print("YOu are in", path,end="\n\n")
files = sorted(os.listdir(path), key=os.path.getctime)

oldest = files[0]
newest = files[-1]

print("Previously accessed\n",oldest)
print("Last modified: %s" % time.ctime(os.path.getmtime(oldest)))
print("Created: %s" % time.ctime(os.path.getctime(oldest)),end="\n\n")


print("Recently accessed\n",newest)
print("Last modified: %s" % time.ctime(os.path.getmtime(newest)))
print("Created: %s" % time.ctime(os.path.getctime(newest)))

