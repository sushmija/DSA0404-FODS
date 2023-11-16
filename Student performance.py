import numpy as np
student_scores = np.array([
    [85, 90, 78, 92],
    [92, 88, 95, 89],
    [78, 85, 88, 90],
    [94, 91, 87, 84]
])

average_scores = np.mean(student_scores, axis=0)


subject_with_highest_average = np.argmax(average_scores)

print("Student Scores:\n", student_scores)
print("\nAverage Score for Each Subject:\n", average_scores)
print("\nSubject with the Highest Average Score:", subject_with_highest_average)
