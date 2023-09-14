#tic tak toe

#classes
class board:
    def __init__(self):
        self.layout = [['-' for i in range(3)] for i in range(3)]
        
        
    def check_victory(self) -> tuple[bool, int]:
        #check horizontal
        victory = False
        spaces_left = 0
        
        for row in self.layout:
            if row[0] == row[1] == row[2] and '-' not in row:
                victory = True
        
        #check verticle
        for i in range(3):
            if self.layout[0][i] == self.layout[1][i] == self.layout[2][i] == 'O' or self.layout[0][i] == self.layout[1][i] == self.layout[2][i] == 'X':
                victory = True
        
        #check diagonal
        if self.layout[0][0] == self.layout[1][1] == self.layout[2][2] == 'X' or self.layout[0][0] == self.layout[1][1] == self.layout[2][2] == 'O':
            victory = True
        if self.layout[0][2] == self.layout[1][1] == self.layout[2][0] == 'X' or self.layout[0][2] == self.layout[1][1] == self.layout[2][0] == 'O':
            victory = True
            
        #check if board is empty
        for row in self.layout:
            for item in row:
                if item == '-':
                    spaces_left += 1
                    
        return victory, spaces_left
            
    def display(self):
        displayed_board = '  | 0 | 1 | 2\n0 | {0} | {1} | {2}\n1 | {3} | {4} | {5}\n2 | {6} | {7} | {8}'
        board_values = []
        for i in range(3):
            for j in range(3):
                board_values.append(self.layout[i][j])
        
        displayed_board = displayed_board.format(*board_values)
        print(displayed_board)
        
        
    def update_board(self,item: str, x, y):
        if item != 'O' and item != 'X':
            raise ValueError('Only O or X can be placed on board!')
        
        self.layout[x][y] = item
    
    def board_update_possible(self, x ,y) -> bool:
        #check board space is empty
        if self.layout[x][y] != '-':
            return False
        
        else:
            return True
 
#functions
def validate_coordinates(board):
    coordinates_valid = False
    
    while not coordinates_valid:
        print('Enter coordinates in the format: x y')
        coordinates = input('')
        
        try:
            x = int(coordinates[0])
            y = int(coordinates[2])
            
        except ValueError:
            print('Enter only numbers with a space in the middle!')
            continue
        
        if x < 0 or x > 2:
            print('X coordinate must be between 0-2')
            continue
        elif y < 0 or y > 2:
            print('Y coordinate must be between 0-2')
            continue
        
        if not board.board_update_possible(y, x):
            print('These coordinates have already been played!')
            continue
        
        coordinates_valid = True
        
    return x, y

        
#variables
game_board = board()
game_done = False
player_turn = 'O'

#main
print('Noughts and Crosses V1')

#game loop
while not game_done:
    game_board.display()
    
    player_name = 'noughts' if player_turn == 'O' else 'crosses'
    print(f'It is {player_name} turn')
    
    x, y = validate_coordinates(game_board)
    
    #switch coordinates around to coordinate system follow norms of graphing
    x, y = y, x
    
    game_board.update_board(player_turn, x, y)
    
    victory, spaces = game_board.check_victory()
    
    if victory:
        print(f'{player_name} is the winner!')
        game_done = True
        continue
    
    if spaces == 0:
        print('Game is a draw: no space left on board!')
        game_done = True
        continue
    
    #change turn of player
    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'


game_board.display()
        
        