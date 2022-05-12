# Scantron Machine Grader
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
## Table of Contents
+ [Purpose](https://github.com/mcmunchie/scantron-machine-grader#purpose)
+ [Scenario](https://github.com/mcmunchie/scantron-machine-grader#scenario)
+ [Input Files](https://github.com/mcmunchie/scantron-machine-grader#input-files)
+ [Output Files](https://github.com/mcmunchie/scantron-machine-grader#output-files)
+ [Example Output](https://github.com/mcmunchie/scantron-machine-grader#example-output)
+ [Test Cases to Consider](https://github.com/mcmunchie/scantron-machine-grader#test-cases-to-consider)

## Purpose
To learn file handling and processing in Python.
## _Scenario_
Students at Yorkfield High School recently took their final exams. Each student were assigned an ID number before the test. The test has their ID number on it and their answers to 100 multiple-choice questions. Grading the tests involves comparing each answer on the student's answer sheet against the corresponding answer on the answer key. Questions are graded as follows:
+ A blank answer is worth 0 points
+ A correct answer is worth 1 point
+ An incorrect answer is worth -0.25 points

Grades can be calculated with the following equation:
<!-- $$
(number of correct answers) - (0.25) * (number of incorrect answers)
$$ --> 

<div align="center"><img style="background: white;" src="svg\NDVomylT2a.svg"></div>
The highest possible score is 100, while the lowest possible score is -25.

Letter grades are assigned based on the following scale:

| Test Score | Letter Grade |
| --- | --- |
| > 46 | A |
| ≥ 44 | A-|
| ≥ 42 | B+|
| ≥ 40 | B |
| ≥ 38 | B-|
| ≥ 36 | C+|
| ≥ 34 | C |
| ≥ 32 | C-|
| ≥ 30 | D |
| < 30 | F |

## Input Files
There are two input files for this program. 
1. **tests.txt**, this file represents the answer sheets that the students turned in. The first line in the file is the **answer key** and has an ID field of all zeros. The following lines have an ID and a set of answers, with a semicolon separating the two fields.
2. **students.txt**, this file has the students' names and their IDs. All fields are separated by spaces. Each line in this file represents the data for a single student: 

    > _Example: KX3105 Jin Qian_

## Output Files
Test data and student data is read, and the information from them are processed into two output files.
1. **grades.txt**, records the students' names, their numeric scores, and their final letter grades.
2. **errors.txt**, records any errors during grading.

## Example Output
> Grades file processed
<img src=img\grades.png />

> Error file processed
<img src=img\errors.png />

> Unit tests
<img src=img\test-grader.png />

## Test Cases to Consider
| ID | Status |
| --- | --- |
| XY1234 | Valid ID |
| X1Y234 | Invalid! 1st two characters are not letters |
| AB9879 | Invalid! Duplicate digit '9' |
| XYZ123 | Invalid! Last four characters should be digits |
| XY12345 | Invalid! Too many characters |
| GG4826 | Invalid! Letters are not distinct |
