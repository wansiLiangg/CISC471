"""
AFRQ Extension

Expand the Hardy-Weinberg Principle to calculate the probability of a randomly
selected individual carries at least one copy of the recessive allele of
polyploid organisms (n-ploid) with 2 alleles based on the number of recessive
homozygous frequency.

Expanded Hardy-Weinberg Principle:
    Allele Frequencies Equation: p + q = 1 ==> p = 1 - q     (1)
    Genotype Frequencies Equation:  (2)
        p^n + k1*p^(n-1)*q^1 + k2*p(n-2)*q^2 + ... + kn-1*p^1*q^(n-1) + q^n = 1
            p^n: dominant homozygous frequency
            k1*p^(n-1)*q^1 + ... + kn-1*p^1*q^(n-1): heterozygous frequency
                k1 ... kn-1: coefficients can get from the Pascal's Triangle
            q^n = A: recessive homozygous frequency
    Probability of not dominant homozygous (modify (2)):
        P(not dominant homozygous) = 1 - p^n
                                   = k1*p^(n-1)*q^1 + ... + kn-1*p^1*q^(n-1)
                                     + q^n      (3)
    Combine (1) and (3):
    P(not dominant homozygous) = k1*(1-q)^(n-1)*q^1 + ... + kn-1*(1-q)^1*q^(n-1)
                                 + q^n
"""

def checkInput(n, qPowerN):
    """
    Check if the input values are valid

    :param n: the number of sets of chromosomes in a cell
              (n-ploid, n must be an even number)
    :type n: suppose to be an integer
    :param qPowerN: the number of recessive homozygous frequency
    :type qPowerN: suppose to be a float

    :return: the validation status of the input values
    :rtype: list
    """
    status = [False, False]
    try:
        n = int(n)
        qSquare = float(qPowerN)
        if n > 0:
            status[0] = True
        if qPowerN >= 0 and qPowerN <= 1:
            status[1] = True
    except:
        None
    return status

def getCoefficient(n):
    """
    Use the Pascal's Triangle to get the get coefficient of each genotype
    frequency

    :param n: the number of sets of chromosomes in a cell
              (n-ploid, n must be an even number)
    :type n: integer

    :return: a list of coefficient of each genotype frequency
    :rtype: list
    """
    curList = [1, 1]
    for row in range(2, n+1):
        preList = curList
        curList = [1]
        for column in range(len(preList)-1):
            curList.append(preList[column] + preList[column+1])
        curList.append(1)
    return curList

def afrqExtension(n, qPowerN):
    """
    Calculate the probability of a randomly selected individual carries at
    least one copy of the recessive allele based on the number of recessive
    homozygous frequency, and the number of sets of chromosomes in a cell.

    :param n: the number of sets of chromosomes in a cell
              (n-ploid, n must be an even number)
    :type n: integer
    :param qSquare: the number of recessive homozygous frequency
    :type qSquare: float

    :return: the probability of a randomly selected individual carries at
             least one copy of the recessive allele
    :rtype: float
    """
    coefficient = getCoefficient(n)[1:]
    q = qPowerN ** (1.0 / n)
    p = 1 - q
    pPower = n-1
    qPower = 1
    prob = 0
    for i in range(n):
        prob += coefficient[i] * pow(p, pPower) * pow(q, qPower)
        pPower -= 1
        qPower += 1
    return round(prob, 3)

def afrqExtensionMain(n, qPowerN):
    """
    Main function: combine functions together

    :param n: the number of sets of chromosomes in a cell
    :type n: list
    :param qSquare: the number of recessive homozygous frequency
    :type qSquare: list
    """
    if len(n) == len(qPowerN):
        if len(n) != 0:
            B = []
            for i in range(len(n)):
                validation = checkInput(n[i], qPowerN[i])
                if False in validation:
                    raise ValueError("You entered invalid values")
                B.append(afrqExtension(n[i], qPowerN[i]))
        else:
            raise IndexError("You entered an empty list")
    else:
        raise IndexError("Different length of the input lists")
    return B
