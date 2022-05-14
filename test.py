# import util

puzzle = [1,3,4,2,5,6,8,7,0]
goal = [1,2,3,4,5,6,7,8,0]


#function to calculate misplaced tile
def calculate_h(N):
    res=0
    for i in range(1,9):
        if N[i] != i:
            res+=1

def swap(N,x,y):
    puzzle = N[:]
    temp = puzzle[y]
    puzzle[y] = puzzle[x]
    puzzle[x] = temp
    return puzzle

def expand(puzzle):
    paths = []
    index = puzzle.index(0)
    if index - 3 >=0:
        paths.append(swap(puzzle,index,index - 3))
    if index - 1 >=0:
        paths.append(swap(puzzle,index,index - 1))
    if index + 3 <  10:
        paths.append(swap(puzzle,index,index + 3))
    if index +1 < 10:
        paths.append(swap(puzzle,index,index + 1))
    return paths

q = [3,7,6,5,1,2,4,0,8]
print(move_zero(q))

# def aStarSearch(problem, heuristic=calculate_h):
#     path=[]                       
#     #store temprorary paths              
#     tpath=[]               
#     #all visited nodes                  
#     visited_nodes = []                
#     #using priority queue for node and path
#     pq = PriorityQueue()                   
#     current_path=PriorityQueue()      
#     pq.push(problem.getStartState(),0)
#     #start node
#     current_node = pq.pop()
#     #exit the current code
#     while not problem.isGoalState(current_node):
#         if current_node not in visited_nodes:
#             visited_nodes.append(current_node)
#             successors = problem.getSuccessors(current_node)
        
#             for node,move,cost in successors:
#                 tpath = path + [move]

#                 #using heuristics for calculating cost
#                 node_cost = problem.getCostOfActions(tpath) + heuristic(node,problem)
                
#                 #add node if not in visited nodes
#                 if node not in visited_nodes:
#                     pq.push(node,node_cost)
#                     current_path.push(tpath,node_cost)

#         path = current_path.pop()    
#         current_node = pq.pop()
#     return path