'''
CISC 471 HW1
'''

#Question 1.1 Frequent k-mer
def frequent_k_mer(text, k):
    i = 0
    kmers = {}

    #Obtain seqences
    while i <= len(text) - k:
        seq = text[i:(i+k)]

        #If the sequence has not been checked
        if not seq in kmers:
            newCount = text.count(seq)
            kmers[seq] = newCount
        i += 1
    maxVal = max(kmers.values())

    #When the seqence showed up more than once
    if maxVal > 1:
        maxKmers = []
        for k,v in kmers.items():
            if v == maxVal:
                maxKmers.append(k)
        print(maxKmers)

    #When all seqneces showed up only once -- no frequent k-mer
    else:
        print("No frequent k-mer is found")


#Question 1.2 Frequent k-mer with mismatches
def frequent_k_mer_mismatches(text, k, d):
    i = 0
    kmers = {}

    #Obtain seqences
    while i <= len(text) - k:
        seq = text[i:(i+k)]

        #If the sequence has not been checked
        if not seq in kmers:
            j = 0

            #Check if the text contains the sequence
            while j <= len(text) - k:
                misCount = 0

                #Compare each element of sequence with the substring of the text
                for a in range(len(seq)):
                    if text[j+a] != seq[a]:
                        misCount += 1

                #If the number of mismatch element is smaller than the requirement
                if misCount <= d:
                    if seq in kmers:
                        kmers[seq] += 1 #Update the frequency of the sequence in the kmers dictionary if the sequence has appeared
                    else:
                        kmers[seq] = 1  #Add the sequence to the kmers dictionary
                j += 1
        i += 1
    maxVal = max(kmers.values())

    #When the seqence showed up more than once
    if maxVal > 1:
        maxKmers = []
        for k,v in kmers.items():
            if v == maxVal:
                maxKmers.append(k)
        print(maxKmers)

    #When all seqneces showed up only once -- no frequent k-mer
    else:
        print("No frequent k-mer is found")

#Question 1.3 Unit tests
#Test frequent k-mer
def test_k_mer_positive():
    print("test k-mer positive")
    frequent_k_mer("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)

def test_k_mer_negative():
    print("test k-mer negative")
    frequent_k_mer("ACGGTGCCTGTCGCATGATGCGTGAGAGCT", 4)

#Test frequent k-mer with mismatches
def test_k_mer_mismatches_positive():
    print("test k-mer mismatches positive")
    frequent_k_mer_mismatches("ACTATGCATACTATCGGGAACT", 5, 1)

def test_k_mer_mismatches_negative():
    print("test k-mer mismatches negative")
    frequent_k_mer_mismatches("AGTTTGCATACTATCGGGAACT", 5, 1)

def main():
    test_k_mer_positive()
    test_k_mer_negative()
    test_k_mer_mismatches_positive()
    test_k_mer_mismatches_negative()

main()
