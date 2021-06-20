# Inscribe AI: rectangles challenge

## Problem decomposition
1. Check intersection between two rectangles x and y.
2. Find all rectangles that intersect with rectangle x.
3. Find set of rectangles in which all members intersect each other, a complete graph.
4. Increase size of set until all other rectangles have been attempted to be added to set, a maximal set.
5. Attempt all combinations for each rectangle with all other rectangles to form largest (maximal) set.
6. If maximal set found compare to existing sets and store unique sets only.
7. Print maximal sets.

## Approach
- Represent as a graph where each rectangle is a vertex with intersections represented by edges.

## Bron Kerbosch (BK) search
- Recursion with backtracking.
- Time complexity is exponential: `O(3^(N/3))`, `N` = number of vertices in graph.

## Time complexity
- Handling exponential run time: can data structure be exploited?
- See [data exploration](data_exploration.ipynb)

## BK with pivot
- Reduce recursive calls to non-maximal sets by leveraging the fact that either the next vertex, `v` or one of it's non-neighbors will be part of the maximal set. We check if this is a maximal set prior to making the above decision.

## BK vertex ordering by degree
- Select outer level search vertices based on degree, `d`, largest first. Minimizes size of graph passed to subsequent recursive calls.
- For sparse graphs run time: `O(d*N*3^(d/3))`, however the graph appears quite densely connected.

## Appendix
- Resources:
    - https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    - https://snap.stanford.edu/class/cs224w-readings/tomita06cliques.pdf

