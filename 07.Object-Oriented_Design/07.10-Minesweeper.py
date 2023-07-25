'''
07.10 Minesweeper: Design and implement a text-based Minesweeper game. Minesweeper is the classic
    single-player computer game where an NxN grid has B mines (or bombs) hidden across the grid. The
    remaining cells are either blank or have a number behind them. The numbers reflect the number of
    bombs in the surrounding eight cells. The user then uncovers a cell. If it is a bomb, the player loses.
    If it is a number, the number is exposed. If it is a blank cell, this cell and all adjacent blank cells (up to
    and including the surrounding numeric cells) are exposed. The player wins when all non-bomb cells
    are exposed. The player can also flag certain places as potential bombs. This doesn't affect game
    play, other than to block the user from accidentally clicking a cell that is thought to have a bomb.
    (Tip for the reader: if you're not familiar with this game, please play a few rounds online first).

    This is a fully exposed board with 3
    bombs. This is not shown to the user.

    The player initially sees a board with
    nothing exposed.

    Clicking on cell (row= 1, col= O)
    would expose this:

    The user wins when everything other
    than bombs has been exposed.
'''