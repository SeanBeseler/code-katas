
    """Kata 5 : soundex - makes a soundex
        #1 Best Practices Solution by Blind4Basics

        import re

REPLACMENTS  = ["BFPV", "CGJKQSXZ", "DT","L","MN","R"]
ER1, ER2     = "HW", "AEIOUY"

TABLE_ERASE1 = str.maketrans("", "", ER1)
TABLE_NUMS   = str.maketrans( ''.join(REPLACMENTS), ''.join( str(n)*len(elt) for n,elt in enumerate(REPLACMENTS, 1)) )
TABLE_ERASE2 = str.maketrans("", "", ER2)


def formatSoundex(w):
    s = w[0]*(w[0] in ER1+ER2) +  re.sub(r'(\d)\1*', r'\1', w.translate(TABLE_ERASE1).translate(TABLE_NUMS)).translate(TABLE_ERASE2)
    return ((w[0] if s[0].isdigit() else s[0]) + s[1:] + "000")[:4]

    """

def soundex(name):
    return ' '.join(formatSoundex(w.upper()) for w in name.split(" "))
    name = name.split()
    answer = ''
    for x in range(len(name)):
        dig_num = 0
        Ldig = 10
        flag = 0
        for y in range(len(name[x])):
            if(y == 0):
                answer = answer + name[x][y].upper()
            low = name[x][y].lower()
            if(low == 'a' or low == 'e' or low == 'i' or low == 'o' or low == 'u' or low == 'y'):
                Ldig = 10
            elif(low =='b' or low =='f' or low =='p' or low == 'v'):
                if Ldig != 1 and dig_num < 3 and flag != 0:
                    answer = answer +'1'
                    dig_num = dig_num +1
                Ldig = 1
            elif(low =='c' or low =='g' or low =='j' or low == 'k' or low =='q' or low =='s' or low =='x' or low == 'z'):
                if Ldig != 2 and dig_num < 3 and flag != 0:
                    answer = answer +'2'
                    dig_num = dig_num +1
                Ldig = 2
            elif(low =='d' or low =='t'):
                if Ldig != 3 and dig_num < 3 and flag != 0:
                    answer = answer +'3'
                    dig_num = dig_num +1
                Ldig = 3
            elif(low =='l'):
                if Ldig != 4 and dig_num < 3 and flag != 0:
                    answer = answer +'4'
                    dig_num = dig_num +1
                Ldig = 4
            elif(low =='m' or low =='n'):
                if Ldig != 5 and dig_num < 3 and flag != 0:
                    answer = answer +'5'
                    dig_num = dig_num +1
                Ldig = 5
            elif(low =='r'):
                if Ldig != 6 and dig_num < 3 and flag != 0:
                    answer = answer +'6'
                    dig_num = dig_num +1
                Ldig = 6
            flag = 1
        for z in range(3):
            if dig_num < 3:
                answer = answer + '0'
                dig_num = dig_num + 1
        if x < (len(name) - 1):
            answer = answer + ' '
                
            
    return answer
