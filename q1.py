import numpy as np
Max_T=10
u=np.zeros((Max_T+1,902))
available_choice=4
moves=[[-1, 0],[1,0], [0,1], [0,-1], [0, 0]]
moves1=[1, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 25, 26, 27, 29]
moves2=[0, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21, 22, 24, 25, 26, 28]
moves4=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 29]
moves3=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 23]
moves5=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
numsList=[]
def bellman(m):#e.g.:m(4,3) 
  cnt=0
  s=[]
  numsList=[]
  for row in range(4):
        numsList.append([])
        for column in range(2):
          num =0
          numsList[row].append(num)
  for i in range(available_choice):
      for j in range(2):
   	    numsList[i][j]=m[j]
   	    numsList[i][j]+=moves[i][j]
      if (numsList[i][0] in range(6)) and (numsList[i][1] in range(5)):	
      		s.append(numsList[i])
      		cnt+=1
  probability=1.0/cnt  
  return probability,s

def player_move(state):
	possible_move=[]
	a,b,c,d=get_point(state)
	temp_point=6*b+a
	if temp_point in moves1:
		possible_move.append(moves[0])
	if temp_point in moves2:
		possible_move.append(moves[1])
	if temp_point in moves3:
		possible_move.append(moves[2])	
	if temp_point in moves4:
		possible_move.append(moves[3])
	if temp_point in moves5:
		possible_move.append(moves[4])
	return possible_move
def get_point(s):
	temp=s//30
	a=temp%6
	b=temp//6
	temp=s%30
	c=temp%6
	d=temp//6
	return a,b,c,d	
def get_state(a,b,s):
	return 30*(a+6*b)+s[0]+6*s[1]
def reward(T, state,action):
	probability=0
	s=[]
	a,b,c,d=get_point(state)
	if T==Max_T:
		if state==900:# state fail
			u[T,state]=0
			return 0
		elif (a==4 and b==4) and (state!=868): #state 868 is the state that player and minotaur are both at (4,4)
			u[T,state]=1
			return 1
		else:
			return 0
	else:
		a,b,c,d=get_point(state)
		if state==900:
			u[T,state]=0
			return 0
		elif state==901 or((a==4 and b==4) and (state!=868)):
			u[T,state]=1
			return 1
		else:
			a+=action[0]
			b+=action[1]
			if (a==4 and b==4) and (state!=868):
				return 1
			elif (a==4 and b==4) and (state==868):
				return 0
			probability,s=bellman([c,d])
			possible_move=player_move(state)
			
			temp_result=0
			for j in range(len(s)):
					temp_result+=probability*u[T+1,get_state(a,b,s[j])]
			u[T,state]=temp_result
			return u[T,state]

T=Max_T
for state in range(902):
	u[T,state]=reward(T,state,[0,0])
	print ('u[',T,',',state,']=',u[T,state])
for i in reversed(range(Max_T)):
	for state in range(902):
		possible_move=player_move(state)
		temp_reward=0
		best_reward=0
		for j in range(len(possible_move)):
			temp_reward=reward(i,state,possible_move[j])
			if temp_reward>=best_reward:
				best_reward=temp_reward
				
		u[i,state]=best_reward
		print ('u[',i,',',state,']=',u[i,state])


