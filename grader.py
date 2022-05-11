import os

ERROR_FILE = 'errors.txt'
GRADE_FILE = 'grades.txt'
TESTS_FILE = 'input_files/tests.txt'
STUDENTS_FILE = 'input_files/students.txt'
GRADE_OUTPUT_TEMPLATE = '{first:15s} {last:15s} {score:5s}  {grade:2s}\n'

def delete_file_if_exists(file_name):
    '''
    Deletes a file if it already exists.
    Input: file_name, the file name to delete
    Output: none
    '''
    if os.path.exists(file_name):
        os.remove(file_name)

def read_file(file_name):
    '''
    Reads the given file name into a list, stripping the newline
    character from each line read.
    Input: file_name, the file name to be read into a list

    Returns the list containing the lines read from the file
    '''
    test_list = []
    infile = open(file_name, 'r')
    test_list = infile.readlines()

    for i in range(len(test_list)):
        test_list[i] = test_list[i].strip('\n')
    infile.close()

    return test_list

def calc_test_score(answer_key, test_answers):
    '''
    Grades student's answers based on the answer key:
        a) a blank answer is worth 0 points
        b) a correct answer is worth 1 point
        c) an incorrect answer is worth -0.25 points
    Highest possible score is 100 and the lowest possible score,
    if all questions are answered but incorrect, is -25.
    Input: answer_key, key used to grade tests,
    and test_answers, list of students' answers as a numeric score

    Returns a float value that is the calculated test score
    '''
    score = 0

    for i in range(len(answer_key)):
        if answer_key[i] == test_answers[i]:
            score += 1
        elif test_answers[i] == '':
            score += 0
        else:
            score -= .25

    return score

def assign_letter_grade(test_score):
    '''
    Assigns a letter grade to students' tests.
    Input: test_score, the letter grade based on the numeric score

    Returns a letter grade
    '''
    letter_grade = ''
    if test_score > 46:
        letter_grade = 'A'
    elif test_score >= 44:
        letter_grade = 'A-'
    elif test_score >= 42:
        letter_grade = 'B+'
    elif test_score >= 40:
        letter_grade = 'B'
    elif test_score >= 38:
        letter_grade = 'B-'
    elif test_score >= 36:
        letter_grade = 'C+'
    elif test_score >= 34:
        letter_grade = 'C'
    elif test_score >= 32:
        letter_grade = 'C-'
    elif test_score >= 30:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade

def validate_id(student_id):
    '''
    Validate the student ID:
        a) The ID field is 6 characters long
        b) The first two characters are letters. The letters must be distinct (no duplicates)
        c) The last four characters are digits. The digits must be distinct (no duplicates)
    Input: student_id, the student id

    Returns a string
    '''
    message = ''

    if len(student_id) != 6:
        message = student_id + ' is invalid: ID is not 6 characters in length.'
    else:
        if not (student_id[0].isalpha() and student_id[1].isalpha()):
            message = student_id + ' is invalid: First 2 characters must be letters.'
        elif student_id[0] == student_id[1]:
            message = student_id + ' is invalid: First 2 characters must be unique.'
        elif not student_id[2:].isdigit():
            message = student_id + ' is invalid: Last 4 digits must be digits.'
        else:
            for num in student_id[2:]:
                if student_id[2:].count(num) > 1:
                    message = student_id + ' is invalid: Last 4 digits must be unique.'
                    return message

    return message

def write_error_message(message):
    '''
    Writes errors to a file.
    Input: message, errors that are written to a file
    Output: none
    '''
    error = open('errors.txt', 'a')
    error.write(message + '\n')
    error.close()

def main():
    '''
    Controls the process of grading student tests.
    The students who took the test were assigned an ID number before the test.
    This grader reads both the test and student data (names and IDs) from two files,
    and puts them into appropriate lists. It grades the tests based on an answer key,
    and assigns each test with a numeric score and letter grade.
    Test information, such as students' names, their numberic scores and letter grades
    are written to a grades file.
    Errors, such as invalid student ids or ids with no names, are written to an error file.
    '''
    delete_file_if_exists(ERROR_FILE)
    delete_file_if_exists(GRADE_FILE)

    first_name = ''
    last_name = ''
    score = float
    letter_grade = ''
    GRADE_OUTPUT_TEMPLATE.format(
        first='First Name', last='Last Name', score='Score', grade='Grade')

    tests_list = read_file('tests.txt')
    students_list = read_file('students.txt')
    students_dictionary = {}

    for student in students_list[0:]:
        students_dictionary[student.split(' ')[0]] = student.split(' ')[
            1], student.split(' ')[2]

    outfile = open('grades.txt', 'w')
    outfile.write(GRADE_OUTPUT_TEMPLATE.format(
        first='First Name', last='Last Name', score='Score', grade='Grade'))
    outfile.write('============================================\n')

    answer_key = tests_list[0].split(';')[1]

    for test in tests_list[1:]:
        student_id, test_answers = test.split(';')
        score = calc_test_score(answer_key, test_answers)
        letter_grade = assign_letter_grade(score)

        error_message = validate_id(student_id)
        if error_message != '':
            write_error_message(error_message)
        else:
            if student_id not in students_dictionary:
                write_error_message(message='ID was not found: ' + student_id +
                                    ' Score: ' + format(score, '.2f') + ' Grade: ' + letter_grade)
            else:
                first_name = students_dictionary[student_id][0]
                last_name = students_dictionary[student_id][1]
                outfile.write(GRADE_OUTPUT_TEMPLATE.format(
                    first=first_name, last=last_name,
                    score=format(score, '.2f'), grade=letter_grade))

    outfile.close()

if __name__ == '__main__':
    main()
