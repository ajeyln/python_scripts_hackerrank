# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.

mark_sheet={}
for i in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet[name] = score

scores=[]
for a in mark_sheet.values():
    scores.append(a)
sorted_scores=list(sorted(set(scores)))
second_scores=sorted_scores[1]

names = []
for key,values in mark_sheet.items():
    if mark_sheet[key] == second_scores:
        names.append(key)
names_list = sorted(names)

for subject in names_list:
    print(subject)