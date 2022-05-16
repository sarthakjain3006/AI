import heapq
from time import time

def swap(N,x,y): #used to make swaps 
    puzzle = N[:]
    temp = puzzle[y]
    puzzle[y] = puzzle[x]
    puzzle[x] = temp
    return puzzle

def getsuccessors(puzzle):
    paths = []
    index = puzzle.index(0)
    if index - 3 >=0:
        paths.append(swap(puzzle,index,index - 3))
    if index %3 !=0:
        paths.append(swap(puzzle,index,index - 1))
    if index + 3 <  9:
        paths.append(swap(puzzle,index,index + 3))
    if index %3 !=2:
        paths.append(swap(puzzle,index,index + 1))
    return paths

def manhattan(ans):
            res=sum(abs((val-1)%3 - j%3) + abs((val-1)//3 - j//3) for j, val in enumerate(ans) if val)  #we calculate the minimum distance needed (in both x and y axis) for the misplaced tile to move to its goal state1
            return res

def misplaced(N):
    count = 0
    for i in range(0, len(goal_state)):
        if N[i] == 0:
            continue
        if (N[i] != goal_state[i]):
            count += 1
    return count
    
def astarsearch(problem,mode):
    
    path=[]             #search path    
    tpath=[]             #store temprorary paths                                  
    visited_state = set()         
    # wl = []  #wl=working list       #using priority queue for node and path
    newpath=[]     #current path in bigger loop
    fn= 0       #f(n)=h(n)+g(n)
    gn=0
    hn=0        #hueristic
    heapq.heappush(newpath,(0,problem))
    _, curr = heapq.heappop(newpath) #retrieving current node value
    # heapq.heappush(wl,(0,problem))
    while True: 
        if tuple(curr) in visited_state:
            _,path=heapq.heappop(newpath)  #pop next node from working list
            curr = path[-1]    
            continue
        if curr == goal_state:
            return (path, len(visited_state))
        if tuple(curr) not in visited_state:
            visited_state.add(tuple(curr))
            res = getsuccessors(curr)
   

            for i in res: #for every successor
                tpath= path + [i]
                gn=len(tpath)
                
                
                if mode==2:
                    hn=misplaced(i)
                    # print(hn)
                elif mode==3:
                    hn= manhattan(i)
                else: hn=0
                fn = gn+ hn #calculate node cost

                if tuple(i) not in visited_state:
                    # heapq.heappush(wl,(fn,i)) #push fn with successor so it is sorted in working list
                    heapq.heappush(newpath, (fn,tpath))     # push  fn and path with successor to the new path
        _,path=heapq.heappop(newpath)
        curr = path[-1]
        # print(len(path))    #pop new path and store it as path
        # _,curr=heapq.heappop(wl)          #pop next node from working list
        if not path:
            break
    
    print("impossible solution")
    return 0

def eval(problem, mode):
    curr_time=time()
    dep,nonv=astarsearch(problem, mode)
    for i in dep:
        print(i)
    print("depth found at ",len(dep))
    finalt=float(time()-curr_time)
    if mode==1:
        f= open("UCSt.txt","a")
        f.write(str("{:0.5f}".format(finalt)+"  "+str(len(dep))+" "+str(nonv)+"\n"))
        f.close
    elif mode==2:
        f= open("Amist.txt","a")
        f.write(str("{:0.5f}".format(finalt)+"  "+str(len(dep))+" "+str(nonv)+"\n"))
        f.close
    else:
        f= open("Amant.txt","a")
        f.write(str("{:0.5f}".format(finalt)+"  "+str(len(dep))+" "+str(nonv)+"\n"))
        f.close



goal_state=[1,2,3,4,5,6,7,8,0]
# problemset=[[1,2,3,4,5,6,7,8,0],[1,2,3,4,5,6,0,7,8],[1,2,3,5,0,6,4,7,8],[1,3,6,5,0,7,4,8,2]]
problemset = [[1,2,3,4,5,6,7,8,0],[1,2,3,4,5,6,0,7,8],[1,2,3,5,0,6,4,7,8],[1,3,6,5,0,7,4,8,2],[1,6,7,5,0,3,4,8,2],[7,1,2,4,8,5,6,3,0],[0,7,2,4,6,1,3,5,8],[8,6,7,2,5,4,3,0,1]]
# problemset = [[1,3,6,5,0,7,4,8,2]]

for i in problemset:
    for j in range(1,4):
        eval(i,j)
        print("\n")
    # curr_time=time()
    # ans=astarsearch(i, 2)  #add mode for: 1) UCS, 2) A star with misplaced tiles; 3) A star with manhattan distance
    # if ans == 0:
    #     continue
    # for j in ans:
    #     print (j)
    # print("Depth = ",len(ans))
    # f= open("Amant.txt","a")

    # finalt=float(time()-curr_time)
    # print(finalt)

    # f.write(str("{:0.5f}".format(finalt)+"  "+str(len(ans))+"\n"))
    # f.close()

# [1,3,4,8,6,2,7,0,5],[2,8,1,0,4,3,7,6,5],[2,8,1,4,6,3,0,7,5],[5,6,7,4,0,8,3,2,1]]
# for i in range (len(problemset)):

#     start_time= time()
#     ucs= astarsearch(problemset[i],1)
#     ucstime=time()
#     amis= astarsearch(problemset[i],2)
#     amistime=time()
#     aman= astarsearch(problemset[i],3)
#     amantime=time()
#     ucst=str(ucstime-start_time)
#     f = open("UCS.txt", "a")
#     f.write(ucst,len(ucs))
#     f.close
#     amist=str(amistime-start_time)
#     f = open("amist.txt", "a")
#     f.write(amist,len(amis))
#     f.close
#     amant=str(amantime-start_time)
#     f = open("amant.txt", "a")
#     f.write(amant,len(aman))
#     f.close
    
   







        



