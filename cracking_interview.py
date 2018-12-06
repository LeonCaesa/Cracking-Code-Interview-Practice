#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/*================================================================
*   Copyright (C) 2018. All rights reserved.
*   Author：Leon Wang
*   Date：Thu Nov 29 11:11:28 2018
*   Email：leonwang@bu.edu
*   Description： Cracking the code interview questions
================================================================*/
"""

string='54321'
from collections import Counter
from collections import defaultdict


def find_unique(string):
    """
        Function to find unique strings, if string element is unique return True
    """
    diction=dict()
    for i in range(len(string)):
        if string[i] in diction:
            return False
        else:
            diction[string[i]]=i
    return True
print(find_unique(string))


string1='abcde'
string2='edcba'
def if_permutation(string1,string2):
    
    """
        Given two strings, find if one is a permutation of another
    """
    if len(string1)!=len(string2):
        return False
    else:   
        
        count=Counter()
        for i in string1:
            
            count[i]+=1
        for j in string2:
            if count[j]==0:
                return False
            count[j]-=1
        return True
    
def replace_space(string,length):
    """
        Function to replace spaces with "%20"
    """
    
    List=[]
    for i in range(length):
        if string[i]==' ':
            List.append('%20')
        else:
            List.append(string[i])
    print(List)
    string="".join(List)
    return string
replace_space("Mr John Smith ",13)


def palidrome(string):
    """
        Function to check if a string is a permutation of a palinidrome
    """
    string=string.lower()
    count=Counter()
    for i in string:
        count[i]+=1
    start=0
    for j in count:
        if count[j]%2==1 and j!=' ':
            start+=1
            if start>1:
                return False
    return True
string='Tact Coa'
palidrome(string)

def one_away(string1,string2):
    """
        Function to check if the string is one edit away
    """
    if abs(len(string1)-len(string2))>1:
        return False
    else:
        count=Counter()
        for j in string1:
            count[j]+=1
        print(count)
        start=0
        for i in string2:
            if i in count:
                count[i]-=1
                if count[i]<-1:
                    start+=1
            else:
                start+=1
        if start>1:
            return False
        return True
            
            
            
string1='pale'
string2='bake'
one_away(string1,string2)


    
def compression(string):
    
    """
        Function to conduct string compression
    """
    count=defaultdict(list)

    strings=""
    count[string[0]].append(1)
    
    for i in range(1,len(string)):
        if string[i] in count and string[i]==string[i-1]:
            # only accumulate if consistent and counter started
            count[string[i]][-1]+=1
        elif string[i] not in count:
            strings=strings+str(string[i-1])+str(count[string[i-1]][-1])
            count[string[i]].append(1)
            
        elif string[i]!=string[i-1]:
            strings=strings+str(string[i-1])+str(count[string[i-1]][-1])
            count[string[i]].append(1)
       
    strings=strings+str(string[i-1])+str(count[string[i-1]][-1])
    
    return min(strings,string,key=len)

string='aabcccccaaa'
compression(string)

def string_rotat(string1,string2):
    
    """
        Function to rotate the strings
    """
    if len(string1)!=len(string2):
        return False
    else:
        temp=string1*2
        return temp.find(string2) !=-1
    
string1='waterbottl'
string2= 'erbottlewa'
string_rotat(string1,string2)
    

def triple_steps(n):
    """
        Dynamic Triple Steps
    """
    if n<=1:
        return 1
    elif n==2:
        return 2
    else:
        return triple_steps(n-3)+triple_steps(n-2)+triple_steps(n-1)
triple_steps(4)



def check_path(r,c,limits,path,memo):
    """
        Function to check if there is a path for robot
    """
    if memo[r][c] !=-1:
        return memo[r][c]
    if r<0 or c<0:
        return False
    origin=(r==0)and (c==0)

    if origin or check_path(r-1,c,limits,path,memo) or check_path(r,c-1,limits,path,memo):
        memo[r][c]=1
        path.append([c,r])
        return True
    else:
        memo[r][c]=0
        return False
        
def robot(r,c,limits):
    """
        Main function to check if bot can reach the ends
    """
    
    path=[]
    memo=[[-1]*(c+1)]*(r+1)
    if check_path(r,c,limits,path,memo):
        return path
    



def power_set(sets,current,index):
    """
        Function to return all the subsets of a set
    """
    if index==len(sets):
        return current
    else:
        List=[]
        
        for e_e in current[index-1]:
            complement=[{i} for i in sets if i not in e_e]
            for e_c in complement:
                
                if e_c.union(e_e) not in List:
                    
                    List.append(e_c.union(e_e))
            
        current[index]=List
    return current

def power_main(sets):
    
    """
        Main function to implement power set
    """
    current=dict()
    
    current[1]=[{i} for i in sets]
    
    for i in range(2,len(sets)+1):
        current= power_set(sets,current,i)
        
    return current
        
    
    
    
sets=[1,2,3,4]
power_main(sets)

def recursive_muti(a,b):
    """
        Function to do mutiplication using recursion
    """
    if b==1:
        return a
    else:
        return a+recursive_muti(a,b-1)

recursive_muti(4,3)

def permu_o_d(string,index,collection):
    """
        Compute all string of unique character
    """
    if index==len(string):
        return collection
    List=[]
    for e_e in collection[index-1]:
        
        complement=[i for i in string if i not in e_e]
        
        for e_c in complement:
            
            for e_i in range(1,len(e_e)-1):
                if e_e[:e_i]+e_c+e_e[e_i:] not in List:
                    List.append(e_e[:e_i]+e_c+e_e[e_i:])
            if e_c+e_e not in List:
                List.append(e_c+e_e)
            if e_e+e_c not in List:
               
                List.append(e_e+e_c)
            
    collection[index]=List
    
    return collection
    
def permu_main(string):
    """
        Main function to implement permutate_o_d
    """
    collection=dict()
    collection[0]=[i for i in string]
    for index in range(1,len(string)):
        collection=permu_o_d(string,index,collection)
    return collection

a=permu_main('1234')



def bracket(n,indexs,collection):
    """
        Function to add bracket 
    """
    if len(collection)==n:
        return collection
    else:
        List=[]
        for e_b in collection[indexs-1]:
            
            if "("+str(e_b)+")" not in List:
                
                List.append("("+str(e_b)+")")
                
            if e_b+"()" not in List:
                
                List.append(e_b+"()")
            if "()"+(e_b) not in List:
                
                List.append("()"+(e_b))
   
        collection[indexs]=List
        return collection
    
    
def bracket_main(n):
    """
        Main function used to implement bracket 
    """
    collection=dict()
    collection[0]=['()']
    for indexs in range(1,n):
        collection=bracket(n,indexs,collection)
    return collection
    
bracket_main(3)
    

