import stockfish_api
from sklearn import tree
from chess import Board, Move
import random

board = Board()
features = list()
labels = list()

for i in range(200):
    if i % 25 == 0:
        board.reset()
        stockfish_api.reset()

    next_move = str(stockfish_api.get_best_move())
    for move in board.legal_moves:
        rand = random.randint(1, 100)
        if rand <= 50:
            next_move = str(move)
        feat, label = stockfish_api.get_input_output(str(move))
        features.append(feat)
        labels.append(label)

    board.push(Move.from_uci(next_move))
    stockfish_api.make_move(next_move)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

for _ in range(20):
    next_move = str(stockfish_api.get_best_move())
    for move in board.legal_moves:
        rand = random.randint(1, 100)
        if rand <= 50:
            next_move = str(move)
        feat, label = stockfish_api.get_input_output(str(move))
        prediction = clf.predict([feat])
        if (label == 0):
            print(prediction[0] == label, prediction[0])

    board.push(Move.from_uci(next_move))
    stockfish_api.make_move(next_move)
    
