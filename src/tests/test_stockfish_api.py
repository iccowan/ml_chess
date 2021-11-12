from ml_chess import stockfish_api
from stockfish import Stockfish
from chess import Board, Move

'''
Test that the best move is actually a legal move
'''
def test_get_best_move():
    stockfish_api.reset()

    board = Board()
    best_move = stockfish_api.get_best_move()
    assert Move.from_uci(best_move) in board.legal_moves

    board = Board('r3kbnr/p1pb1p1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 b kq - 1 10')
    stockfish_api.set_board('r3kbnr/p1pb1p1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 b kq - 1 10')
    best_move = stockfish_api.get_best_move()
    assert Move.from_uci(best_move) in board.legal_moves

'''
Test that a move is made when we want it to be
'''
def test_make_move():
    stockfish_api.reset()
    stockfish_api.make_move('e2e3')
    assert stockfish_api.get_board() == 'rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1'

    stockfish_api.set_board('r3kbnr/p1pb1p1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 b kq - 1 10')
    stockfish_api.make_move('g8e7')
    assert stockfish_api.get_board() == 'r3kb1r/p1pbnp1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 w kq - 2 11'

'''
Test that there is really only one fish instance
being created
'''
def test_get_fish_singleton():
    fish1 = stockfish_api.get_fish()
    fish2 = stockfish_api.get_fish()
    assert fish1 == fish2

''' 
Test that the fish is an instance of Stockfish
'''
def test_get_fish_is_stockfish():
    fish = stockfish_api.get_fish()
    assert isinstance(fish, Stockfish)

'''
Test that we are able to get the board position and it is correct
'''
def test_get_board():
    stockfish_api.reset()
    assert stockfish_api.get_board() == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    stockfish_api.make_move('e2e3')
    assert stockfish_api.get_board() == 'rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1' 

    stockfish_api.set_board('r3kbnr/p1pb1p1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 b kq - 1 10')
    assert stockfish_api.get_board() == 'r3kbnr/p1pb1p1p/4q1p1/2ppP1Q1/8/2N1P3/PPP1NPPP/R1B2RK1 b kq - 1 10'

'''
Test that the fish will reset
'''
def test_reset():
    stockfish_api.make_move('e2e3')
    stockfish_api.reset()
    new_fish = Stockfish()
    assert new_fish.get_fen_position() == stockfish_api.get_board()

