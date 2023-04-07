Tower of Hanoi

The Tower of Hanoi is a classic mathematical puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:

    Only one disk may be moved at a time.
    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    No disk may be placed on top of a disk that is smaller than it.

Usage

In this repository, you can find a Python implementation of the Tower of Hanoi puzzle, with a command line interface.

To run the program, simply execute python Hanoi_Towers.py in your terminal.
Running the Program

When you run the program, you'll be prompted to enter the source rod, destination rod, and disk number for each move. The program will then make the move if it is valid, and update the state of the game.
Win Condition

The game ends when all the disks have been moved to the destination rod, in ascending order of size. At this point, the program will print a "You have won!" message.

Enjoy the game!




```python
# disks stacked on one rod in order of decreasing size, the smallest at the top
Towers = [[5, 4, 3, 2, 1],
    [],
    []
]

def move(n, source, target, auxiliary):
    """
    Move the top n disks from source tower to target tower, using auxiliary tower as buffer.
    """
    if n > 0:
        move(n-1, source, auxiliary, target)
        disk = Towers[source].pop()
        Towers[target].append(disk)
        print("Move disk", disk, "from", source, "to", target)
        move(n-1, auxiliary, target, source)

def solve():
    """
    Solve the Tower of Hanoi puzzle with the given number of disks.
    """
    num_disks = len(Towers[0])
    print("Starting Towers:", Towers)
    move(num_disks, 0, 2, 1)
    print("Ending Towers:", Towers)

solve()