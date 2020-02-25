# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:56:50 2020

@author: deba
"""
def magic(n):
    mat=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        mat.append(l)
        
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(mat[i][j]):
            j=j-2
            i=i+1
            continue
        else:
            mat[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=" ")
        print()
    c=(n*(n**2+1))/2
    print("the sum of the row/column/diagonals is: "+str(c))
    
    
print(magic(int(input())))