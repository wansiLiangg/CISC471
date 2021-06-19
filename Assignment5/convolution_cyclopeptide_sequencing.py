'''
CISC 471 HW5
Part1.1 Convolution Cyclopeptide Sequencing
'''

#Taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200
def newSpectrum(spectrum, M):
    #Expand spectrum and get masses that fall in [57, 200]
    expandSpectrum = []
    for i in spectrum:
        for j in spectrum:
            mass = i - j
            if mass >= 57 and mass <= 200:
                expandSpectrum.append(mass)
    #Count the frequency of each mass shows up
    countMass = {}
    for i in expandSpectrum:
        if i in countMass.keys():
            countMass[i] += 1
        else:
            countMass[i] = 1
    countMassList = list(countMass.items())
    countMassList.sort(key=lambda x:x[1], reverse=True)
    #Get top M elements
    reducedMassList = []
    #When M is greater than the length of the countMassList
    if M >= len(countMassList):
        for i in countMassList:
            reducedMassList.append(i[0])
    else:   #When M is less than the length of the countMassList
        tie = countMassList[:M][-1][1]
        for i in countMassList:
            if i[1] >= tie:
                reducedMassList.append(i[0])
    return reducedMassList

#Leaderboard ← Expand(Leaderboard)
def expand(leaderboard, newSpectrumList):
    expandList = []
    for peptide in leaderboard:
        for mass in newSpectrumList:
            expandList.append(peptide + [mass])
    return expandList

#if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
def score(peptide, spectrum):
    totalMass = [0, sum(peptide)]
    combinedPeptide = peptide + peptide
    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            subpeptide = combinedPeptide[j:j+i]
            totalMass.append(sum(subpeptide))
    totalMass.sort()
    #Calculating score
    score = 0
    masses = set(totalMass + spectrum)
    for mass in masses:
        score += min(totalMass.count(mass), spectrum.count(mass))
    return score

#remove Peptide from Leaderboard
def remove(leaderboard, peptide):
    newPeptide = []
    for i in leaderboard:
        if i != peptide:
            newPeptide.append(i)
    return newPeptide

#Leaderboard ← Cut(Leaderboard, Spectrum, N)
def cut(leaderboard, spectrum, N):
    #When the size of leaderboard is less than N
    if len(leaderboard) <= N:
        return leaderboard
    #When the size oof leaderboard is greater than N, get score of each peptide
    scores = {}
    for i in range(len(leaderboard)):
        scores[i] = score(leaderboard[i], spectrum)
    scoresList = list(scores.items())
    scoresList.sort(key=lambda x:x[1], reverse=True)
    threshold = scoresList[N-1]
    #Update leaderboard
    newLeaderboard = []
    for i in range(len(scoresList)):
        if scoresList[i][1] >= threshold[1]:
            index = scoresList[i][0]
            newLeaderboard.append(leaderboard[index])
    return newLeaderboard

def convolutionCyclopeptideSequencing(spectrum, M, N):
    leaderboard = [[]]  #Leaderboard ← {0-peptide}
    leaderPeptide = [] #LeaderPeptide ← 0-peptide
    #Taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200
    newSpectrumList = newSpectrum(spectrum, M)
    while len(leaderboard) != 0:    #while Leaderboard is non-empty
        leaderboard = expand(leaderboard, newSpectrumList)  # Leaderboard ← Expand(Leaderboard)
        for peptide in leaderboard: #for each Peptide in Leaderboard
            if sum(peptide) == spectrum[-1]:    #if Mass(Peptide) = ParentMass(Spectrum)
                if score(peptide, spectrum) > score(leaderPeptide, spectrum):  #if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                    leaderPeptide = peptide    #LeaderPeptide ← Peptide
            elif sum(peptide) > spectrum[-1]:   #else if Mass(Peptide) > ParentMass(Spectrum)
                leaderboard = remove(leaderboard, peptide)    #remove Peptide from Leaderboard
        leaderboard = cut(leaderboard, spectrum, N) #Leaderboard ← Cut(Leaderboard, Spectrum, N)
    if len(leaderPeptide) == 0:
        return "No sequence is found"
    return leaderPeptide   #output LeaderPeptide
