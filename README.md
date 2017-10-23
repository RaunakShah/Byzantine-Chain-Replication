# Byzantine-Chain-Replication
Asynchronous systems project Fall 2017

PLATFORM:
DistAlgo - version 1.0.9 
Python - 3.5.2
Operating System - macOS Sierra version 10.12.6 

INSTRUCTIONS:
To build and run testcase 1
	python -m da -f --logfilename logs/test1.log -F output src/main.da config/test1.txt

WORKLOAD GENERATION:


BUGS AND LIMITATIONS:
Have not configured to run on multiple hosts. Currently only running on one host.

CONTRIBUTIONS:

MAIN FILES:
clients - Byzantine-Chain-Replication/src/client.da
replicas - Byzantine-Chain-Replication/src/replica.da
olympus - Byzantine-Chain-Replication/src/olympus.da


CODE SIZE:
	algorithm - 523 lines
	other - 129 lines
	total - 652 lines

	Obtained the non-comment and non-blank lines of code from CLOC (https://github.com/AlDanial/cloc).
	Separted algorithms and other manually. About 70 % of the code in "algorithm" is for the algorithm itself and the rest deals with logging and failure injection.

LANGUAGE FEATURE USAGE:
List comprehension used - 1
Set comprehensions used - 1
Aggregrations used - 1
Quantifications used - 9 
