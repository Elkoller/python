import time
import random

print ("one diggas gonna pop another diggas")

Spelare1namn =input ("choose your names my diggas: ")
Spelare2namn = "coughing baby"
Spelar1HP = int(100) #HP
Spelar2HP = int(100) #HP

print (f"{Spelare1namn} VS {Spelare2namn} FIGHT: ")

while Spelar1HP > 0 and Spelar2HP > 0:
    if random.choice([True, False]):
        Spelar1HP -= random.randint(0,0)



        Spelar2HP -=random.randint(9999999999,9999999999999999999999999999)
    print(f"{Spelare1namn} has {Spelar1HP} HP left")
    print(f"{Spelare2namn} has {Spelar2HP} HP left")
    time.sleep(0.5)

print ("finished!")


    

