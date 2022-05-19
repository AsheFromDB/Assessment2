# -*- coding: utf-8 -*-
"""
Created on Sun May 15 02:14:04 2022

@author: 39491
"""

import random

pubpointx=[]
pubpointy=[]
homepointx=[]
homepointy=[]


class drunks:
    def __init__(self,startpointx,startpointy,homex,homey,number,drunks):
         self.x=random.choice(startpointx) #due to pub is a polygon not a point so the start poitns should be a set
         self.y=random.choice(startpointy)
         self.startpointx=self.x
         self.startpointy=self.y
         self.number=number
         self.homex=homex
         self.homey=homey
         self.athome = False #a bool variable for defining the drunk is at home or not
         self.prestepsx =[] #for storing previous steps' information
         self.prestepsy =[]
         self.drunks = drunks
    def move(self):
     for x in self.homex:
      for y in self.homey:# for each x in home coords set
       if(self.x == x & self.y == y & self. athome ==False):# if the drunk is at home
          self.athome = True#set the bool true
          self.x=self.x# make the drunk stable
          self.y=self.y
     if (self.athome==False):#if not at home then continue finding way home
         if random.random() < 0.5:
                self.x=(self.x+10)%300
         else:
                self.x=(self.x-10)%300
         if random.random() < 0.5:
                self.y=(self.y+10)%300
         else:
                self.y=(self.y-10)%300
     self.prestepsx.append(self.x)#add the previous coords into the previous coords list
     self.prestepsy.append(self.y)
      
       
    def makedensitymap(self,densitymap):# if they are not home record each step they take to make the density map
     if (self.athome == False):
        densitymap[self.x][self.y] += 1  
        

 
    


        
        
   
    