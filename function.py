def countWords ():
    fileName=input("enter file name: ")
    numberOfWords=0
    file=open(fileName,'r')
   
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("number of words in the file =")
    print(numberOfWords)

countWords()





