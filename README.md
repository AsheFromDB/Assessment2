# Assessment2
This code has been developed and tested.

When you run runfile.py it will open a tkinter window to run the animation model. All drunks will walk home as required. When the model is run, it will create a density map as a text file and can be drawn through the tkinter window to plot the density of the drunks through each point on the map.

The code is stored in a folder calleddrunk. The folder named drunk contains four files: densitymap.txt, map.txt, runfile.py and framework.py.

The map.txt file is used as the source data for loading the map. It is a 300 x 300 pixel raster file of the town plan. Each line in the file is a row in the raster image, starting from the top left corner. The background is represented by the number 0, the bars by 1 and the houses by 10 to 250 (at intervals of 10).

densitymap.txt is a density map created to show the density of drunks passing through each point on the map.

create runfile.py is the py file created to implement all the functions.

Create framework.py is the framework for the drunk class

    Pull in the data file and find the pub points and home points.
    Draw the pub and house on the screen.
    Model the drunks leaving the pub and arriving at the home and store how many drunks passed each point on the map.
    Plot the density of drunks passing each point on the map.
    Save the density map as text to a file.

Basic algorithmic logic.

    For each drunk (a number between 0 and 250 will be assigned before leaving the bar), move the drunk randomly left/right/up/down into a randomly chosen loop. When it hits the correctly numbered house, stop the process.

Please refer to the runfile.py file for the basic functionality implementation
    Drunks start at an arbitrary point within the confines of the bar
    From the starting point, the drunks randomly travel in four directions, up, down, left, right and centre, until they come across a house with the same number as their own. To ensure that the drunks get home faster, the algorithm adds the ability to record the previous paths taken by each drunks, which prevents them from backtracking and thus saves time on the way home. It also records every point that the alcoholic passes through, which is stored in the densitymap.txt file and can also be viewed at runtime.

Framework.py:
This contains the properties of each alcoholic: his number, his current position, his previous position, etc., and includes the function move which sets him in motion.
