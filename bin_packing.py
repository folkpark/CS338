# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Parker Folkman
# Last Modified: January 31, 2016
# ----------------------------------------------
#
#
#
# ----------------------------------------------

from operator import mul
#import functools

def find_my_solution (rectangles):
    length = len(rectangles)
    placement = []
    initial_placement = []
    upper_left_x = 0
    upper_left_y = 0
    left_x = 0
    left_y = 0
    temp = 0
    count = 0
    index = 0
    #ID the boxes. Stores in new list
    #Stores in format: (Unique ID, index location in list)
    for i in range(length):
        temp = id(rectangles[i])
        initial_placement.append((temp,i))
    
    sorted_widths = sortByWidth(rectangles)
    
    for box in sorted_widths:
      width = box[0]
      height = box[1]
      boxID = id(box)
      original_index = getIndex(boxID, initial_placement)
      coordinate = (upper_left_x, upper_left_y, index)
      placement.insert(index, coordinate)   # insert tuple at front of list
      left_y = max(sorted_widths)[1]
     
      if (len(sorted_widths) <= len(sorted_widths)/2):
          upper_left_x = upper_left_x + width
          upper_left_y = 0
      elif(len(sorted_widths) > len(sorted_widths)/2):
          upper_left_x = 0
          upper_left_y = left_y
          count+=1
          if(count >1):
              upper_left_x = upper_left_x + width
    placement = sortBack(placement)
    return placement
#------------------------------------------------------------------------------

'''
def stackBoxes(sorted_rectangles): #count needs to be initialized to zero before being passed
    placement = []
    length = len(sorted_rectangles)
    loopCount = 0 #Each loop adds a box to the bin and adds 1 to the count
    while(loopCount<length):#while there are boxes left to be placed
        
        
        while(row length < upper_left_x): #
            #y=const. Row Stacking
            boxWidth = box[0] #define width of the box to be placed
            
            index = getIndex(boxID, initial_placement)#get original index of the box
            coordinate = (upper_left_x, upper_left_y,index) #make a tuple w/ index
            placement.insert(index, coordinate)
            upper_left_x = upper_left_x + boxWidth
            loopCount = loopCount+1 #Add 1 to loop count
        
        while(col hight < upper_left_y): #
            #x=const. Column Stacking
            height = box[1]
            
            index = getIndex(boxID, initial_placement)
            coordinate = (upper_left_x, upper_left_y,index) #make a tuple
            placement.insert(index, coordinate)
            upper_left_y = upper_left_y + height # ????
            loopCount = loopCount+1 #Add 1 to loop count
            
    return placement
'''


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

#Function gets called
def find_solution(rectangles):
    return find_my_solution(rectangles)  # a working example!
