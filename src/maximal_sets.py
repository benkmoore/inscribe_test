
from src.utils import *
from src.bron_kerbosch import BK, BKPivot, BKOrderByDegree, BKMultiProcess


##-------------- BK search algos ---------------##
def FindMaximalSets(rectangles, pivot = False, by_degree = False, multi_process = False):
    R = set()
    X = set()
    G = BuildGraph(rectangles)
    P = set(G.keys())
    max_sets = []
    
    if pivot:
        return BKPivot(R, P, X, G, max_sets)
    elif by_degree:
        return BKOrderByDegree(R, P, X, G, max_sets, rectangles)
    elif multi_process:
        return BKMultiProcess(R, P, X, G, max_sets)
    else:
        return BK(R, P, X, G, max_sets)
