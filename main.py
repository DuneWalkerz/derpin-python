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

def solve(bo):
    
    find = find_empty_square(bo)
    if not find:
        return True
    else:
        row, col = find # sets row,col to the location of an empty square

    for i in range (1,10): 
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False


# co_ordinate in this case is an (x,y) cordinate value for defineing look location. this will validate if the num at that square is valid by cheaking row, col and 3 x 3 square
#numeral is value being tested
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    #when using // it tells you the remaider integer eg 6//3 = 2 0-2 = 0 3-5 = 1 6-8 = 2 this lest you find the quadrent
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True



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
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

board_print(board)
solve(board)
print("___________________")
board_print(board)