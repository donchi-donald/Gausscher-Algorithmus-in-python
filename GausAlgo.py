#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:26:31 2020

@author: root
"""

import numpy as np


def gausAlgo(*args):
    rows=len(args)
    columns=getTheMaxX(args[0])
    
    #print("columns ",columns)
    for x in range(len(args)):
        if(getTheMaxX(args[x])>columns):
            columns=getTheMaxX(args[x])
    
    columns+=1
    #print("columns ",columns)
    limit=0
    matrix=np.zeros((rows,columns),dtype=float)
    mRow=0
    
    ## we fill up the matrix with the equations
    for i in range(rows):
        tmp=getTerms(args[i])
        for x in range(1,len(tmp),2):
            matrix[mRow][int(tmp[x])]=float(tmp[x-1])
        matrix[mRow][columns-1]=float(tmp[len(tmp)-1])
        mRow+=1
            
    print(matrix)
    move=0
    move1=0              
    while(limit <columns-1):
        limit+=1
        #break
        
        """
        turn the midpoint to 1
        """
        
        divider=matrix[move][move1]
        for x in range(columns):
            matrix[move][x]/=divider     
        print(matrix)
        
        """
        get 0 
        """
        print("\n\n")
        tmpPivot=matrix[move]
        
        for x in range(rows):
           
            if (x==move):
                continue
            if(isNeg(matrix[x][move1])==1):
                mulNumb=matrix[x][move1]*-1 
                for i in range(columns):
                    #print(matrix[x][i]," + ",tmpPivot[i]*mulNumb)
                    matrix[x][i]+=(tmpPivot[i]*mulNumb)
                    #print(matrix[x][i])
            else :
                mulNumb=matrix[x][move1]*-1
                for i in range(columns):
                    #print(matrix[x][i]," + ",tmpPivot[i]*mulNumb)
                    matrix[x][i]+=(tmpPivot[i]*mulNumb)
                    #print(matrix[x][i])
                
        move+=1
        move1+=1
        print(matrix)
        


     
# check if a character is a negative signe '-' 
def isNegSign(sign):
    return sign=='-'

# check if a character is a positive signe '+' 
def isPosSign(sign):
    return sign=='+'

# check if a number a signed number 
def isNeg(item):
    return item*-1 > 0

# return an array of an linear equation with the index
# egg "1x0+2x1+2x2=2" return => ['1', '0', '+2', '1', '+2', '2', '2']
def getTerms(expr):
    result=[]
    st=""
    for i in range(len(expr)):
        if(str.isnumeric(expr[i]) or isPoint(expr[i])):
            if(i>0):
                if(isNegSign(expr[i-1])==1 or isPosSign(expr[i-1])==1):
                    st+=expr[i-1]
            st+=expr[i]
            
        if ((not(str.isnumeric(expr[i])) or i==(len(expr)-1)) and not isPoint(expr[i]) and len(st)>0):
            result.append(st)
            st=""
            
    return result


# check if the character is a point '.'
def isPoint(c):
    if(c=='.'):
        return True
    return False


def getIndex(array,value):
    result=0
    for i in range(len(array)):
        if(array[i]==value):
            result=i
    return result

# return the max x_value in an expression
# egg: 1x0+2x1+2x2 return => 3
def getTheMaxX(expr):
    maxx=0
    for x in range(len(expr)):
        if(expr[x]=='x'):
            if(int(expr[x+1])>maxx):
                maxx=int(expr[x+1])
    return maxx+1




"""
examples
"""


#print(getTerms("1x0+2x1+2x2=2"))

print(isNeg(4))
print(getTheMaxX("1x0+2x1+2x2-4x5"))
print(getTerms("1x0+2x1+2x2-4x5"))
#gausAlgo("1x0+2x1+2x2=2","1x0+3x1-2x2=-1","3x0+5x1+8x2=8")
#gausAlgo("1x0+1x1-1x2=1","2x0-3x1+2x2=-2","3x0+1x1-1x2=3")
#gausAlgo("-1x0+1x1-2x2=-4","-1x0-1x1-1x2=-11","2x0+1x1-1x2=8")
#gausAlgo("2x0+1x1+-1x2=1","1x0-1x1+1x2=2","4x0+3x1+1x2=3") 
#gausAlgo("1x0-1x1+2x2=5","3x0+2x1+1x2=10","2x0-3x1-2x2=-10")
#gausAlgo("4x0+7x1+3x2=-33","4x0+3x1-1x2+4x3=15","-2x1+6x2+4x3=26","2x0+3x1-5x2-1x3=-12")
#gausAlgo("3x0+6x1-5x2+4x3-2x4=13","1x0+2x1-1x2-1x3+1x4=3","2x2-4x3+7x4=0","2x0+4x1-4x2+4x3-4x4=8","0x4=0")
