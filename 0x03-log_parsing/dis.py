#!/usr/bin/python3
"""log parser that reads stdin and computes memtrics"""
import sys


def log_stats(lines):
        """log parser that reads stdin and computes memtrics"""
        count = 0
        total_size = 0
        status_code_count = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        try:
                for line in lines:
                        count += 1
                        status_code, file_size = log_parser(line)
                        if status_code in status_code_count:
                                status_code_count[status_code] += 1
                        total_size += file_size
                        if count % 10 == 0:
                                print_log(total_size, status_code_count)
                print_log(total_size, status_code_count)
        except KeyboardInterrupt as error:
                print_log(total_size, status_code_count)



def log_parser(line):
        """parses the log"""
        split = line.split()
        status_code = int(split[-2])
        file_size = int(split[-1])
        return status_code, file_size

def print_log(total_size, status_code_count):
        """helper function to print"""
        print('File_size: {}'.format(total_size))
        for code, count in status_code_count.items():
                if count != 0:
                 print('{}: {}'.format(code, count))


if __name__ == "__main__":
    sys.stdin = sys.stdin
    log_stats(sys.stdin)
