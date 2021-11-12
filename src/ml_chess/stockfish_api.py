from stockfish import Stockfish

fish = Stockfish()

def get_best_move():
    return fish.get_best_move()

def make_move(move):
    fish.make_moves_from_current_position([move])

def get_fish():
    return fish

'''
INPUT:
    Array:
        Mappings (indices 0 -> 63: board position):
            -1 -> empty spot
            0 -> white pawn (p)
            1 -> white rook (r)
            2 -> white knight (n)
            3 -> white bishop (b)
            4 -> white king (k)
            5 -> white queen (q)
            6 -> black pawn (P)
            7 -> black rook (R)
            8 -> black knight (N)
            9 -> black bishop (B)
            10 -> black king (K)
            11 -> black queen (Q)

        Mappings (index 64: piece to move col):
            0 -> a
            1 -> b
            3 -> c
            4 -> d
            5 -> e
            6 -> f
            7 -> g
            
        Mappings (index 65: piece to move row):
            0 -> 1
            1 -> 2
            2 -> 3
            3 -> 4
            4 -> 5
            5 -> 6
            6 -> 7
            7 -> 8

        Mappings (index 66: move to spot col):
            Same as index 64

        Mappings (index 67: move to spot row):
            Same as index 65

OUTPUT:
    0 -> good move
    1 -> bad move
'''
def get_input_output(move):
    mappings = {
        'p': 0,
        'r': 1,
        'n': 2,
        'b': 3,
        'k': 4,
        'q': 5,
        'P': 6,
        'R': 7,
        'N': 8,
        'B': 9,
        'K': 10,
        'Q': 11
    }

    move_mappings = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    input_list = list()
    position = get_board().split(' ')[0]
    rows = position.split('/')

    for row in rows:
        for spot in row:
            try:
                spot_int = int(spot)
                for _ in range(spot_int):
                    input_list.append(-1)
            except ValueError:
                input_list.append(mappings[spot])
    input_list.append(move_mappings[move[0]])
    input_list.append(int(move[1]))
    input_list.append(move_mappings[move[2]])
    input_list.append(int(move[3]))
    
    out = 1
    if is_best_move(move):
        out = 0

    return input_list, out

def is_best_move(move):
    return move == get_best_move()

def get_board():
    return fish.get_fen_position()

def set_board(position):
    fish.set_fen_position(position)

def rate_position():
    return fish.get_evaluation()

def reset():
    global fish
    fish = Stockfish()
