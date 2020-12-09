''' The input is read by the provided locked code template. In the first line, there is a single integer q denoting the number of queries.
 Each of the following q lines contains a stream_name followed by integer n, and it corresponds to a single test for your function.'''

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for x in range(n):
        print(stream.get_next())
    
queries = int(input())
for y in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
