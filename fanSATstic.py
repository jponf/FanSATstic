#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO DIMACS Parser
# TODO Solver Logic

from sys import argv, exit

__program__='FanSATstic - Local Search Sat Solver'
__authors__=['Marc Piñol Pueyo <mpp5@alumnes.udl.cat>',
			'Josep Pon Farreny <jpf2@alumnes.udl.cat>']
__copyright__='Copyright 2013, Marc Piñol Pueyo & Josep Pon Farreny'

__version__='0.1a'
__license__='GPL'

#
#
def Main():
	if len(argv) < 2:
		PrintHelp()
		exit(-1)

#
#
def OpenFileOrDie(fname, mode):
	"""
	OpenFileOrDie(fname:string, mode:string) : void
	Tries to open the specified file with the specified mode.
	Abort on failure.
	"""
	try:
		return open(fname, mode)
	except Exception:
		exit('Error opening file: %s' % fname)

#
#	
def PrintHelp():
	"""
	PrintHelp() : void
	Prints a help message on stdout
	"""
	print __program__
	print 'Version:', __version__, '\n'

	print 'Authors:\n', 
	for i in __authors__:
		print '\t%s' % (i)
	
	print 'Usage:\n%s <input-file>' % (argv[0])
	print '\tinput-file must be in dimacs cnf format'

if __name__ == '__main__':
	Main()