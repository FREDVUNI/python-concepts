# Ask the user to input the marks for 5 students in 4 courses
marks = [[int(x) for x in input(f"Enter marks for student {i+1}(courses 1-4): ").split()] for i in range(5)]

# Calculate the average marks for each student
student_averages = [sum(marks[i])/len(marks[i]) for i in range(len(marks))]

# Find the highest average marks for students
highest_student_average = max(student_averages)

# Output the highest average marks for students
print("The highest average mark of students:", highest_student_average)

# Transpose the marks list to get the list of marks for each course
course_marks = list(zip(*marks))

# Calculate the average marks for each course
course_averages = [sum(course_marks[i])/len(course_marks[i]) for i in range(len(course_marks))]

# Find the highest average marks for courses
highest_course_average = max(course_averages)

# Output the highest average marks for courses
print("The highest average mark of courses:", highest_course_average)
