import os
import subprocess
import sys
import datetime
import argparse

def abs_file_paths(directory):
	for dirpath,_,filenames in os.walk(directory):
		for f in filenames:
			yield os.path.abspath(os.path.join(dirpath, f))



def main():
	#list of available formats to convert
	formats = [ 'epub', 'mobi', 'html', 'lit', 'rtf', 'txt', 'odt', 'pdf' ]
	
	#parse command line arguments
	ap = argparse.ArgumentParser(description='Batch convert between ebook formats.')
	ap.add_argument('--have', action='store', default='html', choices=formats)
	ap.add_argument('--want', action='store', default='epub', choices=formats)
	ap.add_argument('-s', '--src', default=os.getcwd())
	args = ap.parse_args()

	#Switch dirs to absolute paths
	src = os.path.abspath(args.src)

	#add period and string-ify things to be safe
	have = "." + str(args.have)
	want = "." + str(args.want)

	files = abs_file_paths(src)
	for f in files:
		if f.endswith(have):
			outfile = f[:-len(have)] + want
			if not os.path.exists(outfile):
				print("converting \ninfile=%s\noutfile=%s" % (f, outfile))
				subprocess.call(['ebook-convert', f, outfile])
			

if __name__ == '__main__':
	main()