
import random
from multiprocessing import Process, Queue


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
    
    tmp = P.union(X)
    if len(tmp) > 0:
        u = random.sample(tmp, 1)[0]
        N_u = set(G[u])
        for v in list(P.difference(N_u)):
            N_v = set(G[v])
            max_sets = BKPivot(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
            P.remove(v)
            X.add(v)
        
    return max_sets

def BKOrderByDegree(R, P, X, G, max_sets, rs):
    vs_by_degree = sorted(G, key=lambda k: len(G[k]), reverse=True)
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
        max_sets = BKPivot(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)
        
    return max_sets

def BKWorker(queue, R, P, X, G, max_sets):
    if len(P) == 0 and len(X) == 0:
        max_sets.append(R)
    
    for v in list(P):
        N_v = set(G[v])
        max_sets = BKPivot(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)
        
    queue.put(max_sets)

def BKMultiProcess(R, P, X, G, max_sets):
    max_processes = 100
    q = Queue()
    jobs = []
    rets = []

    for v in list(P):
        N_v = set(G[v])
        if len(jobs) < max_processes:
            p = Process(target=BKWorker, 
                args=(q, R.union(set({v})), P.intersection(N_v), 
                      X.intersection(N_v), G, max_sets,))
            jobs.append(p)
            p.start()
        else:
            max_sets = BK(R.union(set({v})), P.intersection(N_v), X.intersection(N_v), G, max_sets)
        P.remove(v)
        X.add(v)

    for j in jobs:
        ret = q.get()
        max_sets.extend(ret)
    for j in jobs:
        j.join()

    return max_sets
