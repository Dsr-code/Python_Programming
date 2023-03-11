questions=["National Flower of India ","National Bird of India","RastryaGaan stands for how many seconds", "what is the capital of India"]
# questions=questions.reverse()

answers=["lotus","peacock","52","delhi"]
# answers=answers.reverse()

# points=0
# rupees=[]
# rupees.append(points)
name=input("Enter your Name:\n")

# prize=0
# prize=points*1000

collection=0

for i in range(len(questions)):
    print("\n")
    # points=points+i
    # collection=[]
    # print(points)
    # print(rupees)
    # collection.append(prize)
    print(questions[i])
    a=input("")
    if a == answers[i]:
        print("congratulations \n")
        collection=collection+(i+1)
        sum=collection*1000
        print("You played wonderfull",name.capitalize(),"\nYou won",sum,"rupees!!!")
    else:
        print("better luck next time")
        # sum=0
        
        sum=collection*1000
        print("you won",sum,"rupees !!!" )

        break