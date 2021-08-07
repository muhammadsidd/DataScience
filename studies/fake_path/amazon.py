import numpy as np
#
# Complete the 'deliveryPlan' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY allLocations
#  2. INTEGER numDeliveries
#
def deliveryPlan(allLocations, numDeliveries):
    # Write your code here
    al = np.array(allLocations,dtype=int)
    l1 =[]
    alsorted = np.array(sorted(al,key=lambda al : np.sqrt(np.square(al[0])+np.square(al[1]))))
    # for loc in al:
    #     l1.append()
    
    # temp = []
    # for i in range(numDeliveries):
    #     temp.append(l1.index(min(l1)))
    #     l1[l1.index(min(l1))]=np.inf
    # locs =[]
    # for i in range(0,len(temp)):
    #     locs.append(allLocations[temp[i]])
    
    # return locs
    m = alsorted.tolist()
    n=[]
    for i in range(numDeliveries):
        n.append(m[i])
        
    
    return n
    
        
if __name__ == '__main__':

    t = deliveryPlan([[1,-3],[1,2],[3,4],[0,1],[0,2]],3)
    print(t)

    