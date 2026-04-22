def minimax(depth, is_max):
    if depth == 3:
        return depth  # simple value

    if is_max:
        best = -100
        for i in range(2):
            val = minimax(depth + 1, False)
            best = max(best, val)
        return best
    else:
        best = 100
        for i in range(2):
            val = minimax(depth + 1, True)
            best = min(best, val)
        return best

print("Result:", minimax(0, True))


# Explanation:
# Minimax is used in games.
# MAX player tries to maximize value.
# MIN player tries to minimize value.
# We recursively explore all possibilities.