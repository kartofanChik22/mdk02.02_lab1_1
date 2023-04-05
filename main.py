print("Hello world from vs code")
import random
string=""
for i in range(1,11):
    if i%2!=0:
        string+=chr(random.randint(97,122))
    else:
        if i<10:
            string+=str(i)
        else:
            string+=str(i-8)
print(string)