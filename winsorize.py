import scipy.stats as stats
import numpy as np
import csv

def run(n):
	data = np.genfromtxt('filtered_{}.csv'.format(n), delimiter=',', names=True)

	maximum = np.max(data['wealth'])
	minimum = np.min(data['wealth'])

	print minimum, maximum

	winsorized = stats.mstats.winsorize(data['wealth'], limits=0.05)

	maximum = max(winsorized)
	minimum = min(winsorized)

	print minimum, maximum

	# print len(winsorized)
	# print len(a)

	with open('filtered_{}_winsorized_5.csv'.format(n), 'wb') as csvfile:
	    writer = csv.writer(csvfile)
	    writer.writerow(['lat', 'lon', 'wealth'])
	    for x in zip(data, winsorized):
	        row = [x[0]['cogLat'], x[0]['cogLon'], x[1]]
	        writer.writerow(row)

run(1)
run(5)
run(10)
run(15)
run(20)
run(30)
