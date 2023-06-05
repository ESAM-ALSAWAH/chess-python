
import chess
# Evaluation function
def evaluate_board(board):
    # Count the material balance
    piece_values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5,
    chess.QUEEN: 9, chess.KING: 0}
    score = 0
    for square, piece in board.piece_map().items():
        value = piece_values[piece.piece_type]
        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value
    # Add bonuses/penalties based on piece positions
    for square, piece in board.piece_map().items():
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                score += 10 + (7 - chess.square_distance(square, chess.E2))
            elif piece.piece_type == chess.KNIGHT:
                score += 30 + len(board.attacks(square))
            elif piece.piece_type == chess.BISHOP:
                score += 30 + len(board.attacks(square))
            elif piece.piece_type == chess.ROOK:
                score += 50 + len(board.attacks(square))
            elif piece.piece_type == chess.QUEEN:
                score += 90 + len(board.attacks(square))
            elif piece.piece_type == chess.KING:
                score += 900 + len(board.attacks(square))
        else:
            if piece.piece_type == chess.PAWN:
                score -= 10 + (chess.square_distance(square, chess.E7))
            elif piece.piece_type == chess.KNIGHT:
                score -= 30 + len(board.attacks(square))
            elif piece.piece_type == chess.BISHOP:
                score -= 30 + len(board.attacks(square))
            elif piece.piece_type == chess.ROOK:
                score -= 50 + len(board.attacks(square))
            elif piece.piece_type == chess.QUEEN:
                score -= 90 + len(board.attacks(square))
            elif piece.piece_type == chess.KING:
                score -= 900 + len(board.attacks(square))
    return score


# Define the alpha-beta Minimax function
def alpha_betaMinMaxL(board, l, alpha, beta, maximizing_player):
    if l == 0 or board.is_game_over():
        return evaluate_board(board)
     
    score = float('inf')
    for move in board.legal_moves:
        board.push(move)
        score = min(score, alpha_betaMinMaxL(board.copy(), l-1, alpha, beta, False))
        board.pop()
        beta = min(beta, score)
        if alpha >= beta:
            break

    return score



def alpha_beta_MinMaxbest(board, L, alpha, beta, k, maximizing_player):
    if L == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta_MinMaxbest(board, L - 1, alpha, beta, k, True)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta_MinMaxbest(board, L - 1, alpha, beta, k, False)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

