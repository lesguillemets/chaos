#!/bin/bash
for i in `ls *.dat`
do
	echo "set size square
set term png font ubuntu size 800,800
set xrange[-40:40]
set yrange[-40:40]
set output '$i.png'
plot '$i' w d lc rgb 'blue'" | gnuplot
done
