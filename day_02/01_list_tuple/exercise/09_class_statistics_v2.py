student_scores = [98, 75, 100, 86, 100, 3]

# TODO: Print the average score
average_score = sum(student_scores) / len(student_scores)
print(average_score)

# TODO: Print the rankings, highest to lowest
print(f"Scores: {student_scores}")
print(f"Ascending: {sorted(student_scores)}")
print(f"Descending: {sorted(student_scores, reverse=True)}")
