'''
CISC 471 HW4
Part1.1 RNA Translate to Amino Acids
'''

from textwrap import wrap

def rnaToAA(Rna):
    Rna = Rna.upper()
    #Check if the RNA string only has A, U, C, and/or G
    for i in Rna:
        if i not in "AUCG":
            return "The RNA string contains invalid characters"
    #Split the RNA string to a list that each element contains three characters
    splitRna = wrap(Rna, 3)
    AA = []
    for codon in splitRna:
        #Check if the length of the codon is three
        if len(codon) != 3:
             break
        if codon[0] == "U":     #The first base is U
            if codon[1] == "U":     #The second base is U
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("F")
                else:   #The third base is A or G
                    AA.append("L")
            elif codon[1] == "C":   #The second base is C
                AA.append("S")
            elif codon[1] == "A":   #The second base is A
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("Y")
                else:   #The third base is A or G
                    AA.append("")   #Stop codon
            else:   #The second base is G
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("C")
                elif codon[2] == "A":   #The third base is A
                    AA.append("")   #Stop codon
                else:   #The third base is G
                    AA.append("W")
        elif codon[0] == "C":   #The first base is C
            if codon[1] == "U":     #The second base is U
                AA.append("L")
            elif codon[1] == "C":   #The second base is C
                AA.append("P")
            elif codon[1] == "A":   #The secodn base is A
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("H")
                else:   #The third base is A or G
                    AA.append("Q")
            else:   #The second base is G
                AA.append("R")
        elif codon[0] == "A":   #The first base is A
            if codon[1] == "U":     #The second base is U
                if codon[2] == "G":     #The third base is G
                    AA.append("M")
                else:   #The third base is U, C, or A
                    AA.append("I")
            elif codon[1] == "C":   #The second base is C
                AA.append("T")
            elif codon[1] == "A":   #The second base is A
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("N")
                else:   #The third base is A or G
                    AA.append("K")
            else:   #The second base is G
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("S")
                else:   #The third base is A or G
                    AA.append("R")
        else:   #The first base is G
            if codon[1] == "U":     #The second base is U
                AA.append("V")
            elif codon[1] == "C":   #The second base is C
                AA.append("A")
            elif codon[1] == "A":   #The second base is A
                if codon[2] == "U" or codon[2] == "C":  #The third base is U or C
                    AA.append("D")
                else:   #The third base is A or G
                    AA.append("E")
            else:   #The second base is G
                AA.append("G")
    strAA = "".join(AA)
    return strAA
