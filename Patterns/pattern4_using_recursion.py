def print_row(col, start):
    if col == 0:
        return
    print(start, end=" ")
    # Alternate between 1 and 0
    print_row(col - 1, 1 - start)

def print_pattern(rows, col, current_row=0):
    if current_row == rows:
        return
    # If current row is even (0-based), start with 1, else start with 0
    start = 1 if current_row % 2 == 0 else 0
    print_row(col, start)
    print()  # Move to next line
    print_pattern(rows, col, current_row + 1)

print_pattern(5,5)
