# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Parker Folkman
# Last Modified: January 31, 2016
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

def find_my_solution (rectangles):
    length = len(rectangles)
    placement = []
    upper_left_x = 0
    upper_left_y = 0

#-------------------ID The Boxes-------------------------------------
    #ID the boxes. Stores in new list
    #Stores in format: (Unique ID, index location in list)
    initial_placement = []
    for i in range(length):
        temp = id(rectangles[i])
        initial_placement.append((temp,i))
#-------------------Sort The Boxes-----------------------------------
    #Make a new list of sorted boxes
    sorted_rectangles = sortByArea(rectangles)


    for box in sorted_rectangles:
        width = box[0]
        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.append(coordinate)             # insert tuple at back of list
        upper_left_x = upper_left_x + width

    return placement


#These two functions sort the tuples based on area (w*h)
def f(R):
    return R[0]*R[1]
def sortByArea(rectangles):
	return sorted(rectangles,key=f,reverse=True)

def find_solution(rectangles):
    return find_my_solution(rectangles)  # a working example!




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
