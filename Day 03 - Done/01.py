assumed_scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

reversed_scores = list(set(assumed_scores))

reversed_scores.sort(reverse=True)

runner_up_score = reversed_scores[1]

print("The runner-up score is:", runner_up_score)