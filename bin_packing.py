 ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Parker Folkman & Kevin Ripley
# Last Modified: January 31, 2016
# ----------------------------------------------
# For our strategy we implemented a shelving type of algorithm with no sorting.
#We obtain the biggest height to make the ceiling and the floor of the next level.
#We stack all the random rectangles side by side.
#
# ----------------------------------------------
from operator import mul
#import functools

def find_my_solution (rectangles):
    length = len(rectangles)
    #take length of list and divide it by 8
    lengthByEight = length//8
    #cut list into sections for shelving algorithm
    sec1 = lengthByEight
    sec2 = lengthByEight*2
    sec3 = lengthByEight*3
    sec4 = lengthByEight*4
    sec5 = lengthByEight*5
    sec6 = lengthByEight*6
    sec7 = lengthByEight*7
    sec8 = length
    #local variables initialization
    placement = []
    initial_placement = []
    upper_left_x = 0
    upper_left_y = 0
    left_x = 0
    count = 0
    #using sorted_height to find the max height to use as boundary for shelving
    sorted_height = sortByHeight(rectangles)
    left_y = max(sorted_height[1])
    #making clones of list for each section
    clone_1 = rectangles
    section1 = clone_1[:sec1]
    section2 = clone_1[sec1:sec2]
    section3 = clone_1[sec2:sec3]
    section4 = clone_1[sec3:sec4]
    section5 = clone_1[sec4:sec5]
    section6 = clone_1[sec5:sec6]
    section7 = clone_1[sec6:sec7]
    section8 = clone_1[sec7:]
    
    for box in rectangles: # iterate through all the rectangles list and obtain the box tuples
      width = box[0]
      height = box[1]
      coordinate = (upper_left_x, upper_left_y)
      placement.insert(0, coordinate)   # insert tuple at front of list

      if(count < sec1): #Stack boxes in first shelf
         upper_left_x = upper_left_x + width
         upper_left_y = 0 
         count += 1
      elif(count == sec1):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y
          count += 1
      elif(count > sec1 and count<sec2):#Stack boxes in second shelf
          upper_left_x = upper_left_x + width
          upper_left_y = left_y
          count += 1
      elif(count == sec2):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*2
          count += 1
      elif(count > sec2 and count<sec3):#Stack boxes in third shelf
          upper_left_x = upper_left_x + width
          upper_left_y = left_y*2
          count += 1
      elif(count == sec3):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*3
          count += 1
      elif(count > sec3 and count<sec4):#Stack boxes in fourth shelf
          upper_left_y = left_y*3
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec4):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*4
          count += 1
      elif(count > sec4 and count<sec5):#Stack boxes in fifth shelf
          upper_left_y = left_y*4
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec5):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*5
          count += 1
      elif(count > sec5 and count<sec6):#Stack boxes in sixth shelf
          upper_left_y = left_y*5
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec6):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*6
          count += 1
      elif(count > sec6 and count<sec7):#Stack boxes in seventh shelf
          upper_left_y = left_y*6
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec7):#Makes new shelf
          upper_left_x = 0
          upper_left_y = left_y*7
          count += 1
      elif(count > sec7 and count<sec8):#Stack boxes in eighth shelf
          upper_left_y = left_y*7
          upper_left_x = upper_left_x + width  
          count += 1
    placement.reverse()
    return placement

#------END of Find Solution---------------



#This function takes in the boxes unique ID,
#and the initial_placement list and returns
#the orginal index (int) of where that box
#was found in the rectangles list
def getIndex(ID, initial_placement):
    for i in range(len(initial_placement)):
        tempRect = initial_placement[i] #Temporary rectangle
        tempID = tempRect[0] #temporary ID of that rect
        if(tempID==ID):
            index = tempRect[1]
            return index

#This function sorts the rectangles by height. It takes
#a list of tuples, unsorted, and returns those boxes
#sorted by height. Greatest -> smallest
def sortByHeight(rectangles):
    sorted_by_height = sorted(rectangles,key=lambda x: x[1])
    sorted_by_height.reverse()
    return sorted_by_height

#Function gets called
def find_solution(rectangles):
    return find_my_solution(rectangles)  

