# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:44:51 2022

@author: 39491
"""
import csv
import framework
import matplotlib.animation
import random
import numpy as np
import tkinter
matplotlib.use('TkAgg')
#variables
num_of_drunks = 25
drunks=[]
numd=[]
#create fig
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#give each drunk a number
for i in range (10,251,10):
    numd.append(i)    
num = random.choice(numd)

#base map
f = open('map.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader: # A list of rows
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
        
f.close() 

#make density mat
def makedensity():
     densitymat=np.zeros((300,300))
     return densitymat
 
densitymap = makedensity()

#find pub location
def makepubloc(environment):
    pubx=[]
    puby=[]
    global pubpointx
    global pubpointy
    for i in range(0,len(environment)):
        for j in range(0,len(environment[i])):
           if environment[i][j]==1:
               pubx.append(i)
               puby.append(j)
    pubpointx= list(set(pubx))
    pubpointy= list(set(puby))

#find home location    
def makehomeloc(num,environment):
    homex=[]
    homey=[]
    global homepointx
    global homepointy
    for i in range(0,len(environment)):
        for j in range(0,len(environment[i])):
           if environment[i][j]== num :
               homex.append(i)
               homey.append(j)
    homepointx= list(set(homex))
    homepointy= list(set(homey))

    



#create drunks
for j in range(num_of_drunks):
     makepubloc(environment)
     makehomeloc(num, environment) 
     drunks.append(framework.drunks(pubpointx,pubpointy,homepointx,homepointy,num,drunks))
     
     
     
# main function  
def update(self):
   
    fig.clear()
    
    for i in range(num_of_drunks):
      #make every drunk move and recor the coordinates in density map
      drunks[i].move() 
      drunks[i].makedensitymap(densitymap)
      #prestep is for recording the steps that the drunk takes previously so that could hepl him do not go back
      if ( bool(drunks[i].prestepsx)  & bool(drunks[i].prestepsy) ):
        for x in drunks[i].prestepsx:
          for y in drunks[i].prestepsy:  
        # if the present coords equal to one inside previous steps, than make him go back to th previous position and walk again
            if (x == drunks[i].x & y == drunks[i].y):
                drunks[i].x = drunks[i].prestepsx[len(drunks[i].prestepsx)-1]
                drunks[i].y = drunks[i].prestepsy[len(drunks[i].prestepsy)-1]
                drunks[i].move()

          
          
          
    for k in range(num_of_drunks): #For every drunk
            matplotlib.pyplot.ylim(0, 300) #limit y axis to environment
            matplotlib.pyplot.xlim(0, 300) #limit x axis to environment
            matplotlib.pyplot.imshow(environment, alpha=0.8) #plot environment
            matplotlib.pyplot.scatter(drunks[k].x,drunks[k].y, color = "red") #plot the sheep
    file = "densitymap.txt"
    np.savetxt(file ,densitymap,fmt="%d", delimiter=',')       


def run(): #Function for generating animation
   animation = matplotlib.animation.FuncAnimation(fig, update, frames=200, repeat=False)
   #animation = matplotlib.animation.FuncAnimation(fig, sim, frames=10, repeat=False)
   canvas.draw()

# def Stop(): # function for stopping the model at it's defined conclusion
#     global root
#     root.quit()        
def dm(): # function for stopping the model at it's defined conclusion\
    matplotlib.pyplot.imshow(densitymap, alpha=0.8)
    
def terminate():  # Function to force quit model
    global root
    root.quit()
    root.destroy()

root = tkinter.Tk()    
root.wm_title("Drunks Model") #Set title

#Create canvas for drawing model onto
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create buttons which can call functions. Here I have created a 'run' button
# and a 'stop' button
run_button = tkinter.Button(root, text="Run Model", command=run) #button to start model
quit_button = tkinter.Button(root, text="Stop Model", command=terminate) #button to stop model
dm_button = tkinter.Button(root, text="Density Map", command=dm)
run_button.configure(bg='green') #colours start button green
quit_button.configure(bg='red') #colours stop button red
dm_button.configure(bg='blue')
run_button.pack(side=tkinter.BOTTOM) #locates start button at bottom of gui
quit_button.pack(side=tkinter.BOTTOM) #locates stop button at bottom of gui
dm_button.pack(side=tkinter.BOTTOM)

tkinter.mainloop() #load up GUI   
