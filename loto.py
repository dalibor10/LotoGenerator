def loto():
    import random
    listOfNumbers= []

    for x in range(6):
        random_number = random.randint(1, 46)
    
        while random_number in listOfNumbers:
            random.randint(1, 46)
        else: 
            listOfNumbers.append(random_number)

    return listOfNUmbers.sort()
