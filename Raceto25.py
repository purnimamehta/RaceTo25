__author__ = 'purnimamehta'

def a():
    '''
    Write a while loop that counts from 0 to 10, inclusive.
    Print out each number.
    :return: None
    '''
    i = 0
    while i <= 10:
        print(i)
        i += 1

def b1(n):
    '''
    Count from 0 to n inclusive. Print out each number.
    Use a while loop.
    :param n: an integer
    :return: None
    '''
    i = 0
    while (i <= n):
        print(i)
        i += 1

def b2(n):
    '''
    Count from 0 to n inclusive. Print out each number.
    Use a for loop.
    :param n: an integer
    :return: None
    '''
    for i in range(n + 1):
        print(i)

def get_input():
    '''
    Continually prompt the user for a number, 1,2 or 3 until
    the user provides a good input. You will need a type conversion.
    :return: The users chosen number as an integer
    '''
    while True:
        number = input("Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            return (number)
        else:
            print("Invalid input!")

def c():
    '''
    Write a few lines of code which does the following.
    Ask the user to input a 1,2 or 3.
    If the user enters anything else, then tell the user
    they did something wrong, and prompt them again for a good input.
    Hint: use get_input()
    Hint: use another function above.
    Once the user enters the number, counts from 0 to the number and then returns.
    :return: None
    '''

    while True:
        number = input("Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            number = int(number)
            i = 0
            while i <= number:
                for i in range(0, number + 1):
                    print(i)
                    i += 1
            return (number)
        else:
            print("Invalid input!")
    return

def d():
    '''
    Write a few lines of code which does the following...
    Same as in c(), but this time, keep track of the total
    of all numbers (1,2,3) input so far. Exit when the total
    is 25 or more. You don't actually have to count to the input
    number, just add it.
    :return: None
    '''

    total = 0
    print("Total is " + str(total))
    while total < 25:
        while True:
            number = input("Give me one of 1,2 or 3: ")
            if ((number == "1") or (number == "2") or (number == "3")):
                number = int(number)
                total = total + number
                print("Total is", str(total))

            else:
                print("Invalid input!")
    return

def e():
    '''
    Same as in d(), but this time, make sure that the user can't enter
    a number that would put the total over 25.
    :return: None
    '''

    total = 0
    print("Total is " + str(total))
    while total < 25:
        number = input("Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            number = int(number)
            if (total + number) > 25:
                print("The number you chose would put the total over 25. Try Again.")
            else:
                total = total + number
                print("Total is", str(total))
        else:
            print("Invalid input!")
    return

def get_input_from_player(player):
    '''
    This is the same as get_input, except this time, the prompt includes which player
    is supposed to supply the input.
    :param player: The player, either 1 or 2
    :return: An integer, either 1,2 or 3
    '''

    while True:
        number = input("Player " + str(player) + " Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            return (number)
        else:
            print("Invalid input!")
    return

def f():
    '''
    Same as in e(), but ths time, print out which players move it is,
    on each turn. There are 2 players, Player 1 starts and they alternate.
    Hint: add a player variable, as well as use get_input_from_player(player)
    :return: None
    '''

    total = 0
    print("Total is " + str(total))
    player = 1
    while total < 25:
        number = input("Player " + str(player) + " Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            number = int(number)
            if (total + number) > 25:
                print("The number you chose would put the total over 25. Try Again.")
            else:
                total = total + number
                print("Total is", str(total))
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
        else:
            print("Invalid input!")
    return

def raceTo25():
    '''
    Same as in f(), but this time, print out which player won, before returning.
    :return: None
    '''

    total = 0
    print("Total is " + str(total))
    player = 1
    while total < 25:
        number = input("Player " + str(player) + " Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            number = int(number)
            if (total + number) > 25:
                print("The number you chose would put the total over 25. Try Again.")
                print("Total is " + str(total) + "!")
            elif (total + number) == 25:
                print("Total is 25")
                print ("Player "+ str(player) +" won!!")
                break
            else:
                total = total + number
                print("Total is", str(total))
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
        else:
            print("Invalid input!")
    return

def raceTo(m):
    '''
    Same as in raceTo(), but this time the race to the defined m value.
    :param m:
    :return: None
    '''

    total = 0
    print("Total is " + str(total))
    player = 1
    while total < m:
        number = input("Player " + str(player) + " Give me one of 1,2 or 3: ")
        if ((number == "1") or (number == "2") or (number == "3")):
            number = int(number)
            if (total + number) > m:
                print("The number you chose would put the total over " + str(m) + ". Try Again.")
                print("Total is " + str(total) + "!")
            elif (total + number) == m:
                print("Total is " + str(m) + "!")
                print ("Player "+ str(player) +" won!!")
                break
            else:
                total = total + number
                print("Total is", str(total))
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
        else:
            print("Invalid input!")
    return



# Remove the # in front of the function below to actually call it
# a()
# b1(0)
# b1(-5)
# b1(15)
# b2(0)
# b2(-5)
# b2(15)
# get_input()
# c()
# d()
# e()
# get_input_from_player(1)
# get_input_from_player(2)
# f()
# raceTo25()
# raceTo(25)
# raceTo(17)
# raceTo(100)