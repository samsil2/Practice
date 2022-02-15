def freuentWord(lst):
    counter = 0
    word = lst[0]

    for i in lst:
        curr_frequency = lst.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            word = i

    print("Most frequent word is: {0} and frequency: {1}".format(word, counter))

#main driver
if __name__=="__main__":
    str = input("Enter some Words: ")
    words = str.split()
    freuentWord(words)
