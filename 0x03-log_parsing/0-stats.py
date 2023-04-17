#!/usr/bin/python3
"""
this funtion reads stdin line by line and compute metrics
"""

import sys


def parse_log():
    count = 0
    file_size = 0
    pry_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    status_code_count = {}

    try:
        for line in sys.stdin:
            each = line.split()
            if len(each) < 2:
                continue
            try:
                count += 1
                file_size += int(each[-1:][0])
                status_code = int(each[-2:][0])
                if status_code in pry_status_code:
                    if status_code in status_code_count:
                        status_code_count[status_code] += 1
                    else:
                        status_code_count[status_code] = 1

                if count == 10:
                    count = 0
                    print_error(file_size, status_code_count)
            except ValueError:
                continue
        # if count > 0:
            # print('Here')
        print_error(file_size, status_code_count)
    except KeyboardInterrupt:
        print_error(file_size, status_code_count)
        raise


def print_error(file_size, status_code_count):
    print('File size: {}'.format(file_size))
    for items in sorted(status_code_count.items()):
        print('{}: {}'.format(items[0], items[1]))


if __name__ == '__main__':
    parse_log()
