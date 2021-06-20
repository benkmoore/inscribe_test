
import random

def BK(R, P, X, G, max_sets):
    if len(P) == 0 and len(X) == 0:
        max_sets.append(R)
    
    for v in list(P):
        N_v = set(G[v])
        max_sets = BK(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)
        
    return max_sets

def BKPivot(R, P, X, G, max_sets):
    if len(P) == 0 and len(X) == 0:
        max_sets.append(R)
    
    u = random.sample(P.union(X), 1)[0]
    N_u = set(G[u])
    for v in list(P.difference(N_u)):
        N_v = set(G[v])
        max_sets = BK(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)
        
    return max_sets

def BKPivotByDegree(R, P, X, G, max_sets, rs, vs_by_degree):
    if len(P) == 0 and len(X) == 0:
        max_sets.append(R)
        
    tmp = P.union(X)
    i = 0
    while True:
        if vs_by_degree[i] in tmp:
            u = vs_by_degree[i]
            break
        i += 1
    del vs_by_degree[i]

    N_u = set(G[u])
    for v in list(P.difference(N_u)):
        N_v = set(G[v])
        max_sets = BK(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)
        
    return max_sets
