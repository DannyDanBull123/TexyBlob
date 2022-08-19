#import textblob
from textblob import TextBlob

#variable
a = TextBlob(input("Please enter your word here : "))
a = a.correct()

print(a)
