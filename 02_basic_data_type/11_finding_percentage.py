# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        student_marks[name] = scores
    query_name = input()
    point = 0.0
    count = 0.0
    for key, marks in student_marks.items():
        if key == query_name:
            for mark in marks:
                point += float(mark)
                count += 1
            average = point / count
            print("{0:.2f}".format(average))
                
            
