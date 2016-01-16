# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open n the template in the editor.
'''
In this search we used the (total circular distance /4) as our heuristic function. 


Circular distance for one tile is min moves need to be made by the tile to reach its intended position independently. 


Then we divide it by 4 because optimistically in one move we can help 4 tiles get closer to intended positions. 


circular distance for tile i= cdi= |xnow-xintended|+|ynow-yintended|

total circular distance = (cd1+cd2+......+cd16)/4 


 

In other words, if the element a[i][j] at the [i][j] position in the 4X4 matrices, but is suppose to be in [ai][aj] position. Then, a[i][j]=(ai)*4+(aj+1). To move from [i][j] to [ai][aj], we need to move the row (Left or Right) |i-ai| first and the column (Up and Down) |j-aj| times. But notes that, if we move Left |i-ai| =3 times to get into the correct column number for a[i][j], we can also do this by Right |j-aj| =1 time to move to the correct column number. Therefore, the total circular distance is  |i-ai|+ |j-aj| where we change 3 to 1 for each number of  |i-ai| and  |j-aj|. 


It is admissible, because for each element we only consider the shortest way to get it into the correct position, however when we making one move we actually change the circular distance for four elements which will results more moves. So the h(N) distance/4 must be smaller for the number of actual moves to get everything into the correct position. Bounds on our heuridtic functions are [0,16]


Successor function:

we add 15 children on each node on expansion.

It can make any move from 16 moves except the move that directly nullifies the last move made.
(eg We cannot make a R2 move right after L2)
'''
__author__ = "Owner"
__date__ = "$12 Sep, 2015 5:17:25 PM$"
import copy
import Queue as Q
import sys



class node(object):
    
    def __init__(self, s, prevcost, prevpath, move):
        self.s = s
        self.h=self.cirdh()
        self.g=prevcost+1.0
        self.f=self.h+self.g
        self.path=prevpath+" "+move
    
    def check(self):
        for i in range(0,4):
            for j in range (0,4):
                if(self.s[i][j]!=i*4+j+1):
                    return False
        return True
                
    def cirdh(self):
        cird=0
        y=self.s
        #print y
        for i in range (0,4):
            for j in range (0,4):
                x=y[i][j]
                #print x
                if(1<=x<=4):
                    ai=0
                elif(5<=x<=8):
                    ai=1
                elif(9<=x<=12):
                    ai=2
                else:
                    ai=3
                #print ai
                aj=x%4
                if(aj>0):
                    aj=aj-1
                else:
                    aj=3
                #print aj
                di=abs(i-ai)
                #print di
                if(di==3):
                    di=1
                dj=abs(j-aj)
                if(dj==3):
                    dj=1
                #print dj
                l =((di+dj)/4.0)
                #print l
                cird=cird+l
        return cird    
    
    def succ(self, i):
	#print len(self.path.split(" "))
	prevmove=""
	if self.g!=0:
		prevmove=self.path.split(" ")[-1]
	#newmove=x.path.split(" ")[-1]
		    
        if(0<i<5):
            #if(i==1):
            ns=copy.deepcopy(self.s)
            j=ns[i-1]
            j=j[1:]+j[:1]
            ns[i-1]=j
            #print ns
            move="L"+str(i)
	    if prevmove!="R"+str(i):
            	nk=node(ns,self.g,self.path,move)
            #print type(nk)
            	return nk
	    else:
		return "Ignore me"
        elif(i<9):
            #print "hey"
            ns=copy.deepcopy(self.s)
            i=i-4
            j=ns[i-1]
            j=j[3:]+j[0:3]
            ns[i-1]=j
            #print ns
            move="R"+str(i)
            if prevmove!="L"+str(i):
            	nk=node(ns,self.g,self.path,move)
            #print type(nk)
            	return nk
	    else:
		return "Ignore me"
        elif(i<13):
            #print "hey"
            ns=copy.deepcopy(self.s)
            i=i-8
            temp=ns[3][i-1]
            ns[3][i-1]=ns[2][i-1]
            ns[2][i-1]=ns[1][i-1]
            ns[1][i-1]=ns[0][i-1]
            ns[0][i-1]=temp
            #j=ns[i-1]
            #j=j[3:]+j[0:3]
            #ns[i-1]=j
            #print ns
            move="D"+str(i)
            if prevmove!="U"+str(i):
            	nk=node(ns,self.g,self.path,move)
            #print type(nk)
            	return nk
	    else:
		return "Ignore me"
        elif(i<17):
            #print "hey"
            ns=copy.deepcopy(self.s)
            i=i-12
            temp=ns[0][i-1]
            ns[0][i-1]=ns[1][i-1]
            ns[1][i-1]=ns[2][i-1]
            ns[2][i-1]=ns[3][i-1]
            ns[3][i-1]=temp
            #j=ns[i-1]
            #j=j[3:]+j[0:3]
            #ns[i-1]=j
            #print ns
            move="U"+str(i)
            if prevmove!="D"+str(i):
            	nk=node(ns,self.g,self.path,move)
            #print type(nk)
            	return nk
	    else:
		return "Ignore me"       
if __name__ == "__main__":
    for arg in sys.argv: 
    	f=arg
    infile=open(f,"r")
    inputstate=infile.readlines()

    istate=[]
    for i in inputstate:
    	i=i.rstrip("\n")
     	#print i
    	iline=i.split(" ")
	#print iline
	iline[0]=int(iline[0])
	iline[1]=int(iline[1])
	iline[2]=int(iline[2])
	iline[3]=int(iline[3])

    	istate.append(iline)
    v=[]
    state=0
    #istate=[[11, 2, 12, 9], [6, 10, 8, 16], [14, 15, 7, 1], [5, 13, 3, 4]]
    fringe=Q.PriorityQueue()
    
    ininode=node(istate,-1,"","")
    #print ininode.h, ininode.f
    if(ininode.check()):
        print "initial state is goal!!!!!!!!!"
    else:
        fringe.put((ininode.f,ininode))
        
        while not fringe.empty():
                    #print "here i am"
            currnode=fringe.get()[1]
    
            #state+=1
           #
            #if(state%1000==0):
            #print state, currnode.h, currnode.g, currnode.f
            if(currnode.check()):
                print "Found it"
                print "Cost: ",currnode.g
                print "Path: \n",currnode.path

                break
            else:
                #print "there i am"
               # newnode=[]
                for i in range(1,17):
                    
                    x=currnode.succ(i)
                    if x!="Ignore me":
                    #print type(currnode)
                    #print type(currnode.succ(i))
                    #print type(x.f)
                 #   h=x.f
                #    if x.s not in v:
		    #print x.path.split(" ")[-1],x.path.split(" ")[-2]
		    
                    	fringe.put((x.f,x))####change back this block
                    
               # v.append(currnode.s)    
        if fringe.empty():
            print "Search failed"
        #print states
#    for z in fringe: print z
        
    
