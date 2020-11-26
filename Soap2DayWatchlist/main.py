from argparse import ArgumentParser
import run

def setup_parser():
	parser = ArgumentParser()

	return parser.parse_args()

if __name__ == "__main__":
	run.main(setup_parser())
