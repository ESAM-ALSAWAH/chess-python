from flask import session
import time
from engine import alpha_betaMinMaxL,alpha_beta_MinMaxbest

L=2
k=5

start_time = time.time()

def usingAlpha_betaMinMaxL(board,n_moves):
    start = time.time()
    for move in board.legal_moves:
        best_score = float('+inf')
        board.push(move)
        score = alpha_betaMinMaxL(board, L, float('-inf') ,float('inf') , False)
        board.pop()
        if score < best_score:
            best_move = move
            best_score = score

    board.push(best_move)
    n_moves += 1  
    fen = board.fen()
    session['fen'] = fen  # Save the FEN in the session
    print(f"Time taken: {time.time() - start:.2f}s, Nodes searched: {n_moves}")
   

    return   {
        'move': str(best_move),
        'fen': fen,
        'n_moves': n_moves,
        'time': f"{time.time() - start:.2f}s",
        'nodes': n_moves
    } 




def usingAlpha_MinMaxbest(board,n_moves):
    start = time.time()
    best_move = None
   
    for move in board.legal_moves:
        best_score = float('+inf')
        board.push(move)
        score = alpha_beta_MinMaxbest(board, L,float('-inf') ,float('inf') , k, False)
        board.pop()
        if score < best_score:
            best_move = move
            best_score = score
    board.push(best_move)

    n_moves += 1
    fen = board.fen()
    session['fen'] = fen  # Save the FEN in the session
    print(f"Time taken: {time.time() - start:.2f}s, Nodes searched: {n_moves}")
    return  {
        'move': str(best_move),
        'fen': fen,
        'n_moves': n_moves,
        'time': f"{time.time() - start:.2f}s",
        'nodes': n_moves
    }
