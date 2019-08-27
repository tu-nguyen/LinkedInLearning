#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # i = game.index("Paper")
    # print(game[i])
    # game.append("Computer") # appends to end of list 
    # game.insert(0, "Computer") # insert at index 0
    # game.remove("Paper") # removes item by value
    # game.pop() # pop last item and returns it
    # del game[3] # removes by index [1:3] by slice as well
    # print(", ".join(game)) # prints each with a ", "
    # print(len(game)) # function that returns length
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
