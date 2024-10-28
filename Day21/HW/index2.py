print("The Course assesment")

midterm_score = float(input("Enter your midterm score (0-100):"))
while midterm_score < 0 or midterm_score > 100:
    print("Please enter a valid score from 0 to 100.")
    midterm_score = float(input("Enter Your midterm Score (0-100):"))

final_exam_score = float(input("Enter Your Final Exam Score (0-100):"))
while final_exam_score < 0 or final_exam_score > 100:
    print("Please Enter The correct Number 0-100")
    final_exam_score = float(input("Enter The final exam score: "))

project_score = float(input("Enter The Project Score (0-100): "))
while project_score < 0 or project_score > 100:
    print("Please enter the correct number 0 -100.")
    project_score = float(input("Enter The project score (0-100): "))

final_grade = (0.2 * midterm_score) + (0.4 * final_exam_score) + (0.4 * project_score)

if final_grade >= 70:
    print(f"U have passed The Course")
else:
    print(f"Sadly u didnt pass the Course")