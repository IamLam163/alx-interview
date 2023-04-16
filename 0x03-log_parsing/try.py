#!/usr/bin/python3
"""log parser that reads stdin and computes memtrics"""
import sys



def log_parser():
        """log parser that reads stdin and computes memtrics"""
        count = 0
        total_size = 0
        stdin = sys.stdin
        status_code_count = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        try:
                for line in stdin:
                        count += 1
                        split = line.split()
                        status_code = int(split[-2])
                        file_size = int(split[-1])
                        if status_code in status_code_count:
                                status_code_count[status_code] += 1
                        total_size += file_size
                        if count % 10 == 0:
                                print('file_size: {}'.format(total_size))
                                for code, count in status_code_count.items():
                                        print('{}: {}'.format(code, count))
        except KeyboardInterrupt as error:
                print('File_size: {}'.format(total_size))
                for code, count in status_code_count.items():
                        print('{}: {}'.format(code, count))


"""
try:
    for line in stdin:
        count += 1
        #print(line.split()[-2], line.split()[7])
        status_code = int(line.split()[-2])
        #print(status_code)
        file_size = int(line.split()[-1])
        total_size += file_size
        #print(f'file_size', total_size)
        if status_code in status_code_count:
            status_code_count[status_code] += 1
            #print('{}'.format(count))
        if count % 10 == 0:
            print('File_size: {}'.format(total_size))
            for code, count in status_code_count.items():
                print('{}: {}'.format(code, count))

except KeyboardInterrupt as error:
    print('File_size: {}'.format(total_size))
    for code, count in status_code_count.items():
                print('{}: {}'.format(code, count))
"""
