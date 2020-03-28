import sys
import os

for line in sys.stdin:
	try:
		print(line, end='')
	except BrokenPipeError:
		sys.stderr.close()
