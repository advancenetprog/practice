import os

def run(**args):
	print "dir"
	filenames = os.listdir(".")
	return str(filenames)