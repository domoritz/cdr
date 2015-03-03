import numpy as np
import scipy.stats as stats
from math import radians, cos, sin, asin, sqrt

# http://stackoverflow.com/a/15737218/214950
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

data = np.genfromtxt('cdrMapData_filtered_nan.csv', delimiter=',', names=True)
# data = np.genfromtxt('sample.csv', delimiter=',', names=True)

distances = np.vectorize(haversine)

res = distances(data['modalLon'], data['modalLat'], data['cogLon'], data['cogLat'])

# print stats.describe(res)

header = ",".join(data.dtype.names)

filtered = data[np.where(res < 1)];
np.savetxt("filtered_1.csv", filtered, delimiter=",", header=header, fmt="%.10e")

filtered = data[np.where(res < 5)];
np.savetxt("filtered_5.csv", filtered, delimiter=",", header=header, fmt="%.10e")

filtered = data[np.where(res < 10)];
np.savetxt("filtered_10.csv", filtered, delimiter=",", header=header, fmt="%.10e")

filtered = data[np.where(res < 15)];
np.savetxt("filtered_15.csv", filtered, delimiter=",", header=header, fmt="%.10e")

filtered = data[np.where(res < 20)];
np.savetxt("filtered_20.csv", filtered, delimiter=",", header=header, fmt="%.10e")

filtered = data[np.where(res < 30)];
np.savetxt("filtered_30.csv", filtered, delimiter=",", header=header, fmt="%.10e")
