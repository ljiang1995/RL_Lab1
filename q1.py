available_choice=4
moves=[[-1, 0],[1,0], [0,1], [0,-1], [0, 0]]
numsList=[]
def bellman(p,m,action):#e.g.: p(3,4) m(4,3) action(-1,0).
  for row in range(4):
        numsList.append([])
        for column in range(2):
          num =0
          numsList[row].append(num)
  print numsList
  for i in range(available_choice):
      print('temp1[i][j] is',numsList,p)
      for j in range(2):
   	  numsList[i][j]=p[j]
	  	numsList[i][j]+=moves[i][j]
		
  probability=1
 

  return probability
