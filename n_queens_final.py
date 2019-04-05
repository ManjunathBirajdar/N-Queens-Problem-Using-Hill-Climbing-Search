import copy
from random import randrange
import random

class board():
    def __init__(self, n):
        self.n = n
        self.board= [[0 for i in range (0,self.n)] for j in range (0,self.n)]
        for i in range(0, n):
            while 1:
                rand_row = random.randint(0,n-1)
                rand_col = i
                #place each queen in separate column
                if self.board[rand_row][rand_col] == 0:
                    self.board[rand_row][rand_col] = 'Q'
                    break

#Function to print a state in NXN board
def printState(state):
        for i in range(n):
            result = ""
            for j in range(n):
                result += str(state[i][j])+" "
            print(result)
        print("")
        
def calculateHeuristics(tboard,n):
    cost = 0
    for i in range(0,n):
        for j in range(0,n):
            if tboard.board[i][j]=='Q':
                for k in range(j+1,n): #check row
                    if tboard.board[i][k] == 'Q' :
                        cost+=1
                #check diagonals
                i1,j1=i+1,j+1
                while (i1<n and j1<n):
                    if tboard.board[i1][j1] == 'Q':
                        cost+=1
                    i1+=1
                    j1+=1
                i1,j1=i-1,j+1
                while (i1>=0 and j1<n):
                    if tboard.board[i1][j1] == 'Q':
                        cost+=1
                    i1-=1
                    j1+=1                
    return cost

def calculateMinBoard(tboard,n):
    list1 = []
    minCost=calculateHeuristics(tboard,n)
    for i in range(0,n):
        for j in range(0,n):
            if tboard.board[j][i]=='Q':
                for i1 in range(0,n):
                        #try different combinations by moving a queen in the same column
                        if tboard.board[i1][i]!='Q' :
                            newBoard = copy.deepcopy(tboard)
                            newBoard.board[j][i]=0
                            newBoard.board[i1][i]='Q'
                            cost=calculateHeuristics(newBoard, n)
                            if cost < minCost:
                                list1.clear()
                                minCost = cost
                                list1.append([i1,i])
                            elif cost == minCost:
                                list1.append([i1,i])
    
    return list1,minCost

# Function for steepest-ascent hill climbing
def hill_climbing(board,iterationCount):
    steps=0
    val = calculateHeuristics(board,n)
    if (iterationCount < 4):
        print('The search sequence for random configuration: ', iterationCount + 1)
        stepCnt = 0
    while 1:
        if (iterationCount < 4):
            printState(board.board)
            stepCnt += 1
        if val == 0:
            break
        else:
            steps += 1
            list1,cost = calculateMinBoard(board,n)
            if val <= cost or len(list1) == 0:
                break
            else:
                random_index = randrange(0,len(list1))                           
                index = list1[random_index]
                val = cost
                for i in range (0,n):
                        board.board[i][index[1]]=0
                board.board[index[0]][index[1]]='Q'

    if (iterationCount < 4):
        if val == 0:    #print whether success or failure
            print("Success")
        else:
            print("Failure")
        print('Number of Steps: ',stepCnt-1)
        print('----------------')
    if val == 0:
        return 1, steps
    return 0, steps

# Function for hill climbing with sideways move
def hill_climbing_with_sideways(tboard, iterationCount):
    steps = 0
    sideWayCount=0
    b = tboard
    presentCost = calculateHeuristics(b, n)
    if (iterationCount < 4):
        print('The search sequence for random configuration: ', iterationCount + 1)
        stepCnt = 0
    while steps<100:
        if (iterationCount < 4):
            printState(b.board)
            stepCnt += 1
        if presentCost == 0:
            break
        else:
            steps += 1
            list1, cost = calculateMinBoard(b, n)
            if presentCost < cost:
                break
            if len(list1) == 0:
                break
            else:
                if presentCost == cost:
                    sideWayCount+=1
                else:
                    sideWayCount=0
                random_index = randrange(0, len(list1))
                index = list1[random_index]
                presentCost = cost
                for i in range(0, n):
                    b.board[i][index[1]] = 0
                b.board[index[0]][index[1]] = 'Q'

    if (iterationCount < 4):
        if presentCost == 0:    #print whether success or failure
            print("Success")
        else:
            print("Failure")
        print('Number of Steps: ',stepCnt-1)
        print('----------------')
    if presentCost == 0:
        return 0, steps
    return 1, steps

# Function for hill climbing using random restart without sideways
def hill_climbing_random_restart(tboard):
     
    restart_count=0
    steps=0
    b= tboard
    hprev = calculateHeuristics(b, n)
    while 1:
        if hprev == 0:
            break
        else:
            steps += 1
            list1,h = calculateMinBoard(b,n)
            if hprev <= h or len(list1) == 0:
                restart_count += 1
                b = board(n)
                hprev = calculateHeuristics(b, n)
                continue 

            random_index = randrange(0,len(list1))                            
            index = list1[random_index]
            hprev = h
            for i in range (0,n):
                    b.board[i][index[1]]=0
            b.board[index[0]][index[1]]='Q'
    
    if hprev == 0:
        return 0, steps, restart_count
    return 1, steps, restart_count

# Function for hill climbing using random restart with sideways
def random_restart_hill_climbing_with_sideways(tboard):
    steps = 0
    sideWayCount=0
    restart_count = 0
    b = tboard
    hprev = calculateHeuristics(b, n)
    while 1:
        if hprev == 0:
            break
        else:
            steps += 1
            list1, h = calculateMinBoard(b, n)
            if hprev < h or len(list1) == 0:
                b=board(n)
                hprev = calculateHeuristics(b, n)
                restart_count += 1
                sideWayCount=0
                continue
            
            if hprev == h:
                sideWayCount+=1
                if steps >= 100:
                    b=board(n)
                    hprev = calculateHeuristics(b, n)
                    restart_count += 1
                    sideWayCount=0
            else:
                sideWayCount=0

            random_index = randrange(0, len(list1))
            index = list1[random_index]
            hprev = h
            for i in range(0, n):
                b.board[i][index[1]] = 0
            b.board[index[0]][index[1]] = 'Q'

    if hprev == 0:
        return 0, steps, restart_count
    return 1, steps, restart_count

#main function driving Hill climbing algorithm for n-queens problem
def main():
    global n
    
    success_steps = 0
    failure_steps = 0
    success_count = 0
    failure_count = 0
    try: 
        n = int(input("Enter the value of n: "))
        print("*** Steepest-ascent Hill Climbing ***") 
        print("Executing...")    
        for i in range(0,500):
            b = board(n)  
            val,steps = hill_climbing(b,i)
            if val == 0:
                failure_count +=1
                failure_steps += steps
            else:
                success_count +=1
                success_steps += steps
           
        success_rate=(success_count/(success_count+failure_count))*100
        failure_rate=(failure_count/(success_count+failure_count))*100
        print("Success rate is: ",round(success_rate,2),"% and Failure rate is: ",round(failure_rate,2),"%")
        if success_count != 0:
            print("The average number of steps when the algorithm succeeds: ", round(success_steps / success_count, 2))
        if failure_count != 0:
            print("The average number of steps when the algorithm fails: ", round(failure_steps / failure_count, 2))
 
        print("*** Hill-climbing search with sideways move ***")
        print("Executing...")
        success_steps = 0
        failure_steps = 0
        success_count = 0
        failure_count = 0
        for i in range(0, 500):
            b = board(n)
            val, steps = hill_climbing_with_sideways(b,i)
            if val == 1:
                failure_count += 1
                failure_steps += steps
            else:
                success_count += 1
                success_steps += steps
        success_rate = (success_count / (success_count + failure_count)) * 100
        failure_rate = (failure_count / (success_count + failure_count)) * 100
        print("Success rate is: ", round(success_rate,2), "% and Failure rate is: ", round(failure_rate,2), "%")
        if success_count!=0:
            print("The average number of steps when the algorithm succeeds: ", round(success_steps / success_count,2))
        if failure_count!=0:
            print("The average number of steps when the algorithm fails: ", round(failure_steps / failure_count,2))
  
        print("*** Random-restart hill-climbing search without sideways move ***")
        print("Executing...")
        success_steps = 0
        failure_steps = 0
        success_count = 0
        failure_count = 0
        total_restart_count = 0
        for i in range(0,100):
            b = board(n)  
            val, steps, restartCount = hill_climbing_random_restart(b)
            if val == 1:
                failure_count +=1
                failure_steps += steps
            else:
                success_count +=1
                success_steps += steps
            total_restart_count += restartCount
        print("The average number of random restarts required without sideways move", total_restart_count/(success_count+failure_count))
        print("The average number of steps required without sideways move", success_steps/(success_count+failure_count))
   
        print("*** Random-restart hill-climbing search with sideways move ***")
        print("Executing...")
        success_steps = 0
        failure_steps = 0
        success_count = 0
        failure_count = 0
        total_restart_count = 0
        for i in range(0, 100):
            b = board(n)
            val, steps, restartCount = random_restart_hill_climbing_with_sideways(b)
            if val == 1:
                failure_count += 1
                failure_steps += steps
            else:
                success_count += 1
                success_steps += steps
            total_restart_count += restartCount
        print("The average number of random restarts required with sideways move", total_restart_count / (success_count + failure_count))
        print("The average number of steps required with sideways move", success_steps / (success_count + failure_count))


    except ValueError:
        print("Please enter a number as value of n.")
    
main()           