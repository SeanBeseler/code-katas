""" 7 kyu complementary DNA

best practices by JustyFY,ChingChangChong,pompeu2004

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))


    """


def DNA_strand(dna):
	print(dna)
	RNA = ''
	for x in dna:
		if x == 'A':
			RNA = RNA + 'T'
		elif x == 'T':
			RNA = RNA + 'A'
		elif x == 'G':
			RNA = RNA  + 'C'
		elif x == 'C':
			RNA = RNA  + 'G'
  	return RNA
