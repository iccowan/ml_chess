from stockfish import Stockfish

stockfish = Stockfish("/Users/zhelyabuzhsky/Work/stockfish/stockfish-9-64")

fish = Stockfish()

def get_best_move(fish):
    return fish.get_best_move()

def get_fish():
    return fish
