import string

dna = "ATTGC"

def dna_strand(dna):

    return dna.translate(string.maketrans("ATCG","TAGC"))

