

def checkio(game_result):
    b = game_result
    for x in range(3):
        if b[x][0] == b[x][1] == b[x][2]:
            return b[x][0]
        if b[0][x] == b[1][x] == b[2][x]:
            return b[0][x]
    if b[0][0] == b[1][1] == b[2][2]:
        return b[1][1]
    if b[2][0] == b[1][1] == b[0][2]:
        return b[1][1]
    return "D"


    return "D" or "X" or "O"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"