import tinify
import os
import sys


tinify.key = ""


path = raw_input("Enter directory address: ");

if not path:
    print 'rerun and enter path again'
    sys.exit()


fileList=os.listdir(path);

print "compressing following files :- \n"
for filename in fileList:
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        print "processing "+ filename+'\n'
        source = tinify.from_file(os.path.join(path,filename))
        source.to_file(os.path.join(path,filename))

print "processing finished...."
