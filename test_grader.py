import grader
import pytest

def test_read_file(tmp_path):
    test_file = tmp_path.joinpath('test_data.txt')
    test_file.write_text('000000;A,F,F,F\nZE5379;E,F,F,F\nTA1372;A, ,B,A\n')

    result = grader.read_file(test_file)
    assert len(result) == 3

def test_read_file_remove_newline(tmp_path):
    test_file = tmp_path.joinpath('test_data.txt')
    test_file.write_text('000000;A,F,F,F\nZE5379;E,F,F,F\nTA1372;A, ,B,A\n')

    result = grader.read_file(test_file)
    assert not result[0].endswith('\n')
    assert not result[1].endswith('\n')
    assert not result[2].endswith('\n')

def test_calc_test_score_when_all_answers_are_correct():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['A', 'F', 'F', 'F']) == 4

def test_calc_test_score_when_all_answers_are_incorrect():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['F', 'B', 'A', 'C']) == -1

def test_calc_test_score_when_one_answer_is_incorrect():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['A', 'F', 'F', 'B']) == 2.75

def test_calc_test_score_when_three_answers_are_incorrect():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['F', 'B', 'A', 'F']) == 0.25

def test_calc_test_score_when_one_answer_is_blank():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['A', '', 'F', 'F']) == 3

def test_calc_test_score_when_two_answers_are_blank():
    assert grader.calc_test_score(
        ['A', 'F', 'F', 'F'], ['A', '', 'F', '']) == 2

@pytest.mark.parametrize("score, expected",
                         [(50, 'A'),
                          (45, 'A-'),
                          (43, 'B+'),
                          (40, 'B'),
                          (39, 'B-'),
                          (37, 'C+'),
                          (34, 'C'),
                          (32, 'C-'),
                          (30, 'D'),
                          (5, 'F')])
def test_letter_grade(score, expected):
    assert grader.assign_letter_grade(score) == expected

def test_student_id_when_less_than_6_characters():
    assert grader.validate_id(
        'AB123') == 'AB123 is invalid: ID is not 6 characters in length.'

def test_student_id_when_first_two_characters_are_not_alpha():
    assert grader.validate_id(
        'A11234') == 'A11234 is invalid: First 2 characters must be letters.'

def test_student_id_has_duplicate_first_two_characters():
    assert grader.validate_id(
        'AA1234') == 'AA1234 is invalid: First 2 characters must be unique.'

def test_student_id_when_last_four_digits_are_not_digits():
    assert grader.validate_id(
        'AB12ZB') == 'AB12ZB is invalid: Last 4 digits must be digits.'

def test_student_id_when_last_four_digits_are_duplicates():
    assert grader.validate_id(
        'AB1232') == 'AB1232 is invalid: Last 4 digits must be unique.'

def test_student_id_is_valid():
    assert grader.validate_id('AB1234') == ''
