# -*- coding: utf-8 -*-
import tinify
import os
import sys


tinify.key ="enter your api key here"


path = raw_input("Enter directory address: ");

if not path:
    print 'rerun and enter path again'
    sys.exit()


# fileList=os.listdir(path);
filePath =[]

for folder, subs, files in os.walk(path):
  for filename in files:
    filePath.append(os.path.abspath(os.path.join(folder, filename)))

# print filePath

print "compressing following files :- \n"
for filename in filePath:
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') :
        if  not  filename.endswith('.9.png'):
            print "processing "+ filename+'\n'
            source = tinify.from_file(filename)
            source.to_file(filename)

print "processing finished...."
