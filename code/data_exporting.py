""""""
import csv
import pathlib
import typing

from grid_info import NUM_QUESTIONS, Field, RealOrVirtualField, VirtualField
import list_utils

COLUMN_NAMES: typing.Dict[RealOrVirtualField, str] = {
    Field.LAST_NAME: "Last Name",
    Field.FIRST_NAME: "First Name",
    Field.MIDDLE_NAME: "Middle Name",
    Field.STUDENT_ID: "Student ID",
    Field.COURSE_ID: "Course ID",
    Field.TEST_FORM_CODE: "Test Form Code",
    VirtualField.SCORE: "Total Score (%)"
}


class OutputSheet():
    """A lightweight matrix of data to be exported. Faster than a dataframe but
    can be easily converted to one when the need arises."""
    # Must be structured as: field_a, field_b, ..., 1, 2, 3, ...
    data: typing.List[typing.List[str]]
    field_columns: typing.List[RealOrVirtualField]
    num_questions: int = NUM_QUESTIONS
    row_count: int

    def __init__(self, columns: typing.List[RealOrVirtualField]):
        self.field_columns = columns
        field_column_names = [COLUMN_NAMES[column] for column in columns]
        answer_columns = [str(i + 1) for i in range(self.num_questions)]
        self.data = [field_column_names + answer_columns]
        self.row_count = 0

    def save(self, path: pathlib.PurePath):
        with open(str(path), 'w+', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(self.data)

    def add(self, fields: typing.Dict[RealOrVirtualField, str], answers: typing.List[str]):
        row: typing.List[str] = []
        for column in self.field_columns:
            try:
                row.append(fields[column])
            except KeyError:
                row.append('')
        self.data.append(row + answers)
        self.row_count = len(self.data) - 1

    def addFile(self, csvfile: pathlib.Path):
        with open(str(csvfile), 'r', newline='') as file:
            reader = csv.reader(file)
            names = next(reader)
            keys: typing.List[RealOrVirtualField] = []
            for name in names:
                try:
                    key = next(key for key, value in COLUMN_NAMES.items() if value == name)
                except StopIteration:
                    pass
                keys.append(key)
            first_answer_index = list_utils.find_index(names, "1")
            for row in reader:
                fields = {key: value for key, value in list(zip(keys, row))[:first_answer_index]}
                answers = row[first_answer_index:]
                self.add(fields, answers)
            