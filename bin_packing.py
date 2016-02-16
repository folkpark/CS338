# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Parker Folkman
# Last Modified: February 15, 2016
# ----------------------------------------------
#
#
#
# ----------------------------------------------

"""
FIND_NAIVE_SOLUTION:
    Line the the top left corners of the rectangles up along
the y = 0 axis starting with (0,0).
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""

from operator import mul
#import functools

def find_my_solution (rectangles):
    length = len(rectangles)
    placement = []
    initial_placement = []
    upper_left_x = 0
    upper_left_y = 0

    #ID the boxes. Stores in new list
    #Stores in format: (Unique ID, index location in list)
    for i in range(length):
        temp = id(rectangles[i])
        initial_placement.append((temp,i))
        
    #Make a new list of sorted boxes
    sorted_rectangles = sortByWidth(rectangles)

    print(rectangles)
    print(sorted_rectangles)
    
    for i in range(len(sorted_rectangles)):
        box = sorted_rectangles[i]
        width = box[0]
        height = box[1]
        boxID = id(box)
        index = getIndex(boxID, initial_placement)
        print(index)
        coordinate = (upper_left_x, upper_left_y,index) #make a tuple
        placement.insert(index, coordinate)
        upper_left_x = upper_left_x + width

    placement = sortBack(placement)
    print(placement)
    return placement
#---------End_Find_my_Solution------------------------------------------

def getIndex(ID, initial_placement):
    for i in range(len(initial_placement)):
        tempRect = initial_placement[i] #Temporary rectangle
        tempID = tempRect[0] #temporary ID of that rect
        if(tempID==ID):
            index = tempRect[1]
            return index

#This function sorts the rectangles by width. It takes
#a list of tuples, unsorted, and returns those boxes
#sorted by width. Greatest -> smallest
def sortByWidth(rectangles):
    sorted_by_width = sorted(rectangles)
    sorted_by_width.reverse()
    return sorted_by_width

#This function sorts the rectangles by height. It takes
#a list of tuples, unsorted, and returns those boxes
#sorted by height. Greatest -> smallest
def sortByHeight(rectangles):
    sorted_by_height = sorted(rectangles,key=lambda x: x[1])
    sorted_by_height.reverse()
    return sorted_by_height

#These two functions sort the tuples based on area (w*h)
def f(R):
    return R[0]*R[1]
def sortByArea(rectangles):
	return sorted(rectangles,key=f,reverse=True)

def sortBack(placement):
    newPlacement = []
    for i in range(len(placement)):
        tempCord = placement[i]
        tempX = tempCord[0]
        tempY = tempCord[1]
        newCord = (tempX,tempY)
        tempIndex = tempCord[2]
        newPlacement.insert(tempIndex, newCord)
    return newPlacement





    
    
'''
#---------------Sort Back Function-------------------
#This function builds a final placement list, from a
#sorted list of boxes based on uniqueID. The final placement
#returns the boxes in their original order. The function
#takes in the initial_placement list from the ID function,
#the list of sorted rectangles, and returns the placement
#of the boxes based on their unique ID's
def sortBack(initial_placement, sorted_rectangles):
    final_placement = []
    length = len(initial_placement)
    for i in range(length):#Loop through initial placement
        #Grab the ID if the first Box
        initBox = initial_placement[i]
        initBoxID = initBox[0]
        for j in range(length):#Loop through the sorted boxes
            #Grab the ID of the sorted box
            sortBox = sorted_rectangles[j]
            boxID = id(sortBox)
            if(initBoxID==boxID):
                tempTup = initial_placement[j]
                posIndex = tempTup[1]
                final_placement.insert(i,sortBox)
    return final_placement
'''







#Function gets called
def find_solution(rectangles):
    return find_my_solution(rectangles)  # a working example!

'''
Here is an outline of the program:
- Take in rectangles (done)
-ID the Rectangles (done)
-sort the Rects. Here we can do this by either area or width.
  width makes more sense.  (done)
- Stack the Rects (while loop or called recursively)
   1. Function to update the skyline
       Once a box is placed, the skyline needs to be updated. This is done in two steps:
	   1. Instantiates a new line segment corresponding to the top edge of b
	   2. and updates existing segments effected
   2. Function to Find where to place
      (If Sj-1 > Sj => Leftmost
       If Sj > Sj-1 => Rightmost
       Left Endpoint
       Right Endpoint) Total of 4 possible placements
    3. Function to Place the Rect. (Return updated placement list)
       This is a list of positions of the rect and NOT the (w,l)
       The trick here is to either place it in its correct Index based
       on its Unique ID, OR to have someway to identify which box this is
       A. Note I have written a function to sort Back the list based on Unique ID (done)
    4. Maintain a list of tuples of the placements of the Rect's in order
- Return final_placement
Other Needs:
-Need to either pick a really reasonable fix size bin width (let height be dynamic) to start with, or
make the bin capable of being dynamically sized
-When the boxes are placed in the bin, the x,y position of the upper left most corner will be recorded in an list. This will be a list of tuples.
I need a way to ID that box that was placed in the bin
'''






"""
FIND_SOLUTION:
    Define this function in bin_packing.py, along with any auxiliary
functions that you need.  Do not change the driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""
