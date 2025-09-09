import openpyxl
import random
import string
from selenium.webdriver.support.ui import Select
import time

def read_employee_data_from_excel(excel_path):
    """
    Reads employee data from Excel and returns a list of dictionaries.
    Each dictionary contains employee info for one row.
    """
    workbook = openpyxl.load_workbook(excel_path)
    sheet = workbook.active
    employees = []

    headers = [cell.value for cell in sheet[1]]  # first row as headers
    for row_index, row in enumerate(sheet.iter_rows(min_row=2), start=2):
        data = {headers[i]: row[i].value for i in range(len(headers))}
        data["row_index"] = row_index  # keep track of Excel row
        employees.append(data)
    return employees, workbook, sheet


def write_result_to_excel(sheet, row_index, result):
    """
    Writes 'Pass' or 'Fail' in the last column of Excel for the given row.
    """
    last_col = sheet.max_column + 1
    sheet.cell(row=row_index, column=last_col, value=result)
