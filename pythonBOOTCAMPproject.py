#program of python to generate string data type using MD5
import hashlib 
# using md5 hash 

result = hashlib.md5(b'chitrankmudgal') 

  
# printing the byte

print("The byte code is : ",result.digest()) 