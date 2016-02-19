# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Parker Folkman & Kevin Ripley
# Last Modified: January 31, 2016
# ----------------------------------------------
# For our strategy we implemented a shelving type of algorithm with no sorting.
#We obtain the biggest height to make the ceiling and the floor of the next level.
#We stack all the random rectangles side by side. We used a fixed amount
#of 16 rows. 
# ----------------------------------------------
from operator import mul

def find_my_solution (rectangles):
    #Get the length of the list
    length = len(rectangles)
    lengthBySixteen = length//16
    
    placement = []
 
    upper_left_x = 0
    upper_left_y = 0
    current_height = 0
    count = 0

    #Get the maximum length to set the row height
    longest_box = max(rectangles,key=lambda x:x[1])
    left_y = longest_box[1]
    
    #Use 16 fixed size rows
    #Get the length of each section
    sec1 = lengthBySixteen
    sec2 = lengthBySixteen*2
    sec3 = lengthBySixteen*3
    sec4 = lengthBySixteen*4
    sec5 = lengthBySixteen*5
    sec6 = lengthBySixteen*6
    sec7 = lengthBySixteen*7
    sec8 = lengthBySixteen*8
    sec9 = lengthBySixteen*9
    sec10 = lengthBySixteen*10
    sec11 = lengthBySixteen*11
    sec12 = lengthBySixteen*12
    sec13 = lengthBySixteen*13
    sec14 = lengthBySixteen*14
    sec15 = lengthBySixteen*15
    sec16 = length
    
    for box in rectangles:#iterate through all the rectangles list and obtain the box tuples
      width = box[0]
      height = box[1]
      
      coordinate = (upper_left_x, upper_left_y)
      placement.insert(0, coordinate)   # insert tuple at front of list

      if(count < sec1): #Stack boxes in first shelf
         upper_left_x = upper_left_x + width
         upper_left_y = current_height 
         count += 1
      elif(count == sec1):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec1 and count<sec2):#Stack boxes in second shelf
          upper_left_x = upper_left_x + width
          upper_left_y = current_height
          count += 1
      elif(count == sec2):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec2 and count<sec3):#Stack boxes in third shelf
          upper_left_x = upper_left_x + width
          upper_left_y = current_height
          count += 1
      elif(count == sec3):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec3 and count<sec4):#Stack boxes in fourth shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec4):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec4 and count<sec5):#Stack boxes in fifth shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec5):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec5 and count<sec6):#Stack boxes in sixth shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec6):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec6 and count<sec7):#Stack boxes in seventh shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec7):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec7 and count<sec8):#Stack boxes in eighth shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
    #------------8 more rows---------------
      elif(count == sec8):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec8 and count<sec9):#Stack boxes in ninth shelf
          upper_left_x = upper_left_x + width
          upper_left_y = current_height
          count += 1
      elif(count == sec9):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec9 and count<sec10):#Stack boxes in tenth shelf
          upper_left_x = upper_left_x + width
          upper_left_y = current_height
          count += 1
      elif(count == sec10):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec10 and count<sec11):#Stack boxes in eleventh shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec11):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec11 and count<sec12):#Stack boxes in 12th shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec12):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec12 and count<sec13):#Stack boxes in 13th shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec13):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec13 and count<sec14):#Stack boxes in 14th shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec14):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec14 and count<sec15):#Stack boxes in 15th shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      elif(count == sec15):#Makes new shelf
          upper_left_x = 0
          current_height = current_height-left_y
          upper_left_y = current_height
          count += 1
      elif(count > sec15 and count<sec16):#Stack boxes in 16th shelf
          upper_left_y = current_height
          upper_left_x = upper_left_x + width  
          count += 1
      
    placement.reverse()
    return placement

#------END of Find Solution---------------

#Function gets called
def find_solution(rectangles):
    return find_my_solution(rectangles)  # a working example!
