import numpy as np
import sklearn.cluster as cl
import csv


def run(n):
    print "run", n

    data = np.genfromtxt('filtered_{}_winsorized_5.csv'.format(n), delimiter=',', names=True)
    # data = np.genfromtxt('sample_winsor.csv', delimiter=',', names=True)

    locations = np.column_stack((data['lat'], data['lon']))

    kmeans = cl.MiniBatchKMeans(n_clusters=25000, reassignment_ratio=0, verbose=True)
    # kmeans = cl.KMeans(n_clusters=500)

    kmeans.fit(locations)

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # print labels
    # print centroids

    clusters = {}

    for i in xrange(len(data)):
        lab = labels[i]
        d = data[i]
        if lab not in clusters:
            latlon = centroids[lab]
            clusters[lab] = [0, 0, lab, latlon[0], latlon[1]]
        clusters[lab][0] += 1  # count
        clusters[lab][1] += d[2]  # weight

    with open('filtered_{}_clustered.csv'.format(n), 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['lat', 'lon', 'wealth', 'numClusters'])
        for row in clusters.iteritems():
            row = row[1]
            writer.writerow([row[3], row[4], float(row[1])/row[0], row[0]])

run(1)
run(5)
run(10)
run(15)
run(20)
run(30)