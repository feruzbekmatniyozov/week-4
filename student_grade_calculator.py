print("STUDENT GRADE CALCULATOR")
print("========================================")

def calculate_average(score1, score2, score3):
    return (score1+score2+score3)/3

def drop_lowest(score1, score2, score3):
    return (sum((score1, score2, score3))-min(score1, score2, score3))/2
    
def calculate_weighted(assignments, midterm, final):
    weighted = (assignments*0.3) + (midterm*0.3) + (final*0.4)
    return weighted

def determine_grade(average):
    if average > 89:
        return "A"
    elif average > 79:
        return "B"
    elif average > 69:
        return "C"
    elif average > 59:
        return "D"
    else:
        return "F"

def needs_improvement(current_avg, target_grade):
    if current_avg <=target_grade:
        return True
    
def full_stats(score1, score2, score3, midterm, final):
    assignments_avg = calculate_average(score1, score2, score3)
    weighted_avg = calculate_weighted(assignments_avg, midterm, final)
    print(f"Assignment Scores: {score1}, {score2}, {score3}")
    print(f"Midterm Score: {midterm}")
    print(f"Final Score: {final}")
    print("----------------------------------------")
    