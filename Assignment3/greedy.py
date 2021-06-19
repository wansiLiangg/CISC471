'''
CISC 471 HW3
Part1.1.1 Greedy Motif Search
'''

import math

#Form profile from motifs Motif1, …, Motifi - 1
def profileMotifs(motifs):
    profile = {}
    A = []
    T = []
    C = []
    G = []
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
        A.append(countA)
        T.append(countT)
        C.append(countC)
        G.append(countG)
    profile["A"] = A
    profile["T"] = T
    profile["C"] = C
    profile["G"] = G
    return profile

#Profile-most probable k-mer in the i-th string in Dna
def probableKmer(seq, k, profile):
    bases = []
    probable = ""
    dicIndex = {}
    #Obtain the data from profile and store it to the corresponding position in bases
    for i in range(k):
        bases.append([])
        for base in "ATCG":
            bases[i].append(profile[base][i])
    #Find the base with max value based on the index
    for j in range(len(bases)):
        maxNumIndex = bases[j].index(max(bases[j]))
        if maxNumIndex == 0:
            maxBase = "A"
        elif maxNumIndex == 1:
            maxBase = "T"
        elif maxNumIndex == 2:
            maxBase = "C"
        elif maxNumIndex == 3:
            maxBase = "G"
        probable += str(maxNumIndex)
    #Obtain porbable kmers
    for sk in range(len(seq)-k+1):
        seqkmer = seq[sk:sk+k]
        index = 1
        for s in range(len(seqkmer)):
            if seqkmer[s] == "A":
                i = 0
            elif seqkmer[s] == "T":
                i = 1
            elif seqkmer[s] == "C":
                i = 2
            elif seqkmer[s] == "G":
                i = 3
            index *= bases[s][i]
        dicIndex[seqkmer] = index
    #Find a key with max value in the dictionary
    for key, value in dicIndex.items():
        if value == max(dicIndex.values()):
            return key

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

def greedyMotifSearch(Dna, k, t):
    bestMotifs = []
    bestScore = math.inf
    for seq in Dna:
        bestMotifs.append(seq[:k])  #Motif matrix formed by first k-mers in each string from Dna
    for first in range(len(Dna[0])-k+1):    #For each k-mer Motif in the first string from Dna
        motifs = [Dna[0][first:(first+k)]]   #Motif1 ← Motif
        for i in range(1, t):   #For i = 2 to t
            profile = profileMotifs(motifs) #Form profile from motifs Motif1, …, Motifi - 1
            probable = probableKmer(Dna[i], k, profile) #Profile-most probable k-mer in the i-th string in Dna
            motifs.append(probable)     #Motifs ← (Motif1, …, Motift)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs #BestMotifs ← Motifs
            bestScore = score(motifs)
    if bestScore == math.inf:
        return "No best motifs"
    return bestMotifs
