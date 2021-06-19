'''
CISC 471 HW3
Part1.3.1 Gibbs Sampler
'''

import random
import math

#Profile ← profile matrix constructed from all strings in Motifs except for Motifi
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

#Motifi ← Profile-randomly generated k-mer in the i-th sequence
def probableKmer(profile, seq, motifs):
    probableList = []
    for sk in range(len(seq)-len(motifs[0])+1):
        probableList.append(0)
        probable = 1
        for s in range(len(motifs[0])):
            if seq[sk+s] == "A":
                probable *= profile[s][0]
            elif seq[sk+s] == "T":
                probable *= profile[s][1]
            elif seq[sk+s] == "C":
                probable *= profile[s][2]
            elif seq[sk+s] == "G":
                probable *= profile[s][3]
        probableList[sk] = probable
    #Normalize probables
    sumProbable = sum(probableList)
    for i in range(len(seq)-len(motifs[0])+1):
        probableList[i] = probableList[i] / sumProbable
    #Count differences
    for i in range(1, len(probableList)-1):
        probableList[i] += probableList[i-1]
    #Get a random k-mer
    randomNum = random.random()
    for i in range(len(seq)-len(motifs[0])+1):
        if randomNum < probableList[i]:
            break
    probableKmers = seq[i:i+len(motifs[0])]
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

def gibbsSampler(Dna, k, t, N):
    motifs = []
    bestMotifs = []
    #Randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    for i in range(t):
        ranIndex = random.randrange(len(Dna[i])-k+1)
        motifs.append(Dna[i][ranIndex:ranIndex+k])
    bestMotifs = motifs #BestMotifs ← Motifs
    bestScore = score(bestMotifs)
    for j in range(1, N):
        i = random.randrange(t) #i ← Random(t)
        motifsNoi = motifs[0:i] + motifs[i+1:t]
        profile = profilePseudocounts(motifsNoi)    #Profile ← profile matrix constructed from all strings in Motifs except for Motifi
        motifs[i] = probableKmer(profile, Dna[i], motifsNoi)  #Motifi ← Profile-randomly generated k-mer in the i-th sequence
        if score(motifs) < bestScore:
            bestMotifs = list(motifs)   #BestMotifs ← Motifs
            bestScore = score(bestMotifs)
    return bestMotifs

def getBestMotifs(Dna, k, t, N, repeat):
    bestMotifs = gibbsSampler(Dna, k, t, N)
    bestScore = math.inf
    for i in range(repeat):
        motifs = gibbsSampler(Dna, k, t, N)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
            bestScore = score(motifs)
    if bestScore == math.inf:
        return "No best motifs"
    return bestMotifs
