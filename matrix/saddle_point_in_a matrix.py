 

#min in a row  and max in a column 
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

n=len(arr)

for i in range(n):
    mi=arr[i][0]
    ind=i 
    
    for j in range(1,n):
        if arr[i][j]<mi:
            mi=arr[i][j]
            ind=j 
    c=0
    for k in range(n):
        if arr[k][ind]<mi :
            c+=1 
    if c==n-1:
            print(mi)
 