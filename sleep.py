import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='puts computer to sleep',formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-m', metavar='minutes',nargs=1,default=0,help='type how many minutes to wait before sleep')
parser.add_argument('-s', metavar='mseconds',nargs=1,default=0,help='type how many seconds to wait before sleep')
args = parser.parse_args()

if type(args.m) is not int:
	mins = int(args.m[0])
	for x in range(0,mins):
		print("Sleep in",mins-x,"minutes")
		time.sleep(60)
	subprocess.call("systemctl suspend", shell=True)
elif type(args.s) is not int:
	sec = int(args.s[0])
	for i in range(0,sec):	
		if i % 10 == 0:
			print("Sleep in",sec-i,"seconds")
		time.sleep(1)
	subprocess.call("systemctl suspend", shell=True)
