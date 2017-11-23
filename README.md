# Byzantine-Chain-Replication
Asynchronous systems project Fall 2017

Members:
	
	Jiajie Li - 109255512
	Raunak Shah - 111511721

PLATFORM:

	DistAlgo - version 1.0.9 
	Python - 3.5.2
	Operating System - macOS Sierra version 10.12.6 

INSTRUCTIONS:

	To build and run on same machine
	python -m da -f --logfilename logs/test1.replica.phase3.log -F output -n MainNode src/main.da config/test1.txt
	python -m da -f --logfilename logs/test1.client.phase3.log -F output -n ClientNode -D src/main.da config/test1.txt

	To built on multiple hosts
	python -m da -f --logfilename logs/test1.replica-phase3.log -F output -H <host_ip> -n MainNode src/main.da config/test1.txt
	python -m da -f --logfilename logs/test1.client.phase3.log -F output -n -H <host_ip> -R <peer_ip> ClientNode -D src/main.da config/test1.txt

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

Sometimes reconfiguration will run in an infinite loop. However, it will work normally for another run. It depends on the order of wedged responses received by Olympus

CONTRIBUTIONS:

	Jiajie Li - Pseudorandom request; Implement part of each da files; Generate some test cases; Reconfiguration; Logging; Testing

	Raunak Shah - Implementation of parts of source code files; Failure Injection; Logging; Reconfiguration; Testing


MAIN FILES:
	
	clients - Byzantine-Chain-Replication/src/client.da
	replicas - Byzantine-Chain-Replication/src/replica.da
	olympus - Byzantine-Chain-Replication/src/olympus.da
	main - Byzantine-Chain-Replication/src/main.da

CODE SIZE:

	algorithm ~ 1100 lines
	other ~ 400 lines
	total - 1459 lines

	Obtained the non-comment and non-blank lines of code from CLOC (https://github.com/AlDanial/cloc).
	Separted algorithms and other manually. About 70 % of the code in "algorithm" is for the algorithm itself and the rest deals with logging and failure injection.

LANGUAGE FEATURE USAGE:

	List comprehension used - 1
	Set comprehensions used - 2
	Aggregrations used - 3
	Quantifications used - 15 
