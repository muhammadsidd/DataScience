import numpy as np 

a = np.array([1,2,3], dtype='int16')
print(a)

b = np.array([[9,0,8,7,6], [1,2,3,4,5]], dtype='int16')
print(b)
print(b.ndim)

print(b.shape)
print(b.dtype)

print(b.itemsize, b.size, b.nbytes)

#getting a specific row 
print(b[0,:])
#cooumn
print(b[:,0])
#specific element 
print(b[1,2])

print(np.zeros((2,3)))

print(np.full((2,3), 99))

print(np.random.rand(4,3)) 

filedata = np.genfromtxt('data.txt', delimiter =',')
# filedata = filedata.astype('int32')
print (filedata)
np.any(filedata > 50, axis=0) #axis 0 looks at coloumn . 1 looks at rows


l = np.random.randint(10, 30,6)
print(l)

l2= np.random.rand(3,3,3)
print(l2)

##random int 3Darray from 0,100
l3 = np.random.randint(0,100, (5,5,5))
print(l3)

l4 = np.random.rand(5,3)
print(l4)
print(l4.min())
print(l4.max())
print(l4.mean(axis=1)) ##mean in each row


l5 = np.random.rand(10,4)
print(l5)

ex = l5[0:5,:]
print(ex)

l6 = np.random.randint(0,100,5)
print(np.all(l6))
##will return true if the array doesnt contain a 0 or none