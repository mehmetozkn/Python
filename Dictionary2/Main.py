# Q1 - Her eleman kaçar kere geçiyor.

items = ['computer', 'phone', 'tv', 'tv', 'computer', 'tv', 'game console', 'tv', 'computer']
print({item: items.count(item) for item in items})

# Q2 - Vize Final ortalaması.
student_details= [
  {'id' : 1, 'subject' : 'math', 'Midterm' : 70, 'Final' : 82},
  {'id' : 2, 'subject' : 'math', 'Midterm' : 73, 'Final' : 74},
  {'id' : 3, 'subject' : 'math', 'Midterm' : 75, 'Final' : 86}
]
sum([(record['Midterm'] + record['Final']) / 2 for record in student_details]) / len(student_details)


# Q3 - 2 Ayrı dersin 2 ayrı ortalaması
student_details= [
  {'id' : 1, 'subject' : {'math': [70, 82], 'cs': [75, 87]}},
  {'id' : 2, 'subject' : {'math': [73, 74], 'cs': [78, 79]}},
  {'id' : 3, 'subject' : {'math': [75, 86], 'cs': [80, 91]}}
]
print({student['id']: {"math": sum(student['subject']['math']) / len(student['subject']['math']),
                  "cs": sum(student['subject']['cs']) / len(student['subject']['cs'])} for student in student_details})

