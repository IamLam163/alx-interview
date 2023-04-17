import sys
#!/usr/bin/python3


def parse_log_line(line):
    """Parse a single log line and return the status code and file size."""
    fields = line.split()
    if len(fields) < 2:
        return None, None
    status_code = int(fields[-2])
    file_size = int(fields[-1])
    return status_code, file_size


def log_parser():
    """Parse logs from standard input and print metrics."""
    count = 0
    total_size = 0
    status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
    try:
        for line in sys.stdin:
            count += 1
            status_code, file_size = parse_log_line(line)
            if status_code is None:
                continue
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            if file_size is not None:
                total_size += file_size
            if count % 10 == 0:
                print('File size: {}'.format(total_size))
                for code, count in status_code_count.items():
                    if count > 0:
                        print('{}: {}'.format(code, count))
    except KeyboardInterrupt:
        print('File size: {}'.format(total_size))
        for code, count in status_code_count.items():
            if count > 0:
                print('{}: {}'.format(code, count))


if __name__ == '__main__':
    log_parser()


