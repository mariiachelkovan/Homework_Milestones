def get_triangle(rows):
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))


if __name__ == "__main__":
    rows = input("Enter the number of rows: ")

    try:
        rows = int(rows)
    except ValueError:
        print("Please provide a valid integer for the number of rows.")
        exit(1)

    triangle = get_triangle(rows)
    print_triangle(triangle)
