import os
import hashlib
from dataminer.miner import mine
from progress.creator import *


def is_expired(fixed_term, real_term):
    return fixed_term < real_term


def convert_to_hex(string):
    return hashlib.md5(string.encode()).hexdigest()


def efficiency_calc(path, criterion):
    employee_dict = {}
    for file in os.listdir(path):
        wp_data = mine(f'{path}/{file}')
        if wp_data is None:
            continue
        for project in wp_data:
            project_id = str(uuid.uuid4())
            name, leader, *date_lst = project['info']
            for emp_name, progress in project['progress'].items():
                hex_name = convert_to_hex(emp_name)
                if hex_name not in employee_dict:
                    employee_dict[hex_name] = {
                        'employee': Employee(emp_name),
                        'projects': []
                    }
                employee_dict[hex_name]['projects'].append(
                    Project(project_id, name, leader, is_expired(*date_lst), progress))

    result_tb = {}
    for emp_hash, emp_progress in employee_dict.items():
        employee, project = emp_progress.values()
        wp = WorkPlan(employee, project, criterion=criterion)
        result_tb[employee.name] = wp.efficiency()
    return sorted(result_tb, key=lambda x: result_tb[x])


