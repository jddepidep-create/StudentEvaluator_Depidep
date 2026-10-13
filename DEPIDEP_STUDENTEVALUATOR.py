# Helpers
#John owen D. Depidep
#8-adelfa

def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    # Declares the variables as GLOBAL
    global name
    global assessment1
    global assessment2
    global assessment3

    # Asks user for name, and assesment scores
    name = input("Please enter student name: ")
    assessment1 = input("Enter Assessment 1: ")
    assessment2 = input("Enter Assessment 2: ")
    assessment3= input("Enter Assessment 3: ")

    return name,assessment1,assessment2,assessment3

def evaluate_performance():
    # declares variables as global
    global average
    global performance_level

    # Average assesment scores together
    average = ( int(assessment1) + int(assessment2) + int(assessment3) ) / 3

    # if-elif ladder to determine performance level
    if average >= 90:
        performance_level = "outstanding"
    elif average >= 85:
        performance_level = "very satisfactory"
    elif average >= 80:
        performance_level = "satisfactory"
    elif average >= 75:
        performance_level = "fairly satisfactory"
    else:
        performance_level = "needs improvement"

def display_report():
    # Displays finalized and calculated data
    print("STUDENT PERFORMANCE REPORT")
    print("Student name: ",name)
    print("Average Performance: " + str(average))
    print(f"Assesment Scores: {assessment1},{assessment2},{assessment3}")
    print("Performance Level: " + str(performance_level) )

# Calls Helper Functions in order
display_header()
get_student_info()
evaluate_performance()
display_report()
