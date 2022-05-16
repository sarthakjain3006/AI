# """ " Python Implementation of 8 puzzle search  "
#       SID- 862324889
#       Name- Sarthak Jain
# """
# import heapq as h
# import collections
# class Node:
#       def __init__(self, value):
#             self.left = None
#             self.right = None
#             self.down=None
#             self.up= None
#             self.value = value
#             self.h=None

      


# def a_star(problem,mode ): #problem will be passed as value, mode is to determine which algorithm to run
#       gn=0
#       working_list=collections.deque()
#       visited= []
#       misplaced = None
#       successors=expand(problem)
#       working_list=successors
#       successors.pop()

#       def calc_misplaced(N):
#                   res=0
#                   for i in range(1,9):
#                         if N[i] != i+1:
#                               res+=1
#                   return res
#       def calc_manhattan(ans):
#             res=sum(abs((ans-1)%3 - j%3) + abs((ans-1)//3 - j//3) #we calculate the minimum distance needed (in both x and y axis) for the misplaced tile to move to its goal state
#             for j, ans in enumerate(j) if ans)
#             return res
#       while successors:
#             gn+=1
#             for i in successors:
#                   for k in successors[i]:
#                         misplaced=calc_misplaced(successors[i])
#                         manhattan= calc_manhattan(successors[i])
#                         if mode==2:
#                               hn= misplaced
#                         elif mode==3:
#                               hn= misplaced+manhattan
#                         else: hn=0
#                         fn=gn+hn
                  





     

      
      


      


# inp=[]
# for i in range(9):
#       inp[i]=input("please select a number from 0-9")


# goal_state=[1,2,3,4,5,6,7,8,0]
# zero_at=inp.find(0)


# if mode==1:
#       a_star(inp, )