'''
CISC 471 HW3
'''

import greedy
import greedy_unit

import randomized
import randomized_unit

import gibbs
import gibbs_unit

def main():
#Greedy Motif Search unit tests
    #Postivie unit tests
    print("Greedy Motif Search -- positive unit tests")
    print(greedy.greedyMotifSearch(greedy_unit.Dna1, greedy_unit.k1, greedy_unit.t1))
    print(greedy.greedyMotifSearch(greedy_unit.Dna2, greedy_unit.k2, greedy_unit.t2))

    #Negative unit tests
    print("Greedy Motif Search -- negative unit test")
    print(greedy.greedyMotifSearch(greedy_unit.Dna3, greedy_unit.k3, greedy_unit.t3))
    print("")

#Randomized Motif Search unit tests
    #Postivie unit tests
    print("Randomized Motif Search -- positive unit tests")
    print(randomized.getBestMotifs(randomized_unit.Dna1, randomized_unit.k1, randomized_unit.t1))
    print(randomized.getBestMotifs(randomized_unit.Dna2, randomized_unit.k2, randomized_unit.t2))

    #Negative unit tests
    print("Randomized Motif Search -- negative unit test")
    print(randomized.getBestMotifs(randomized_unit.Dna3, randomized_unit.k3, randomized_unit.t3))
    print("")

#Gibbs Sampler unit tests
    #Postivie unit tests
    print("Gibbs Sampler -- positive unit tests")
    print(gibbs.getBestMotifs(gibbs_unit.Dna1, gibbs_unit.k1, gibbs_unit.t1, gibbs_unit.N1, gibbs_unit.repeat1))
    print(gibbs.getBestMotifs(gibbs_unit.Dna2, gibbs_unit.k2, gibbs_unit.t2, gibbs_unit.N2, gibbs_unit.repeat2))

    #Negative unit tests
    print("Gibbs Sampler -- negative unit test")
    print(gibbs.getBestMotifs(gibbs_unit.Dna3, gibbs_unit.k3, gibbs_unit.t3, gibbs_unit.N3, gibbs_unit.repeat3))

main()
