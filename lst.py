# lst = ['a', 'b', 'c', 'd', 'e', 'f']
# print("Slice index 2 to 4:", lst[2:5])

# lst = []
# lst.append(1)
# lst.append(2)
# lst.append(3)
# lst.extend([4, 5, 6])
# print("Extended list:", lst)


# squares = [x**2 for x in range(1, 11)]
# print("Squares:", squares)

# nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Element 5:", nested[1][2])

# def filter_even():
#     return tuple(x for x in range(1,10) if x % 2 == 0)

# print("Even from tuple:", filter_even())

# students = (("John", 20, 3.5), ("Alice", 21, 3.8), ("Bob", 19, 3.2))
# print("Second student name:", students[1][0])
# avg_gpa = sum(s[2] for s in students) / len(students)
# print("Average GPA:", avg_gpa)

list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
list_of_lists = [list(item) for item in list_of_tuples]
list_of_lists[1][1] = 'TWO'
print("Modified Tuples:", [tuple(item) for item in list_of_lists])
