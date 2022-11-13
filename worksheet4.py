""" 
thCount = 0
2 word = input("Word: ")
3 if word == 'the':
4     the_Count = the_Count + 1

5 elif word == 'The':
6     the_Count = the_Count + 1

7 print( "Total count %s" % (theCount) )
"""

words = ["outside","today", "weather", "raining", "nice", "rain","snow", "day", "winter", "cold"]
totalcount = 0
word = 0
while word != "exit":
    
    word = input("word: ")
    if word in words:
        totalcount = totalcount + 1

    else: break
    if word not in words:
        x = list("")

