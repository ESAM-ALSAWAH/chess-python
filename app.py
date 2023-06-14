from flask import Flask, flash, jsonify, redirect, render_template, request, send_from_directory, session, url_for
import chess 

from helper import usingAlpha_betaMinMaxL,usingAlpha_MinMaxbest
app = Flask(__name__)
app.secret_key = 'mysecretkey'

n_moves=0

@app.route('/')
def reset():
    session.clear()
    return redirect(url_for('play'))


@app.route('/finish')
def finish():
    session.clear()
    global n_moves
    n_moves = 0
    global L
    L = 2
    return redirect(url_for('play'))

@app.route('/play')
def play():
    fen = session.get('fen', chess.STARTING_FEN)
    board = chess.Board(fen)
    return render_template('index.html', fen=fen, board=board)



@app.route('/move')
def move():
    global n_moves  
    move_str = request.args.get('name')
    fen = session.get('fen', chess.STARTING_FEN)
    board = chess.Board(fen)
    if board.is_game_over():
        return redirect(url_for('play'))
    try:
        move = chess.Move.from_uci(move_str)
        if move in board.legal_moves:
            if board.turn == chess.WHITE:
                board.push(move)
                fen = board.fen()
                session['fen'] = fen  # Save the FEN in the session
                n_moves += 1  # Increment the move count

            # Compute the computer's move using alpha-beta Minimax
            if  board.turn == chess.BLACK:
                # response= usingAlpha_betaMinMaxL(board,n_moves)
                response= usingAlpha_MinMaxbest(board,n_moves)
                return(jsonify(response))
         
        else:
            raise ValueError('Illegal move')
    except ValueError:
        flash(f'Invalid move: {move_str}')
    print(board)
    return redirect(url_for('play'))



@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)