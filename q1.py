available_choice=4
moves=[[-1, 0],[1,0], [0,1], [0,-1], [0, 0]]
numsList=[]
def bellman(m,action):#e.g.:m(4,3) action(-1,0).
  cnt=0
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
	    cnt+=1
  probability=1.0/cnt  
  return probability
