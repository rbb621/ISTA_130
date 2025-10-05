'''
Pseudocode for tic-tac-turtle (or any game)
'''
initial setup                   # make the turtle, set its attributes
while playing:                  # each iteration is one game
    setup that happens once each game # draw board, initialize variables
    while not game over:        # each iteration one turn per player
        do turns
    play another?

'''
More complex pseudocode for tic-tac-turtle.  This is a nice
size for main.  After this, you want to start filling
in with functions.
'''
initial setup                   # make the turtle, set its attributes
while playing:                  # each iteration is one game
    setup that happens once each game # draw board, initialize variables
    while not game over:        # each iteration one turn per player
        x takes a turn
        if not x wins:
            o takes a turn
            if not o wins:
                continue loop
            else:
                game over = True
        else:
            game over = True
    game is over - play another?
    if not:
        playing = False        # outer loop ends
