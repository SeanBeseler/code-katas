""" Kyu 6 Matrices: Process for a Square Matrix Best Practices by Smile67

def avg_diags(m):
  a1,a2,l,l1,l2=0,0,len(m),0,0
  for i in range (0,l):
    if i&1: 
       if m[i][i]>=0: a1+=m[i][i]; l1+=1
    else:
       if m[l-i-1][i]<0: a2+=m[len(m)-i-1][i]; l2+=1
  return [round(a1/l1) if l1>0 else -1,round(abs(a2)/l2) if l2>0 else -1]

  """
import math
def pidg(m):
	y = 0
	x = 0
	res = []
	h = len(m)
	for z in range(h):
		res.append(m[x][y])
		x = x + 1
		y = y + 1
	return(res)
    
def sidg(m):
	h = len(m)
	x = 0
	y = h -1
	res = []
	for z in range(h):
		res.append(m[x][y])
		x = x +1
		y = y -1
	return(res)
def getave(a , n):
	if a == False:
		return []
	print(a)
	answer = 0
	count = 0
	for x in range(len(a)):
		if x % 2 == n and a[x] >= 0 and n == 1:
			answer = answer + a[x]
			count = count + 1
		elif x % 2 == n and a[x] < 0 and n == 0:
			a[x] = a[x] * -1
			answer = answer + a[x]
			count = count + 1
	answer = math.ceil(answer/ count)
	return answer
    
def avg_diags(m):
	s = pidg(m)
	an = []
	c = sidg(m)
	an.append(getave(s,1))
	an.append(getave(c,0))
	return an
