1. Maximum Index
There is an infinite array of integers numbered consecutively from 0. At each step, a pointer can move from index i to index i + j, or remain where it is. The value of i begins at 0. The value of j begins at 1 and at each step, j increments by 1. There is one known index that must be avoided. Determine the highest index that can be reached in a given number of steps.
Example
steps = 4
badElement = 6
The pointer is limited to 4 steps and should avoid the bad item 6.
    Scenario 1:
    In the first step, jstarts at 7. Move / unit to
index 0 + 1 = 1 and j= 2.
    At step 2, move 2 units to index 1 + 2 = 3, a = 3
    Al step 3, do not move. Otherwise