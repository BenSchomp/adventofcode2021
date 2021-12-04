
SIZE = 5
NO_BINGO = -1

# ----------------------------
class Board:
    def __init__( self, new_grid ):
        self.grid = new_grid
        self.bingo = False

    def __str__( self ):
        out = ''
        for row in self.grid:
            out += ' '.join( row ) + "\n"
        return out

    def has_bingo( self ):
        return self.bingo

    def check_for_bingo( self ):
        total_sum = 0
        found_bingo = False
        column_bingo = [True]*SIZE
        for row in self.grid:
            column = 0
            row_bingo = True
            for number in row:
                if number != 'X':
                    total_sum += int(number)
                    row_bingo = False
                    column_bingo[column] = False
                column += 1

            if row_bingo:
                found_bingo = True

        if True in column_bingo:
            found_bingo = True

        if found_bingo:
            self.bingo = True
            return total_sum

        return NO_BINGO

    def mark( self, number ):
        row_count = 0
        for row in self.grid:
            if number in row:
                self.grid[row_count][ row.index(number) ] = 'X'
                return self.check_for_bingo()
            row_count += 1
        return NO_BINGO

# ----------------------------
def part_one(boards, called_numbers):
    for number in called_numbers:
        for board in boards:
            remaining_sum = board.mark( number )
            if remaining_sum != NO_BINGO:
                print( "Bingo!", remaining_sum, '*', number, '=', remaining_sum*int(number))
                return

def part_two(boards, called_numbers):
    for number in called_numbers:
        for board in boards:
            remaining_sum = board.mark( number )
            if remaining_sum != NO_BINGO:
                # found a bingo ... but is it the LAST bingo?
                done = True
                for check_board in boards:
                    if not check_board.has_bingo():
                        done = False
                        break

                if done:
                    print( "Last Bingo:", remaining_sum, '*', number, '=', remaining_sum*int(number))
                    return

# ----------------------------
def main():
    file = open('day-04.txt', 'r')
    called_numbers = None
    board_array = []
    boards = []
    for line in file:
        line = line.strip()
        if  not called_numbers:
            called_numbers = line.split(',')
            continue

        if len(line) == 0:
            if len(board_array) == 0:
                continue
            new_board = Board( board_array )
            boards.append( new_board )
            board_array = []
        else:
            current_row = line.split()
            board_array.append(current_row)
    file.close()

    part_one(boards, called_numbers)
    part_two(boards, called_numbers)

if __name__ == "__main__":
    main()
