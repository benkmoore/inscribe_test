import os
import numpy as np
from bisect import bisect_right, bisect_left

from src.rectangle import UUIDRectangle


##-------------- Rectangle Operation Utils ---------------##
def IntersectingRectanglesByAxis(curr, rectangles, axis, dimension):
    rectangles.sort(key=lambda r: getattr(r, axis) + getattr(r, dimension))
    upper_right_corners = [getattr(r, axis) + getattr(r, dimension) for r in rectangles] 
    idx = bisect_right(upper_right_corners, getattr(curr, axis))
    rectangles = rectangles[max(0,idx):]

    rectangles.sort(key=lambda r: getattr(r, axis))
    lower_left_corners = [getattr(r, axis) for r in rectangles] 
    idx = bisect_left(lower_left_corners, getattr(curr, axis) + getattr(curr, dimension))
    rectangles = rectangles[0:min(idx, len(rectangles))]
        
    return rectangles

def GetIntersectingRectangles(curr, rectangles):
    rectangles = IntersectingRectanglesByAxis(curr, rectangles, 'x', 'width')
    rectangles = IntersectingRectanglesByAxis(curr, rectangles, 'y', 'height')
    
    return rectangles

##-------------- Data Utils ---------------##
def CreateRectanglesFromData():
    rectangles = []
    data = np.loadtxt(os.getcwd() + '/data/rectangles.txt')

    for i in range(0, data.shape[0]):
        rectangle = UUIDRectangle(data[i,0], data[i,0], data[i,0], data[i,0], i)
        rectangles.append(rectangle)
    
    return rectangles

def BuildGraph(rectangles):
    G = {}
    for r in list(rectangles):
        G[r.uuid] = []
        intersects = GetIntersectingRectangles(r, rectangles)
        for i in intersects:
            if i.uuid == r.uuid: continue
            G[r.uuid].append(i.uuid)
                
    return G


##-------------- Print Utils ---------------##
def PrintMaximalSet(maximal_set):
    for i, rectangle in enumerate(maximal_set):
        if i < len(maximal_set) - 1:
            print("{}, ".format(rectangle.uuid), end = '')
        else: 
            print("{}".format(rectangle.uuid), end = '')
            
def PrintMaximalSets(maximal_sets):
    for maximal_set in sorted(maximal_sets, key=len, reverse=True):
        PrintMaximalSet(maximal_set)
        print('')
