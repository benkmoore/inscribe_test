
from src.utils import BuildGraph
from src.bron_kerbosch import BK, BKPivot, BKPivotByDegree

def FindMaximalSets(rectangles, pivot = False, by_degree = False):
    R = set()
    X = set()
    G = BuildGraph(rectangles)
    P = set(G.keys())
    max_sets = []
    
    if pivot:
        return BKPivot(R, P, X, G, max_sets)
    elif by_degree:
        vs_by_degree = sorted(G, key=lambda k: len(G[k]))
        return BKPivotByDegree(R, P, X, G, max_sets, rectangles, vs_by_degree)
    else:
        return BK(R, P, X, G, max_sets)
