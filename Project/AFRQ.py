"""
AFRQ: Counting Disease Carriers

To model the Hardy-Weinberg principle.
Calculate the probability of a randomly selected individual carries at least
one copy of the recessive allele with a provided list contains the proportion
of homozygous recessive individuals for the k-th Mendelian factor in a diploid
population.

Hardy-Weinberg principle:
    Allele Frequencies Equation: p + q = 1 ==> p = 1 - q     (1)
    Genotype Frequencies Equation: p^2 + 2pq + q^2 = 1      (2)
        p^2: dominant homozygous frequency
        2pq: heterozygous frequency
        q^2 = A: recessive homozygous frequency
Probability of not dominant homozygous (modify (2)):
    P(not dominant homozygous) = 1 - p^2 = 2pq + q^2    (3)
Combine (1) and (3):
    P(not dominant homozygous) = 2(1-q)q + q^2
                               = 2q - q^2
                               = 2 * sqrt(A) - A
"""

from math import sqrt

def afrq(A):
    """
    Calculate the probability of a randomly selected individual carries
    at least one copy of the recessive allele and check the validation of
    the inputs

    :param A: the proportion of homozygous recessive individuals
    :type A: list
    :return: the probability of a randomly selected individual carries at
             least one copy of the recessive allele
    :rtype: list
    """
    if len(A) != 0:
        B = []
        for a in A:
            if (type(a) != int) and (type(a) != float):
                raise TypeError("You entered non-numeric values")
            else:
                if a < 0 or a > 1:
                    raise ValueError("You entered invalid values")
            P = 2 * sqrt(a) - a
            B.append(round(P, 3))
    else:
        raise IndexError("You entered an empty list")
    return B
