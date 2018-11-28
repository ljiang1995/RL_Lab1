import numpy as np

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
    if not(n in no_left):
        directions=[].append([-1,0])
    if not(n in no_right):
        directions=[].append([1,0])
    if not(n in no_up):
        directions=[].append([0,-1])
    if not(n in no_down):
        directions=[].append([0,1])
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

def robber_move(state,action):
    p=[] #probability  define later
    r=0  #reward
    a,b,c,d=get_point(state)
    robber=[a,b]
    police=[c,d]
    if(robber==police):
        r=-10
        #how to move

    else:
        directions=get_possible_directions(c,d)
        #police move
        for i in range(4):
            c_temp=c+directions[i][0]
            d_temp=d+directions[i][1]
            if(c_temp in range(4) and d_temp in range(4)):
                state=get_state(a,b,c_temp,d_temp)

        if(robber==bank):
            r=1
    state=get_state(a,b,c,d)
    return state,r
    
#for i in range(4): #test
    state=robber_move(state)
    print(robber)
    print(state)
