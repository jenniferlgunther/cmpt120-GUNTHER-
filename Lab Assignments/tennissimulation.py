#Jennifer Gunther
#Introduction to Programming
#27 April 2018

from simstats import SimStats
from tennismatch import RBallGame

def printIntro():
    print("This program simulates a racquetball series of games")

def getInputs():
    probA = float(input("Enter the probability of A: "))
    probB = float(input("Enter the probability of B: "))
    n = int(input("Number of games to simulate: "))
    return probA, probB, n
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        stats.update(theGame)
    stats.printReport()

main()
