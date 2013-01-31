## Game Plan
1. write up truth table, wire contents, state
2. write puzzle config
3. skeleton component, puzzle, board
4. skeleton calculator, boardfactory, render, inputhandler
5. finish component, puzzle
6. start boardfactory.generate
7. finish board
8. make usable boardfactory.generate
9. write console render
10. write main's generate board
11. test & refine using console render
12. write calculator
13. test calculator
14. finish generate
15. write save/load
16. write console input handler
17. write render for...webpage? maybe?
18. write input handler for what we did the render for
19. thoroughly bugtest
20. deploy

## Classes
#TruthTable
a truth table for each component. maps inputs to outputs
immutable, make a new one
[Serializable]
#WireContents
array of wire States, one for each tested input
is mutable
[Serializable]
#State
immutable, is enumerated
Either WHITE(0), YELLOW(1), or RED(2)
[Serializable]
#Component
immutable, but truth table can be changed
has reference to truth table
has reference to input components, unless is one of the input components
holds last computed result + timestamp
[Serializable]
#PuzzleConfig
no code, just data
defines the wire relations
[Serializable]
#Puzzle
gives list of allowed truth tables
knows what the fixed/extra pieces are
knows what the inputs and the goal are
holds the PuzzleConfig
[Serializable]
#Board
holds the Puzzle and all Components
knows the ordering of components
handles truth table swapping
[Serializable]
#Calculator
calculates the results of each component
 - needs only Board
 - generates WireContents and stores them in Components
stores a timestamp to know when to recalc
[Not Serializable]
#BoardFactory
creates, loads, and saves boards
 - only one allowed to create a Component object
 - called from main? maybe?
[Not Serializable]
#Render
Takes board and outputs something pretty
[Not Serializable]
#InputHandler
handles input
passes truthtable swaps to Board
[Not Serializable]
#Main
parses args
 - create board and save
 - create board and play
 - load board and play

