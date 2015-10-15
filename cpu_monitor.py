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
    execCommand("rm -f tmp", shell = True)
    execCommand("rm -f graph.png", shell = True)
    for i in range(0, int(args.samples)):
        execCommand("top -p " + str(args.pid) + " -n1 | awk '/ " + str(args.pid) + " /{print $12\"\t\" $10}' >> tmp", shell = True)
    execCommand("gnuplot gplotscript", shell = True)
    lines = tuple(open('./tmp', 'r'))
    count = 0
    mysum = 0.0
    for line in lines:
        mysum += float(line.split('\t')[1].replace(',','.'))
        count += 1
    print "Average CPU load: " + str(float(mysum)/float(count))
    execCommand("eog graph.png", shell = True)

if __name__ == "__main__":
    main()
