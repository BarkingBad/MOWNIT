main:
	gcc zad2.c -o program -lgsl -lm -lgslcblas
	echo "N1V25000000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 1 25000000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N1V50000000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 1 50000000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N1V100000000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 1 100000000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N1V200000000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 1 200000000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N2V100, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 2 100; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N2V1000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 2 1000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N2V10000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 2 10000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv
	echo "N2V20000, " >> csv.csv
	truncate -s-1 csv.csv
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		time -f "%e," -o csv.csv -a ./program 2 20000; \
		truncate -s-1 csv.csv ; \
	done
	truncate -s-2 csv.csv
	echo "" >> csv.csv


	