'''
CISC 471 HW3
Part1.2.1 Randomized Motif Search
'''

import random
import math

#Profile ← Profile(Motifs)
def profilePseudocounts(motifs):
    profile = []
    for i in range(len(motifs[0])):
        tempStr = ""
        for motif in motifs:
            tempStr += "".join(motif[i])
        tempList = []
        for base in "ATCG":
            tempList.append(round(float(tempStr.count(base)+1)/float(len(tempStr)+4), 4))
        profile.append(tempList)
    return profile

#Motifs ← Motifs(Profile, Dna)
def probableKmer(profile, Dna, k):
    probableKmers = []
    for seq in Dna:
        probable = [-1, None]   #Initialize the probable
        basesPos = {}
        bases = "ATCG"
        #Store bases and their corresponding index in a dictionary
        for key in bases:
            basesPos[key] = bases.index(key)
        #Calculate and store the k-mer with maximum probable
        for i in range(len(seq)-k+1):
            currentPos = 1
            seqIndex = 0
            for base in seq[i:i+k]:
                currentPos *= profile[seqIndex][basesPos[base]]
                seqIndex += 1
            if currentPos > probable[0]:
                probable = [currentPos, seq[i:i+k]]
        probableKmers.append(probable[1])
    return probableKmers

#Calculate the score of motifs
def score(motifs):
    seq = ""
    score = 0
    #Finding a most common sequence
    for i in range(len(motifs[0])):
        countA = 0
        countT = 0
        countC = 0
        countG = 0
        for motif in motifs:
            if motif[i] == "A":
                countA += 1
            elif motif[i] == "T":
                countT += 1
            elif motif[i] == "C":
                countC += 1
            elif motif[i] == "G":
                countG += 1
        if countA >= max(countT, countC, countG):
            seq += "A"
        elif countT >= max(countA, countC, countG):
            seq += "T"
        elif countC >= max(countA, countT, countG):
            seq += "C"
        elif countG >= max(countA, countT, countC):
            seq += "G"
    for motif in motifs:
        if len(seq) != len(motif):  #When seq and motif have different length
            score = math.inf
        else:
            for j in range(len(motif)):
                if seq[j] != motif[j]:  #Compare each base of seq and motif
                    score += 1  #Different base
    return score

def randomizedMotifSearch(Dna, k, t):
    motifs = []
    bestMotifs = []
    #Randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    for i in range(t):
        ranIndex = random.randint(0, len(Dna[i])-k)
        motifs.append(Dna[i][ranIndex:ranIndex+k])
    bestMotifs = motifs #BestMotifs ← Motifs
    while True:
        profile = profilePseudocounts(motifs) #Profile ← Profile(Motifs)
        motifs = probableKmer(profile, Dna, k)  #Motifs ← Motifs(Profile, Dna)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs #BestMotifs ← Motifs
        else:
            return bestMotifs

#Running randomizedMotifSearch(Dna, k, t) 1000 times
def getBestMotifs(Dna, k, t):
    bestMotifs = randomizedMotifSearch(Dna, k, t)
    bestScore = math.inf
    for i in range(1000):
        motifs = randomizedMotifSearch(Dna, k, t)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
            bestScore = score(motifs)
    if bestScore == math.inf:
        return "No best motifs"
    return bestMotifs
