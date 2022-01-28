import random
li=["snake","water","gun"]
i=1
p1count=0
p2count=0
print("Welcome to the Snake Water Gun game")
name=input("Enter your name ")
print("You have total 10 chances.",
      "Enter any word from snake,water,gun")

while(i<=10):
    p1 = random.choice(li)
    p2 = input("Enter your choice ")
    print(f"You have entered {p2}","and",f"Opposite player has entered {p1}")
    if p1=="snake" and p2=="water":
        print("Opposite player wins this round","now",f"{10-i} chance left")
        p1count+=1

    elif p1=="water" and p2=="gun":
        print("Opposite player wins this round","now",f"{10-i} chance left")
        p1count += 1

    elif p1=="gun" and p2=="snake":
        print("Opposite player wins this round","now",f"{10-i} chance left")
        p1count += 1

    elif p1=="snake" and p2=="gun":
        print(f"{name} wins this round","now",f"{10-i} chance left")
        p2count += 1

    elif p1=="gun" and p2=="water":
        print(f"{name} wins this round","now",f"{10-i} chance left")
        p2count += 1

    elif p1 == "water" and p2 == "snake":
        print(f"{name} wins this round","now",f"{10-i} chance left")
        p2count += 1

    else:
        print("Its Tie.You both have entered the same")
    i+=1
if i>10:
    print("\nGame Over!!Hope you have enjoyed now let's see the results")
    if p1count>p2count:
        print(f"{name} wins,score is {p1count} points")
    else:
        print(f"Opposite player wins,score is {p2count} points")
