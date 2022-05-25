#creating my board taking this off random image from google tbh
# board solution https://www.researchgate.net/figure/Solution-of-the-sample-Sudoku-board-shown-in-Figure-1-5_fig2_256169416

board = [
[0,0,0,7,9,0,0,5,0],
[3,5,2,0,0,8,0,4,0],
[0,0,0,0,0,0,0,8,0],
[0,1,0,0,7,0,0,0,4],
[6,0,0,3,0,1,0,0,8],
[9,0,0,0,8,0,0,1,0],
[0,2,0,0,0,0,0,0,0],
[0,4,0,5,0,0,8,9,1],
[0,8,0,0,3,7,0,0,0]
]


def board_print(bo):

    for i in range(len(bo)): # defines steps of function from rows (0,9)
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0 :
                print(" | ", end="") 

            if j == 8:              # this is the final line as 0 - 8 is 1-9 0=1 in this case
                print(bo[i][j])  # no need for an added space " " 
            else:
                print(str(bo[i][j]) + " ", end="")

#board_print(board)

def find_empty_square(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0
