import os

def run(**args):
	filenames = os.listdir(".")
	return str(filenames)