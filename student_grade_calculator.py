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
    else:
        return False
    
def full_stats(score1, score2, score3, midterm, final, target):
    assignments_avg = calculate_average(score1, score2, score3)
    weighted_avg = calculate_weighted(assignments_avg, midterm, final)
    grade_letter = determine_grade(weighted_avg)
    bool_grade = needs_improvement(weighted_avg, target)
    difference = round((target-weighted_avg), 2)
    print(f"Assignment Scores: {score1}, {score2}, {score3}")
    print(f"Midterm Score: {midterm}")
    print(f"Final Score: {final}")
    print("----------------------------------------")
    print(f"Regular Assignment Average: {assignments_avg:.2f}")
    print(f"Average with Lowest Dropped: {drop_lowest(score1, score2, score3)}")
    print(f"Using Better Average: {drop_lowest(score1, score2, score3)}")
    print()
    print(f"Weighted Course Average: {weighted_avg}")
    print(f"Letter Grade: {grade_letter}")
    print()
    print(f"Needs improvement for an '{determine_grade(target)}': {"Yes" if bool_grade else "No"}")
    print(f"Points needed: {difference if bool_grade else "0.00"}")
    print(f"Already meets or exceeds '{grade_letter}' grade requirements")


full_stats(85, 78, 92, 88, 82, 85)