import random
import binascii 
import hashlib

#a = "ABCD" - Test 
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = a.lower()
c = "1234567890!@#$%^&*"

characters = list(a + b + c)

x = int(input("min: "))
y = int(input("max: "))

z = str(input("NTLM: "))
#z = "EB4FF39B74B0CBCE20A4F62DBD1E3585" - Test 
 

def randstr(length):
	random.shuffle(characters)
	passwd = []
 
	for i in range(length):
		passwd.append(random.choice(characters))

	random.shuffle(passwd)
	return "".join(passwd)


check = True

while(check):
	temp = randstr(random.randrange(x, y+1))
	print(temp)
	#temp = "abcd" - Test 
	ntlm = binascii.hexlify(hashlib.new('md4', temp.encode('utf-16le')).digest())
	print(ntlm)
	#print("b'"+z.lower()+"'") - Test 

	if(str(ntlm.lower()) == ( "b'"+z.lower()+"'")):
		check = False
		print("\n\n\n====================END====================")
		print("NTLM:",ntlm, ); print("Passwd:",str(temp),"\n")
		
    
    
    

    
