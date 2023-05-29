import datetime
from io import TextIOWrapper
import os.path
import subprocess
from subprocess import STDOUT, PIPE
import time
import re
import csv
import math


def open_file(path: str):
    # open the file
    try:
        file = open(path, 'r', encoding='utf-8')
        return file
    except:
        print('Error opening file')
        return None


def read_content(file: TextIOWrapper):
    return file.read()


def count_the_lines(file_content: str):
    return file_content.count("\n")


def count_number_of_primitive_variables(file_content: str):
    variables_matched = re.findall(
        r"\b(byte|short|int|long|float|double|boolean|char)\b\s*\b\w+\b\s*(=.*?)*?;", file_content)
    return len(variables_matched)


def count_comments(file_content: str):
    comments_matched = re.findall(
        r"/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/|//.*", file_content)
    return len(comments_matched)


def count_if_statements(file_content: str):
    return file_content.count("if")


def count_switch_statements(file_content: str):
    return len(re.findall(r"switch\s*\(.+\)", file_content))


def count_else_statements(file_content: str):
    return len(re.findall(r"(?<!\bif\s)else\b(?!\s*if)", file_content))


def count_while_loops(file_content: str):
    return file_content.count("while")


def count_for_loops(file_content: str):
    return file_content.count("for")


def get_file_size_in_Kib(path: str):
    return round(os.path.getsize(path)/1024, 4)


def compile_java_file(path: str):
    try:
        subprocess.check_call(['javac', path])
        return True
    except:
        print('Error compiling java file')
        return False


def get_execution_time(path: str, assignment_number: str, problem_number: str, is_compiled_successfully: bool):
    if (not is_compiled_successfully):
        return 0
    if (assignment_number == 3):
        if (problem_number == 1):
            return get_execution_time_assignment3_problem1(path, 1, 5)
        elif (problem_number == 2):
            return get_execution_time_assignment3_problem2(path, 5, 10)
        elif (problem_number == 3):
            return get_execution_time_assignment3_problem3(path, "483 52 990 684 732 287 597 102 759 981 200 284 717 833 357 46 439 354 893 457 456 865 961 498 647 889 363 698 20 342 334 390 794 190 570 702 317 92 687 731 273 963 422 515 771 306 170 592 768 928 668 742 89 442 195 986 417 750 50 988 95 864 962 785 54 587 760 105 854 873 561 898 998 366 803 489 388 191 182 832 8 663 868 840 475 959 197 316 309 721 849 838 497 423 952 520 675 277 614 670 238 467 604 120 270")
    elif (assignment_number == 4):
        if (problem_number == 1):
            return get_execution_time_assignment4_problem1(path, "khaled")
        elif (problem_number == 2):
            return get_execution_time_assignment4_problem2(path, "1 8001")
        elif (problem_number == 3):
            return get_execution_time_assignment4_problem3(path, "3 5 6 7 200 4 5 6 2 3 4 100 2 2 2 8 9 10 1000 9 9 9")
    return 0


def get_execution_time_assignment3_problem1(path: str, test_number: int, count_number: int):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    # execute function
    stdout, stderr = proc.communicate(
        bytes(f"{test_number} {count_number}", "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment3_problem2(path: str, first_input: int, second_input: int):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate(
        bytes(f"{first_input} {second_input}", "utf-8"))
    # execute function
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment3_problem3(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment3_problem4(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment4_problem1(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment4_problem2(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment4_problem3(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def get_execution_time_assignment4_problem4(path: str, first_input: str):
    cmd = ['java', path]
    start_time = time.time()
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    # execute function
    stdout, stderr = proc.communicate(bytes(first_input, "utf-8"))
    # print(stdout.decode("utf-8"))
    if (stdout):
        end_time = time.time()
        return end_time - start_time
    if (stderr):
        print(stderr)


def number_of_methods(file_content: str):
    methods_matched = re.findall(
        "(public|protected|private|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])", file_content)
    return len(methods_matched)


def get_assignment_number(file_name: str) -> int:
    capture_assignment_number = re.search(
        "(?<=Assignment #)\d+", file_name, re.IGNORECASE)
    if capture_assignment_number:
        return int(capture_assignment_number.group(0))
    else:
        return None


def get_average_method_length(lines_count: int, methods_count: int) -> int:
    return math.ceil(lines_count / methods_count)


def find_problem_number(file_name: str):
    match = re.search(
        r"(Program|Problem|problem|program)[_ ]*(\d+)", file_name)
    if match:
        return int(match.group(2))
    else:
        return None


def get_student_id(file_name: str) -> int:
    capture_student_id = re.search(
        "(?<=Assignment #\d_)\d+", file_name, re.IGNORECASE)
    if capture_student_id:
        return capture_student_id.group(0)
    else:
        return None


def convert_timestamp_to_isoformat(file_name: str):
    match = re.search(
        "(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})", file_name)
    if match:
        year, month, day, hour, minute, second = map(int, match.groups())
        return datetime.datetime(year, month, day, hour, minute, second).isoformat()
    else:
        return None


def remove_comments_and_empty_lines(file_content):
    file_content = re.sub(
        r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)", "", file_content)
    file_content = re.sub(r"^\s*$\n?", "", file_content,  flags=re.MULTILINE)
    return file_content


def get_condition_type(if_count, switch_count):
    if (if_count > 0 and switch_count > 0):
        return "both"
    elif (if_count > 0 and switch_count == 0):
        return "if"
    elif (if_count == 0 and switch_count > 0):
        return "switch"
    else:
        return ""


def get_loop_type(for_count, while_count):
    if (for_count > 0 and while_count > 0):
        return "both"
    elif (for_count > 0 and while_count == 0):
        return "for"
    elif (for_count == 0 and while_count > 0):
        return "while"
    else:
        return ""


def extract_information(file_path: str):
    file = open_file(file_path)
    assignment_number = get_assignment_number(file.name)
    problem_number = find_problem_number(file.name)
    if (not assignment_number or not problem_number or (assignment_number == 3 and problem_number == 4) or (assignment_number == 4 and problem_number == 4)):
        return
    file_content = read_content(file)
    comments_count = count_comments(file_content)
    file_content = remove_comments_and_empty_lines(file_content)
    methods_count = number_of_methods(file_content)
    lines_count = count_the_lines(file_content)
    primitive_variables_count = count_number_of_primitive_variables(
        file_content)
    average_method_length = get_average_method_length(
        lines_count, methods_count)
    file_size = get_file_size_in_Kib(file_path)
    student_id = get_student_id(file.name)
    if_statements_count = count_if_statements(file_content)
    switch_statements_count = count_switch_statements(file_content)
    else_statements_count = count_else_statements(file_content)
    for_loops_count = count_for_loops(file_content)
    while_loops_count = count_while_loops(file_content)
    loops_count = for_loops_count + while_loops_count
    submission_time = convert_timestamp_to_isoformat(file.name)
    preferred_loop_type = get_loop_type(for_loops_count, while_loops_count)
    preferred_condition_type = get_condition_type(
        if_statements_count, switch_statements_count)
    file.close()
    new_name = rename_file(file_path, assignment_number,
                           student_id, problem_number)

    new_path = f"./renamed_submissions/{new_name}"
    rename_class(new_path, new_name)

    is_compiled_successfully = compile_java_file(new_path)
    # execute with the correct arguments
    execution_time = get_execution_time(new_path, assignment_number, problem_number, is_compiled_successfully)
    if(execution_time):
        execution_time = round(execution_time, 4)
    # print everything in one print statement
    """
        print('Methods: ' + str(methods_count) + '\n' +
          'Lines: ' + str(lines_count) + '\n' +
          'File Size: ' + str(file_size) + '\n' +
          'Compiled: ' + str(is_compiled_successfully) + '\n' +
          'Execution Time: ' + str(execution_time) + '\n' +
          'Assignment Number: ' + str(assignment_number) + '\n' +
          'Student ID: ' + str(student_id) + '\n' +
          'Submission Time: ' + str(submission_time) + '\n' +
          'Problem Number: ' + str(problem_number) + '\n')
    """
    write_to_dataset(student_id, assignment_number, problem_number, submission_time,
                     file_size, methods_count, lines_count, is_compiled_successfully, execution_time, if_statements_count, loops_count, primitive_variables_count, comments_count, average_method_length, else_statements_count, switch_statements_count, for_loops_count, while_loops_count, preferred_loop_type, preferred_condition_type)


def rename_class(path: str, new_name: str):
    # Read in the file
    with open(path, 'r', encoding="utf-8") as file:
        filedata = file.read()
    # Replace the target string
    new_name = new_name.replace('.java', '')
    filedata = re.sub(r"(public\s+)?class\s+\w+",
                      'public class ' + new_name, filedata)
    # Write the file out again
    with open(path, 'w', encoding="utf-8") as file:
        file.write(filedata)


def rename_file(path: str, assignment_number: int, student_id: int, problem_number: int | None):
    # replace file name
    new_file_name = f"A{assignment_number}_P{problem_number}_{student_id}" + '.java'
    os.rename(f"{path}",
              f"./renamed_submissions/{new_file_name}")
    return new_file_name


def main():
    loop_through_dir()


def write_to_dataset(Student_ID, Assignment_number, Problem_number, Submission_time, File_size, Methods_count, Lines_count,  Compiled_succesfully, Execution_time, if_statements_count, loops_count, primitive_variables_count, comments_count, average_method_length, else_statements_count, switch_statements_count, for_loops_count, while_loops_count, preferred_loop_type, preferred_condition_type):
    with open('dataset.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Student_ID, Assignment_number, Problem_number, Submission_time,
                        File_size, Methods_count, Lines_count, average_method_length, if_statements_count, else_statements_count, switch_statements_count, for_loops_count, while_loops_count, loops_count, comments_count, primitive_variables_count, Compiled_succesfully, Execution_time, preferred_loop_type, preferred_condition_type])


def create_dataset_file():
    with open('dataset.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student_ID", "Assignment_number", "Problem_number", "Submission_time", "File_size", "Methods_count", "Code_lines_count",
                        "Average_method_length", "if_statements_count", "else_statements_count", "switch_statements_count", "For_loop_count", "While_loop_count", "Loops_count", "Comments_count", "primitive_variables_count", "Compiled_succesfully", "Execution_time", "preferred_loop_type", "preferred_condition_type"])


def loop_through_dir():
    # loop through directory and get all files
    path_of_the_directory = ".\\submissions"
    print("Files and directories in a specified path:")
    create_dataset_file()
    for filename in os.listdir(path_of_the_directory):
        f = os.path.join(path_of_the_directory, filename)
        if os.path.isfile(f):
            extract_information(f)


if __name__ == "__main__":
    main()
