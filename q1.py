import numpy as np
Max_T=15
u=np.zeros((Max_T+1,902))
available_choice=4
moves=[[-1, 0],[1,0], [0,1], [0,-1], [0, 0]]
numsList=[]
def bellman(m):#e.g.:m(4,3) action(-1,0).
  cnt=0
  s=[]
  for row in range(4):
        numsList.append([])
        for column in range(2):
          num =0
          numsList[row].append(num)
  for i in range(available_choice):
      for j in range(2):
   	    numsList[i][j]=m[j]
	    numsList[i][j]+=moves[i][j]
      if (numsList[i][0] in range(5)) and (numsList[i][1] in range(6)):	
	    s.append(numsList[i])
            cnt+=1
  probability=1.0/cnt  
  return probability,s

def reward(T, state):
	if T==Max_T:
		if state==900:# state fail
			u[T,state]=0
		elif (state>=840) and (state!=840+24+4):
			u[T,state]=1
	else:
		if state==900:
			u[T,state]=0
		elif state==901:
			u[T,state]=1
		else:
			temp=state%30
			c=temp//6
			d=temp%6
			bellman(m)
			
		
