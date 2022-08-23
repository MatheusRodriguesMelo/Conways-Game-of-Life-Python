from random import randint
from cell import cell

class board:
    def __init__(self, rows, columns):        
        self._columns = columns
        self._rows = rows
        self._grid = [[cell() for column_cells in range(self._columns)] for rows_cells in range(self._rows)]

        self.random_board()
    
    def board_draw(self):
        print('\n'*10)
        print('printing the board...')
        for row in self._grid:
            for column in row:
                print (column.cell_printer(), end='')
            print ()
    
    def random_board(self):
        for row in self._grid:
            for column in row:
                if randint(0,2) == 2:
                    column.alive()


    def check_near(self, check_row , check_column):

        search_min = -1
        search_max = 2
        neighbor_list = []
    
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbor_row = check_row + row
                neighbor_column = check_column + column 

                valid_neighbor = True

                if (neighbor_row) == check_row and (neighbor_column) == check_column:
                    valid_neighbor = False

                if (neighbor_row) < 0 or (neighbor_row) >= self._rows:
                    valid_neighbor = False

                if (neighbor_column) < 0 or (neighbor_column) >= self._columns:
                    valid_neighbor = False

                if valid_neighbor:
                    neighbor_list.append(self._grid[neighbor_row][neighbor_column])
        return neighbor_list


    
    def update_board(self):

        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbor pr. square:
                check_neighbor = self.check_near(row , column)
                
                living_neighbors_count = []

                for neighbor_cell in check_neighbor:
                    if neighbor_cell.checker():
                        living_neighbors_count.append(neighbor_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.checker()

                #If the cell is alive, check the neighbor status.
                if status_main_cell == True:
                    if len(living_neighbors_count) < 2 or len(living_neighbors_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbors_count) == 3 or len(living_neighbors_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbors_count) == 3:
                        goes_alive.append(cell_object)

        #sett cell statuses
        for cell_items in goes_alive:
            cell_items.alive()

        for cell_items in gets_killed:
            cell_items.dead()
