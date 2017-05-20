""" 5 kyu #9 Matrices: Adding diagonal products

my function passed the test but it keep and giving me an error div by zero, Nick said to just sumbmit it

"""
def get_ur_top(matrix, h , w):
    sum = 0
    for p in range(w):
        tsum =1
        x =0
        y = p
        ex = True
        while ex:
            temp = matrix[x][y]
            x = x + 1
            y = y + 1
            if x >= w or y >= h:
                ex = False
            tsum = tsum * temp
        sum = sum + tsum
    return sum
    
def get_ur_side(matrix, h , w):
    sum = 0
    for p in range(1,w):
        tsum =1
        x =p
        y = 0
        ex = True
        while ex:
            temp = matrix[x][y]
            x = x + 1
            y = y + 1
            if x >= w or y >= h:
                ex = False
            tsum = tsum * temp
        sum = sum + tsum
    return sum
    
def get_ul_top(matrix, h , w):
    sum = 0
    for p in range(w):
        tsum =1
        x =0
        y = p
        ex = True
        while ex:
            temp = matrix[x][y]
            x = x + 1
            y = y - 1
            if x >= h or y < 0:
                ex = False
            tsum = tsum * temp
        sum = sum + tsum
    return sum
    
def get_ul_side(matrix, h , w):
    sum = 0
    for p in range(1,w):
        tsum =1
        x =p
        y = 4
        ex = True
        while ex:
            temp = matrix[x][y]
            x = x + 1
            y = y - 1
            if x >= w or y < 0:
                ex = False
            tsum = tsum * temp
        sum = sum + tsum
    return sum
                
def sum_prod_diags(matrix):
    # your code here
    h = len(matrix)
    w = len(matrix[0])
    sum1 =get_ur_top(matrix, h, w)
    sum2 = get_ul_top(matrix, h, w)
    sum1 = sum1 + get_ur_side(matrix,h,w)
    sum2 = sum2 + get_ul_side(matrix,h,w)
    total = sum1 - sum2
    print(total)
    return total
    
M1 = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]
sum_prod_diags(M1)
