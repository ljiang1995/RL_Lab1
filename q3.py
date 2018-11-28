import numpy as np
import random
import matplotlib.pyplot as plt

no_left=[0,4,8,12]
no_right=[3,7,11,15]
no_up=[0,1,2,3]
no_down=[12,13,14,15]
bank=[1,1]
robber=[0,0] #[a,b]
police=[3,3] #[c,d]

def get_possible_directions(x,y):
    directions=[]
    n=4*y+x
    directions.append([0,0])
    if not(n in no_left):
        directions.append([-1,0])
    if not(n in no_right):
        directions.append([1,0])
    if not(n in no_up):
        directions.append([0,-1])
    if not(n in no_down):
        directions.append([0,1])
    return directions

def get_point(state):
	temp=state//16
	a=temp%4
	b=temp//4
	temp=state%16
	c=temp%4
	d=temp//4
	return a,b,c,d

def get_state(a,b,c,d):
    temp=(a+4*b)*16+c+4*d
    return temp

def get_probability(x,y):
  m=[x,y]
  cnt=0
  s=[]
  numsList=[]
  for row in range(5):
        numsList.append([])
        for column in range(2):
          num =0
          numsList[row].append(num)
  for i in range(5):
      for j in range(2):
   	    numsList[i][j]=m[j]
   	    numsList[i][j]+=moves[i][j]
      if (numsList[i][0] in range(4)) and (numsList[i][1] in range(4)):	
      		s.append(numsList[i])
      		cnt+=1
  p=1.0/cnt  
  return p,s



def reward(state,action):
    p=0  #probability  
    r=0  #reward
    s=[]
    a,b,c,d=get_point(state)
    robber=[a,b]
    police=[c,d]
    if(robber==police):
        r=r-10
    if(robber==bank):
        r=r+1
    a=a+action[0]
    b=b+action[1]
    p,s=get_probability(c,d)
    state=get_state(a,b,c,d)
    return state,r,p

    




#for i in range(4): #test
    state=robber_move(state)
    print(robber)
    print(state)
