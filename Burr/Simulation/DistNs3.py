import numpy as np


# class DistNS3(object):
#     """
#     This class is Distribution Implementation based on Inverse CDF to validate, generate random numbers
#
#     """

def burrdist(landa, c, k):
    """
    Inverse CDF of Burr Dist

    Args:
        :param landa: coefficient of X in dist
        :param c: coefficient
        :param k: coefficient

    """

    param = np.power(1 / (1 - np.random.rand()), 1 / k)
    result = landa * np.power(param - 1, 1 / c)

    return result


def dataGen(dim, randNum, size, fun, landa, c, k):
    hist = np.zeros(size)
    if fun == "burr":
        for i in range(0, randNum):
            rnd = dim * burrdist(landa, c, k)
            if rnd >= size:
                continue
            hist[int(rnd)] += 1
    hist *= dim / randNum
    return hist
