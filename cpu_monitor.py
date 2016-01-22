from subprocess import check_output as execCommand

def parse_args():
	import argparse
	import itertools
	import sys

	parser = argparse.ArgumentParser(description='Provide graph for CPU usage of a specific running program')
	parser.add_argument('pid', action='store', help='PID to monitor')
	parser.add_argument('samples', action='store', help='Number of samples')
	if len(sys.argv)!=3:
		parser.print_help()
		sys.exit(1)
	return parser.parse_args()

def main():
	args = parse_args()
	if (int(args.samples) < 10):
		print "Samples must be at least 10"
		return

	execCommand("rm -f tmp", shell = True)

	# PID Checking
	execCommand("top -p " + str(args.pid) + " -n1 -b | awk '/" + str(args.pid) + "/{print $12\"\t\" $10}' >> tmp", shell = True)
	if len(tuple(open('./tmp', 'r'))) == 0:
		execCommand("rm -f tmp", shell = True)
		print "Error: PID not found"
		return

	execCommand("rm -f graph.png", shell = True)
	print "Start scanning..."
	for i in range(0, int(args.samples)):
		execCommand("top -p " + str(args.pid) + " -n1 -b | awk '/" + str(args.pid) + "/{print \"" + str(i) + " \t\" $9}' >> tmp", shell = True)
	execCommand("sudo gnuplot gplotscript", shell = True)

	# Check sample size
	if len(tuple(open('./tmp', 'r'))) < 10:
		print "Error: Not enough samples"
		return

	lines = tuple(open('./tmp', 'r'))
	count = 0
	mysum = 0.0
	for line in lines:
		mysum += float(line.split('\t')[1].replace(',','.'))
		count += 1
	print "Average CPU load: " + str(float(mysum)/float(count))

if __name__ == "__main__":
	main()
