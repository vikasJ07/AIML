MAX,MIN=1000,-1000

def minimax(depth,nodeidx,maximizingplayer,values,alpha,beta):
    if(depth==3):
        return values[nodeidx]
    if (maximizingplayer):
        best=MIN
        for i in range(0,2):
            val=minimax(depth+1,nodeidx*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(best,alpha)
            if(alpha>=beta):
                break
        return best
    
    else:
        best=MAX
        for i in range(0,2):
            val=minimax(depth+1,nodeidx*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(best,beta)
            if(alpha>=beta):
                break
        return best
    


values=[3,5,6,9,2,0,-1]
print("The optimal value is:",minimax(0,0,True,values,MIN,MAX))
    