# Byzantine-Chain-Replication
Asynchronous systems project Fall 2017

Members:
Jiajie Li - 109255512
Raunak Shah - ID

PLATFORM:
DistAlgo - version 1.0.9 
Python - 3.5.2
Operating System - macOS Sierra version 10.12.6 

INSTRUCTIONS:
To build and run testcase 1
	python -m da -f --logfilename logs/test1.log -F output src/main.da config/test1.txt

WORKLOAD GENERATION:
We get a random number from 0 to 100 using the given seed, and we limit it to generate (n/3) + 1 key values only. 
When we get a random number, we divide it by 4 and get its division, and get which operation we are doing. We also divide it by number of keys to get a division as the key value.

For put operation, divide random number by n and get its division as the value.
For example, if key value = 1 and value = 2, the operation is put('key_1','value_2')

For get operation, we use the key value generated the same way as above as its argument.
For example, if key value = 0, operation is get('key_0')

For slice operation, divide random number by 3 to get a division as the starting slice number. Then divide it by 5 to get a division as the ending slice number.
If start is larger than end, then we make end = start + start - end
The key value is generated the same way as above.
For example, if key value = 0, start = 2 and end = 4, operation is slice('key_0','2:4')

For append operation, divide random number by n and get its division as the append value.
The key value is generated the same way as above.
For example, if key value = 0 and append value = 3, operation is append('key_0','value_3')

BUGS AND LIMITATIONS:
Have not configured to run on multiple hosts. Currently only running on one host.
No reconfig request or reconfig detection by client. If client timeout during retransmission request, it simply skips the request and moves on.

CONTRIBUTIONS:
Jiajie Li - 
Pseudorandom request; 
Implement part of each da files;
Generate some test cases;

Raunak Shah -


MAIN FILES:
clients - Byzantine-Chain-Replication/src/client.da
replicas - Byzantine-Chain-Replication/src/replica.da
olympus - Byzantine-Chain-Replication/src/olympus.da
main - Byzantine-Chain-Replication/src/main.da

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
