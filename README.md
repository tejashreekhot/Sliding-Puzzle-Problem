# Sliding-Puzzle-Problem
This a variant of the 15-puzzle with the following important changes:
First, instead of 15 tiles, there are 16, so that there are no empty spaces on the board. Second, instead of moving a single tile into an open space, a move in this puzzle consists of either 
(a) sliding an entire row of tiles left or right, with the left- or right-most tile “wrapping around” to the other side of the board, or 
(b) sliding an entire column of the puzzle up or down, with the top- or bottom-most tile “wrapping around.”

The goal of the puzzle is to find a short sequence of moves that restores the canonical configuration
(on the left above) given an initial board configuration.

We used A* search to solve this problem.

This code was awarded as the fastest code in "Elements of Artificial Intelligence" class of 65 MS and PhD students.
