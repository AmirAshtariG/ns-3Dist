import numpy as np
import coef

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


def ExtremeValue (mu, etta):
    val = -1 * etta * np.log(-1 * np.log(np.random.rand())) + mu
    return val


def Tloc (v, loc, scale):
    u = np.random.rand()
    val1 = 0
    x = Vcalc(u, v)
    for i in range(1, 10):
        val1 += coef.coef(i, v) * np.power(x, 2 * i + 1)
        print(val1)
    print((val1 + x) * scale + loc)
    return (val1 + x) * scale + loc


def Tloc2 (v, loc, scale):
    u = np.random.rand()
    val1 = 0
    x = VcalcLargeN(u, v)
    for i in range(1, 10):
        val1 += coef.coef(i, v) * np.power(x, 2 * i + 1)
      #  print("val in loop is :", val1)
  #  print((val1 + x) * scale + loc)
    return (val1 + x) * scale + loc

def gamma(n):
    if n < 2:
        return 1
    else:
        return (n-1) * gamma(n-1)


def Vcalc(u, n):
    x = gamma(n/2) / gamma((n+1)/2)
    val = (u - 0.5) * x * np.power((n * np.pi), 0.5)

    return val


def VcalcLargeN (u, n):
    x = (1 + (1/4 * n) + (1/32 * np.power(n, 2)) - 5/128 * np.power(n, 3) - 21/2048 * np.power(n, 4))
    val = (u - 0.5) * x * np.power((2 * np.pi), 0.5)

    return val


def dataGen(dim, randNum, size, fun, param1, param2, param3):
    hist = np.zeros(size)
    if fun == "burr":
        for i in range(0, randNum):
            rnd = dim * burrdist(param1, param2, param3)
            if rnd >= size:
                continue
            hist[int(rnd)] += 1
    elif fun == "Extreme":
        for i in range(0, randNum):
            rnd = dim * ExtremeValue(param1, param2)
            if rnd >= size or rnd < 0:
                continue
            hist[int(rnd)] += 1
    elif fun == "tloc":
        for i in range(0, randNum):
            rnd = dim * Tloc(param1, param2, param3) + size/ 2
            if rnd >= size:
                continue
            hist[int(rnd)] += 1
    elif fun == "tloc2":
        for i in range(0, randNum):
            rnd = dim * Tloc2(param1, param2, param3) + size / 2
            if rnd >= size:
                continue
            hist[int(rnd)] += 1
    else:
        print("No distribution Found!!!!!!")

    hist *= dim / randNum
    return hist
