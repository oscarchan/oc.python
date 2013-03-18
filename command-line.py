import argparse

parser = argparse.ArgumentParser(description='generate data.')
parser.add_argument('start', type=int, default=0,
                   help='starting index of the first user name generated')
parser.add_argument('end', type=int, default=9999,
                   help='ending index of the last user name generated')
parser.add_argument('--format', 
                   default="oc_loadtest_{0:04d}",
                   help='python string format for the user name')
parser.add_argument('--reset-if-exists',
                    action='store_true',
                    help="override the data if the data already exist")
parser.add_argument('--cvs-file', 
                    default="oc_loadtest.csv",
                    help='csv to store the user data')

args = parser.parse_args()
print args

print dir(args)
print "format=%s" %args.format
print "start=%s" % args.start
print "end=%s" % args.end
print "reset-if-exists=%s" % args.reset_if_exists
