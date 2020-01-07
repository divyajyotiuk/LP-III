subNib = [
['9','4','A','B'],
['D',"1",'8','5'],
['6','2','0','3'],
['C','E','F',"7"]
]
const1 = [1,0,0,0,0,0,0,0]
const2 = [0,0,1,1,0,0,0,0]
pTxt = list(map(int,input("Enter 16bit plaintxt \n")))
key = list(map(int,input("Enter 16bit key \n")))

w0 = key[0:8]
w1 = key[8:16]

print(w0,w1)

#init round
#key1 = [w2,w3]

def rotateNib(w):
	return w[4:8]+w[0:4]

def sboxNib(w):
	res=[]
	for i in range(int(len(w)/2)):
		if(i%2==0):
			row = w[i*2]*2 + w[i*2+1]
			col = w[i*2+2]*2 + w[i*2+3]
			res1 = "{0:04b}".format(int(subNib[row][col], 16))
			res = res + list(map(int,res1))
	return res

def xor(wn1,wn2,const):
	wn2 = rotateNib(wn2)
	wn2 = sboxNib(wn2)
	res=[]
	for i in range(8):
		res.append(wn1[i]^const[i])
		res[i] = res[i]^wn2[i]
	return res

def xoring(wn1,wn2):
	res=[]
	for i in range(len(wn1)):
		res.append(wn1[i]^wn2[i])
	return res
w2 = xor(w0,w1,const1)
w3 = xoring(w2,w1)

key1 = w2 + w3 
print("Key1:")
print(key1)

w4 = xor(w2,w3,const2)
w5 = xoring(w4,w3)

key2 = w4 + w5
print("Key2:")
print(key2)

#round0 pTxt xor key
out0 = xoring(pTxt,key)
print("Round0 o/p: ",out0)

#round 1
#step1 - out0 to sbox 

