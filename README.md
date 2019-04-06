# N-Queens-Problem-Using-Hill-Climbing-Search

Implemented N-queens problem by using hill-climbing search and its variants 

● Steepest- ascent hill climbing

● Hill-climbing with sideways move

● Random-restart hill-climbing with and without sideways move

**Program Structure:**
The code implements a heuristics function to calculate the number of pairs of queens that are attacking to each other. Another implemented function returns the possible moves that has less number of violations.

Following is the program structure.

*1. Global Variables -*
The variables named n is used which is the number of queens.
*2. Functions & Procedures -*
calculateHeuristics() : Function to calculate the number of pairs of queens that are attacking to each other

calculateMinBoard(): Function to calculate the possible moves that has less number of violations

printState() : Function to print a state in NXN board form

hill_climbing() : Function that takes board as input and returns solution using steepest ascent hill climbing

hill_climbing_with_sideways() : Function that takes board as input and returns solution using hill climbing with sideways move

hill_climbing_random_restart() : Function that takes board as input and returns solution using random restart hill climbing search without sideways move

random_restart_hill_climbing_with_sideways() : Function that takes board as input and returns solution using using random restart hill climbing search with sideways move
