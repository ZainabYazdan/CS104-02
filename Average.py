Total=0
ScoreCount=0
Average=0

NumberOfScores=int(input("Please enter the number of scores to be averaged:"))

while ScoreCount<NumberOfScores:
    ScoreCount=ScoreCount+1
    Score=int(input("Please enter the score:"))
    Total=Total+Score


Average=Total/NumberOfScores
print("Your requested average is ", Average)
print("Have a good day!")
