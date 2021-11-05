from stockfish import Stockfish

fish = Stockfish()

def get_best_move():
    return fish.get_best_move()

def make_move(move):
    fish.make_moves_from_current_position([move])

def get_fish():
    return fish

def get_board():
    return fish.get_fen_position()
