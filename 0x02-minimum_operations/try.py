def pascal_triangle(n):
    if n <= 0:
        return 0
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    for row in triangle:
        print('[{}]'.format(','.join([str(x) for x in row])))

print_triangle(pascal_triangle(5))


def minOperations(n):
    if n == 1:
        return 0
    factor = 2
    operations = 0
    while factor * factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1
    if n > 1:
        operations += n
    return operations

n = 4
print('Minumum number of operation to reach {} char: {}'.format(n, minOperations(n)))
n = 12
print('Minimum number of operations to reach {} char: {}'.format(n, minOperations(n)))
n = 37
print('Minimum number of operations to reach {} char: {}'.format(n, minOperations(n)))
