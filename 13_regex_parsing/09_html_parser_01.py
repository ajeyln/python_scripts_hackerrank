#Task
''' You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

If an HTML tag has no attribute then simply print the name of the tag.
If an attribute has no attribute value then simply print the name of the attribute value as None.'''

# Input Format
''' The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.'''

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for m in range(int(input()))]))