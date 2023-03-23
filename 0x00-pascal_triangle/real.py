def pascal_triangle(n):
    """pascal's triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        rows = [1]
        for j in range(1, i):
            rows.append(triangle[i-1][j-1] + triangle[i-1][j])
        rows.append(1)
        triangle.append(rows)
    return triangle

def print_triangle(triangle):
    """Function to print triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
