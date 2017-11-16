'''This program works like the Engima machine. It utilized the Ceaser 
encryption method along with a few advanced tweaks that make sure that 
the encrypted message is not easy to crack
To us this:
          1) To encrypt a message: >python3 encrypter.py -e
				then enter an integer key followed by a message
		  2) To decrypt a message: >python3 encrypter.py -d
				then enter the integer key followed by the encrypted message	'''
import argparse

simplealphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
complexalphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,><-_=+)(&*^%$#@!`/\ 1234567890"
alphabet=complexalphabet
length=len(alphabet)-1
def get_index(a):
	i=0
	while(i<(length+1)):
		x=alphabet[i]
		if(x==a):
			return(i)
			break
		else:
			i=i+1
			
def convertmessage(k,m,f):
	mess=str(m)
	result=""
	l=1
	for j in mess:
		oldindex=get_index(j)
		newindex=(oldindex + (f*l*funct(k)))%length                 #modulo ensures index value remains between 0 and 36. the 'l' increment ensures that no character has the same encoded value twice.
		result=result+alphabet[newindex]
		l=l+1
	return(result)
	
def funct(h):                                          #this function generates a hashed key
	n=int((h*h)/(3.14))
	return(n)
	

p=argparse.ArgumentParser()
g=p.add_mutually_exclusive_group()
g.add_argument("-e","--encrypt",help="Add the -e to encrypt a message",action="store_true")
g.add_argument("-d","--decrypt",help="Add the -d to decrypt a message",action="store_true")
argopt=p.parse_args()

if(argopt.encrypt):
	key=int(input("Enter key: "))
	message=str(input("Enter message to be encrypted: "))
	print(convertmessage(key,message,(1)))
	
elif(argopt.decrypt):
	key=int(input("Enter key: "))
	message=str(input("Enter message to be encrypted: "))
	print(convertmessage(key,message,(-1)))
