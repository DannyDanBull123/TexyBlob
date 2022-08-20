#import textblob
from textblob import TextBlob
while True:
  #variable
    a = TextBlob(input("Please enter your sentence here: "))
    a = a.correct()
    print(a)

    b = input("Press Y for if it was correct and N if the correction was wrong : ")
    if b == "y":
        print("I was right!")
        quit()
    elif b == "n":
        c=input("Please enter your phrase again: ")

#variable
