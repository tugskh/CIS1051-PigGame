#Tugsbileg Khaliunbat
#CIS 1051

import random

def holdAt20(holdValue):
    turnTotal = 0
    while turnTotal<=holdValue:
        roll = random.randrange(1,6)
        #print("Roll:", roll)
        if roll == 1:
            turnTotal=0
            break
        else:
            turnTotal+=roll
    #print("Turn total:",turnTotal)
    return turnTotal


def holdAt20Outcomes():
    num = int(input("How many Hold-at-20 turn simulations?\n"))
    print("Score","Estimated Probability", sep="\t")
    stats = {}
    for _ in range(num):
        score = holdAt20(20)
        if score not in stats:
            stats[score] = 1
        else:
            stats[score]+=1
    percentages = {}
    for score in stats.keys():
        percentages[score] = stats[score]/num
    for per in sorted(percentages.keys()):
        print(per, percentages[per], sep="\t")


def holdAtXOutcomes():
    holdValue = int(input("What is the hold value?\n"))
    num = int(input("How many turn simulations?\n"))
    print("Score","Estimated Probability", sep="\t")
    stats = {}
    for _ in range(num):
        score = holdAt20(holdValue)
        if score not in stats:
            stats[score] = 1
        else:
            stats[score]+=1
    percentages = {}
    for score in stats.keys():
        percentages[score] = stats[score]/num
    for per in sorted(percentages.keys()):
        print(per, percentages[per], sep="\t")


def holdAt20orGoalTurn():
    score = int(input("Score?\n"))
    turnTotal = 0
    newScore = 0
    while newScore<=100 and turnTotal<=20:
        roll = random.randrange(1,6)
        print("Roll:", roll)
        if roll!=1:
            turnTotal+=roll
            newScore = score + turnTotal
        else:
            turnTotal=0
            print("Turn total:",turnTotal)
            newScore = score + turnTotal
            print("New score:",newScore)
            return newScore
    print("Turn total:",turnTotal)
    print("New score:",newScore)
    return newScore



def holdAt20orGoalGame():
    newScore = 0
    turnCount = 0
    while newScore<=100:
        turnTotal = holdAt20(20)
        newScore+= turnTotal
        turnCount +=1
        print("New score:",newScore)
    #return turnCount
    return newScore
          

def AveragePigTurns():
    num = int(input("Games?\n"))
    turnCountSum = 0
    for _ in range(num):
        turnCount = holdAt20orGoalGame()
        turnCountSum += turnCount
    avg = turnCountSum/num
    print("Average turns:",avg)


def twoPlayerPig():
    p1Score = 0
    p2Score = 0
    print("Player 1 score:", p1Score)
    print("Player 2 score:", p2Score)
    print()
    while p1Score<100 and p2Score<100:
        for i in range(1,3):
            newScore1 = 0
            newScore2 = 0
            print("It is player",i,"\'s","turn")
            turnTotal = holdAt20(20)
            if i==1:
                newScore1+=turnTotal
                p1Score+=newScore1
                print("New score:",p1Score)
            if i==2:
                newScore2+=turnTotal
                p2Score+=newScore2
                print("New score:",p2Score)
            print()
            print("Player 1 score:", p1Score)
            print("Player 2 score:", p2Score)
            print()


def PigGame():
    print("You will be player 2.")
    print("Enter nothing to roll; enter anything to hold")
    p1Score = 0
    p2Score = 0
    print()
    print("Player 1 score:", p1Score)
    print("Player 2 score:", p2Score)
    print()
    while p1Score<100 and p2Score<100:
        for i in range(1,3):
            newScore1 = 0
            newScore2 = 0
            turnTotal = 0
            print("It is player",i,"\'s","turn")
            if i==1:
                turnTotal = holdAt20(20)
                newScore1+=turnTotal
                p1Score+=newScore1
                print("New score:",p1Score)
            if i==2:
                inp=""
                while inp=="":
                    roll = random.randrange(1,6)
                    print("Roll:", roll)
                    if roll == 1:
                        turnTotal=0
                        print("Turn total:", turnTotal)
                        break
                    else:
                        turnTotal+=roll
                        print("Turn total:", turnTotal)
                    inp = input("Roll/Hold?  (Enter) ")
                newScore2+=turnTotal
                p2Score+=newScore2
                print("New score:",p2Score)
            print()
            print("Player 1 score:", p1Score)
            print("Player 2 score:", p2Score)
            print()
    


PigGame()
#holdAtXOutcomes()
