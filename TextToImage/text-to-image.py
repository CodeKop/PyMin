from argparse import ArgumentParser
from PIL import Image

def setup_parser():
	parser = ArgumentParser(description="Program to convert text file to image.")

	parser.add_argument("filename", help="The name of the input file to convert.")
	parser.add_argument("-e", "--ext", help="The file extension of the output file.", default="jpg", choices=["jpg", "png", "gif"])
	parser.add_argument("-o", "--out", help="The name of the file to output as.", default="out.[ext]")
	parser.add_argument("-s", "--scale", help="The amount to scale the outputted image by. Scale of 1 is equal to font-size 16px.", default=1)
	parser.add_argument("-p", "--padding", help="The amount of padding surrounding the edge of the file.", default="5"))

	return parser.parse_args

def readfile(filename):
	f = open(filename, mode='r')
	return f.readlines()


if __name__ == '__main__':
	args = setup_parser()
	file_data = readfile(args.filename)
	longest = max(file_data)

	
