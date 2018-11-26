import numpy as np
Max_T=15
u=np.zeros((Max_T+1,902))
available_choice=4
moves=[[-1, 0],[1,0], [0,1], [0,-1], [0, 0]]
numsList=[]
def bellman(m):#e.g.:m(4,3) 
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
      if (numsList[i][0] in range(6)) and (numsList[i][1] in range(5)):	
	    s.append(numsList[i])
            cnt+=1
  probability=1.0/cnt  
  return probability,s

def player_move(p):
	possible_move=[]
	player=[[0,0],[0,0],[0,0],[0,0],[0,0]]
	for i in range(5):
		for j in range(2):
			player[i][j]+=p[j]
			player[i][j]+=moves[i][j]
		if (player[i][0] in range(6)) and (player[i][1] in range(5)):	
				possible_move.append(moves[i])
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
def reward(T, state, action):
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
			possible_move=player_move([a,b])
			print possible_move
			best_result=0
			for i in range(len(possible_move)):
				temp_result=0
				for j in range(len(s)):
					temp_result+=probability*reward(T+1,get_state(a,b,s[j]),possible_move[i])
				if temp_result>=best_result:
					best_result=temp_result
					best_action=possible_move[i]
			u[T,state]=best_result
			return u[T,state]
print reward(0,28,[0,0])
