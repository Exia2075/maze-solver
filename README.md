# Maze Solver (Python)

Recursive maze generator and animated solver built from scratch in Python.

---

## Overview

The program:

- Generates a fully connected maze using recursive depth-first search (DFS)
- Solves the maze visually using recursive backtracking
- Animates exploration and backtracking in real time
- Includes deterministic generation via seed support
- Is covered with unit tests

---

## Algorithms Used

### Maze Generation  
Depth-First Search (DFS) with randomized neighbor selection.

- Guarantees a valid maze  
- No isolated sections  
- Exactly one path between any two cells  

### Maze Solving  
Recursive backtracking.

- Explores valid paths  
- Visually backtracks from dead ends  
- Stops when reaching the goal cell  

---

## How to Run

Run the animation:

```bash
python main.py
