# Task
''' You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.'''

# Input Format
''' The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data   ')
            print(data)
    def handle_comment(self, data):
        if len(data.split('\n')) == 1:
            print('>>> Single-line Comment  ')
            print(data)
        elif len(data.split('\n')) > 1:
            print('>>> Multi-line Comment  ',)
            for i in data.split('\n'):
                print(i) 
  
if __name__ == '__main__':
    lis = []
    for _ in range(int(input())):
        lis.append(input())
    html = '\n'.join(lis)
    parser = MyHTMLParser()
    parser.feed(html)
