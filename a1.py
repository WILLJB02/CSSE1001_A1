from a1_support import *

def create_cell(cell_contents, row_number, column_number):
    """Creates a string which represents a cell in the game grid based on its
    location within the game grid.

    Parameters:
        cell_contents (str or int): Character to be displayed within the cell. 
        row_number (int): Row number of the cell within the game grid.
        column_number (int): Column number of the cell within the game grid. 

    Returns:
        (str): string which represents a cell within the game grid. 
    """
    
    if row_number == 0 and column_number >= 10:
        cell = ' ' + str(cell_contents) + WALL_VERTICAL

    elif column_number == 0:
        cell = str(cell_contents) + ' ' + WALL_VERTICAL
        
    else:
        cell = ' ' + str(cell_contents) + ' ' + WALL_VERTICAL
        
    return cell




def horizontal_boundary(grid_size):
    """ Creates string based on the grid size which represents the horizonatal
    wall between rows of the game grid. 
        
    Parameters:
 	grid_size (int): an integer representing the size of the game grid. 
 		
    Returns:
 	(str): a string representing the horizinal wall between rows of the game grid. 
    """
    
    horizontal_boundary = (4 + grid_size * 4)* WALL_HORIZONTAL
    return horizontal_boundary



def create_row(game, row_number, grid_size):
    """ Creates a string which represents a row in the game grid.

    Paramters:
        grid_size (int): an integer representing the size of the game grid. 
        row_number (int): row number of the row within the game grid.
        game (str): A string which represents each cells contents in the game.

    Returns:
        (str):  A string which represents a row of the game grid. 
    """
    
    column_number = 0
    
    if row_number == 0:
        row = create_cell(' ', row_number, column_number)
        column_number = 1

        #loop which places column number's in each cell of the inital row.
        while column_number <= grid_size:
            row += create_cell(column_number, row_number, column_number)
            column_number += 1
            
    else:
        row_letter = ALPHA[row_number - 1]
        row = create_cell(row_letter, row_number, column_number)
        column_number = 1

        #loop places game string char's in the corresponding cells of specified row. 
        while column_number <= grid_size:
            index = (row_number-1) * grid_size + (column_number-1)
            row += create_cell(game[index], row_number, column_number)
            column_number += 1
            
    return row



    
def display_game(game, grid_size):
    """Prints out a grid-shaped representation of the game given the game string
    and the grid size as arguments. 

    Paramters:
        grid_size (int): an integer representing the size of the game grid. 
        game (str): A string which represents the cells in the game.
    """
    
    row_number = 0
    
    while row_number <= grid_size:
        print(create_row(game, row_number, grid_size))
        print(horizontal_boundary(grid_size))
        row_number += 1


    

def row_letter_2_game_row(row_letter):
    """Converts row letter to the corresponding position tuple row number
    within the grid.  eg: Converts A to 0

    Parameters:
        row_letter (str): The letter associted with a row in the game grid.

    Returns:
        (int): The number which represents the row of a cell in the game
            grid's position tuples. 
    """
    
    for row_number, letter in enumerate(ALPHA):
       if letter == row_letter:
        return row_number


def coordinate_2_position(Coordinate):
    """ Converts a coordinate of a cell in the game grid to a position tuple. 
    eg: Converts A3 to (0,2)

    Parameters:
        Cooridnate (Str): A string which represents a cell within the game grid
                        based on the row letter and column number diplayed by
                        the game grid [eg A12 = row A, column 12].

    Returns:
        (tuple <int, int>): A tuple representing the row and column position of
                            a cell within the game grid. 
    """
    
    row_letter = Coordinate[0]
    
    game_row = row_letter_2_game_row(row_letter)
    game_column = int(Coordinate[1:]) - 1
    
    position = (game_row, game_column)
    return position



    
def position_to_index(position, grid_size):
    """ Converts the row, column coordinate of a cell within the game grid to its
        corresponding index within the game string.

    Parameters:
        position (tuple <int, int>): a tuple representing the row and column
                                        position of a cell within the game grid.
        grid_size (int): an integer representing the size of the game grid.

    Return:
        (int): an integer representing the index of the cell in the game string. 
    """
    index = position[0] * grid_size + position[1]
    return index



def replace_character_at_index(game, index, char):
    """ Returns an updated game string with the specified character placed at
    the specified index in the game string.

    Paramters:
        game (str): A string which represents the cells in the game.
        index (int): An interger which indicates the position in the game string.
        char (int or str): character to replace exsisting charater at the specified index.

    Return:
        (str): An updated game string with the specified character placed at the specified
            index in the game string.
    """
    game = game[:index] + str(char) + game[index+1:]
    
    return game



    
def flag_cell(game, index):
    """Returns an updated game string after toggling the flag at the specified index in
    the game string.

    Parameter:
        game (str): A string which represents the cells in the game.
        index (int): An interger which indicates the position in the game string.

    Return:
        (sttr): An updated game string with the a flag toggled at the specified index.
    """
    
    if game[index] == FLAG:
        game = replace_character_at_index(game, index, UNEXPOSED)
        
    else:
        game = replace_character_at_index(game, index, FLAG)
        
    return game 


def index_in_direction(index, grid_size, direction):
    """ Takes in the index of a cell within the game string and returns the index
    correpsonding to an adjacent cell in the specified direction.
    
    If an invalid direction is input, or there is no cell in the specified direction,
    None will be returned.

    Parameters:
        index (int): An interger which indicates the position in the game string.
        grid_size (int): an integer representing the size of the game grid.
        direction (str): direction of adjacent cell. 

    Return:
        (int): index in game string of the adjacent cell in the specified direction. 
    """

    if direction == UP and index >= grid_size:
        index_neighbour = index - grid_size
        
    elif direction == DOWN and index <= grid_size*(grid_size-1)-1:
        index_neighbour = index + grid_size
        
    elif direction == RIGHT and (index+1) % grid_size != 0:
        index_neighbour = index + 1
        
    elif direction == LEFT and (index) % grid_size != 0:
        index_neighbour = index - 1
        
    elif direction == f"{UP}-{LEFT}" and index >= grid_size \
    and (index) % grid_size != 0:
        index_neighbour = index - grid_size - 1
        
    elif direction == f"{UP}-{RIGHT}" and index >= grid_size \
        and (index+1) % grid_size != 0:
        index_neighbour = index - grid_size + 1
        
    elif direction == f"{DOWN}-{LEFT}" and index <= grid_size*(grid_size-1)-1 \
        and (index) % grid_size != 0:
        index_neighbour = index + grid_size - 1
        
    elif direction == f"{DOWN}-{RIGHT}" and index <= grid_size*(grid_size-1)-1 \
        and (index+1) % grid_size != 0:
        index_neighbour = index + grid_size + 1
        
    else:
        index_neighbour = None
        
    return index_neighbour


def neighbour_directions(index, grid_size):
    """Determens all the indexes of cells neighbouring the index of a specified cell.

    Parameters:
        index (int): the position of a cell within the game string. 
        grid_size (int): an integer representing the size of the game grid.

    Returns:
        (list <int, ...>): a list containing the indexes of all neighbouring cells. 
    """
    neighbouring_indexes = []

    #loop checks all possible directions, and if valid, adds index to a list. 
    for direction in DIRECTIONS:
        if index_in_direction(index, grid_size, direction)!= None:
            neighbouring_indexes += [index_in_direction(index, grid_size, direction),]
            
    return  neighbouring_indexes
        

def number_at_cell(game, pokemon_locations, grid_size, index):
    """Returns the number of pokemon in cells neighbouring the cell at a specified index.

    Parameters:
        game (str): A string which represents the cells in the game.
        index (int): An interger which indicates the position in the game string.
        grid_size (int): an integer representing the size of the game grid.
        pokemon_locations (tuple <int, ...>): A tuple containing indexes where the pokemons are located.
        
    Return:
        (int): The number of pokemon in neighbouring cells. 
    """
    
    neighbouring_indicies = neighbour_directions(index, grid_size)
    neighbouring_pokemon = 0
    
    for pokemon_index in pokemon_locations:
        if pokemon_index in neighbouring_indicies:
                neighbouring_pokemon += 1
                
    return neighbouring_pokemon



def check_win(game, pokemon_locations):
    """Checks if a player has has located all the pokemon and therefore won the game.

    Paramters:
        game (str): A string which represents the cells in the game.
        pokemon_locations (tuple <int, ...>): A tuple containing indexes where the pokemons are located.

    Returns:
        (Bool): A boolean showing weather the player has won the game (true if player
                has won and false otherwise).
    """
    
    flag_locations = []
    number_of_pokemon_flagged = 0
    won_game = False
    
    #creates list of flag indexes
    for flag_index, character in enumerate(game):
        if character == FLAG:
            flag_locations += [flag_index,]

    #checks how many pokemon flagged       
    for pokemon_index in pokemon_locations:
        if pokemon_index in flag_locations:
            number_of_pokemon_flagged += 1

    #checks requirements to win game
    if number_of_pokemon_flagged == len(pokemon_locations) \
        and UNEXPOSED not in game and len(flag_locations) == len(pokemon_locations):
        won_game = True
        
    return won_game


def parse_position(action, grid_size):
    """Checks if the 'select a cell' input action is in a valid format and, if so,
    returns the position of this cell in a tuple.
    
    Returns None if the input action format is invalid. 

    Parameters:
        action (str): desired action to be completed on game.
        grid_size (int): an integer representing the size of the game grid.

    Return:
        (tuple <int, int>): A tuple representing the row and column position of the
                            inputted cell within the game grid.
    """

    #if statement checks all requirments of select cell action format
    if len(action) > 1 and action[0] in ALPHA and action[1:].isdigit() \
        and row_letter_2_game_row(action[0]) < grid_size and int(action[1:]) <= grid_size:
        position = coordinate_2_position(action)
        return position
    
    else:
        return None
    

def check_action_flag(action):
    """Checks if input action is to flag a cell. 

    Parameters:
        action (str): desired action to be completed on game.

    Returns:
        (Bool): A boolean showing weather the input action is to flag a cell
               (true if input action is to flag cell and false otherwise)

    """
    action_flag = False

    if action[0:2] == "f " and action[2] in ALPHA and action[3:].isdigit():
        action_flag = True
        
    return action_flag
        


def main():
    """ This function runs the Pokemon game.

    When main() is called it initally prompts the user to input the desired grid size
    and number of pokemon and subsequently display's the game based on these variables.
    
    It then asks the user to input an action, and if valid, completes this action on the
    game using the above defined functions.

    The game grid is then reprinted and another action is promoted.

    This continues in a loop until the player wins the game (by flagging all the
    pokemon locations and exposing all other cells) or loses the game (by exposing a
    cell with a pokemon in it).
    """
    
    grid_size = int(input('Please input the size of the grid: '))
    number_of_pokemons = int(input('Please input the number of pokemons: '))
    
    game = grid_size**2*UNEXPOSED
    pokemon_locations = generate_pokemons(grid_size, number_of_pokemons)
    
    won_game = False
    loss_game = False

    #loop prompting user to enter action and then executing action until game is won or lost. 
    while won_game == False and loss_game == False:
        
        display_game(game, grid_size)
        print()
        action = input('Please input action: ')
        
        #if, elif, else block validating and executing entered action.
        if action == "h":
                 print(HELP_TEXT)
                 
    
        elif action == "q":
                quit_response = input('You sure about that buddy? (y/n): ')
                
                if quit_response == 'y':
                    print('Catch you on the flip side.')
                    loss_game = True
                    
                elif quit_response == 'n':
                    print("Let's keep going.")
                    
                else:
                    print(INVALID)
                    
            
        elif action == ':)':
                print("It's rewind time.")
                game = grid_size**2*UNEXPOSED
                pokemon_locations = generate_pokemons(grid_size, number_of_pokemons)

       
        elif check_action_flag(action) == True and parse_position(action[2:], grid_size) != None:
                flag_coordinate = parse_position(action[2:], grid_size)
                flag_index = position_to_index(flag_coordinate, grid_size)
                game = flag_cell(game, flag_index)
                
                
        elif parse_position(action, grid_size) != None:
            
            coordinate = parse_position(action, grid_size)
            coordinate_index = position_to_index(coordinate, grid_size)

            #select cell action if cell contains pokemon(player losses)
            if game[coordinate_index] != FLAG and coordinate_index in pokemon_locations:
            
                for pokemons_index in pokemon_locations:
                    game = replace_character_at_index(game, pokemons_index, POKEMON)
                    
                display_game(game, grid_size)
                print("You have scared away all the pokemons.")
                loss_game = True

                
            #select cell action if cell does not contain pokemon (exposing cells)
            elif game[coordinate_index] != FLAG and coordinate_index not in pokemon_locations:

                num_neighbour_pokemon = number_at_cell(game, pokemon_locations, grid_size, coordinate_index)           
                game = replace_character_at_index(game, coordinate_index, num_neighbour_pokemon)

                visible_cells = big_fun_search(game, grid_size, pokemon_locations, coordinate_index)

                for cells in visible_cells:
                    if game[cells] != FLAG:
                        number_pokemon_neighbouring = number_at_cell(game, pokemon_locations, grid_size, cells)
                        game = replace_character_at_index(game, cells, number_pokemon_neighbouring)
                        
        else:
            print(INVALID)
            
        won_game = check_win(game, pokemon_locations)
        
        if won_game == True:
            display_game(game, grid_size)
            print('You win.')



def big_fun_search(game, grid_size, pokemon_locations, index):
 	"""Searching adjacent cells to see if there are any Pokemon"s present.

 	Using some sick algorithms.

 	Find all cells which should be revealed when a cell is selected.

 	For cells which have a zero value (i.e. no neighbouring pokemons) all the cell"s
 	neighbours are revealed. If one of the neighbouring cells is also zero then
 	all of that cell"s neighbours are also revealed. This repeats until no
 	zero value neighbours exist.

 	For cells which have a non-zero value (i.e. cells with neightbour pokemons), only
 	the cell itself is revealed.

 	Parameters:
 		game (str): Game string.
 		grid_size (int): Size of game.
 		pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
 		index (int): Index of the currently selected cell

 	Returns:
 		(list<int>): List of cells to turn visible.
 	"""
 	queue = [index]
 	discovered = [index]
 	visible = []
 	if game[index] == FLAG:
 		return queue
 	number = number_at_cell(game, pokemon_locations, grid_size, index)
 	if number != 0:
 		return queue
 	while queue:
 		node = queue.pop()
 		for neighbour in neighbour_directions(node, grid_size):
 			if neighbour in discovered or neighbour is None:
 				continue

 			discovered.append(neighbour)
 			if game[neighbour] != FLAG:
 				number = number_at_cell(game, pokemon_locations, grid_size, neighbour)
 				if number == 0:
 					queue.append(neighbour)
 			visible.append(neighbour)
 	return visible

if __name__ == "__main__":
    main()
