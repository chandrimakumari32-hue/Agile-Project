from flask import Flask, render_template, request

app = Flask(__name__)

# Game board
board = [""] * 9

# Current player
current_player = "X"

# Winner
winner = None


def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if "" not in board:
        return "Draw"

    return None


@app.route("/", methods=["GET", "POST"])
def home():
    global board, current_player, winner

    if request.method == "POST":

        # Reset game
        if "reset" in request.form:
            board = [""] * 9
            current_player = "X"
            winner = None

        # Make a move
        elif "position" in request.form and winner is None:

            position = int(request.form["position"])

            if board[position] == "":
                board[position] = current_player

                winner = check_winner()

                if winner is None:
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"

    return render_template(
        "index.html",
        board=board,
        current_player=current_player,
        winner=winner
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



