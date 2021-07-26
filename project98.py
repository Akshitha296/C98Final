def swapFileData():
    #input file names
    fileOne = input("File #1: ")
    fileTwo = input("File #2: ")


    #reading+saving
    with open(fileOne, 'r') as a:
        data_a = a.read()
    
    with open(fileTwo, 'r') as b:
        data_b = b.read()


    #writing
    with open(fileOne, 'w+') as a:
        a.write(data_b)
    
    with open(fileTwo, 'w+') as b:
        b.write(data_a)

    #printing "finished" message
    print("Data swapped successfully!")

swapFileData()