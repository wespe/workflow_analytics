from abc import ABC, abstractmethod

import numpy as np
import pandas as pd


class Rider(ABC):
    reserve_headers = [
        'Название проекта',
        'Руководитель',
        'Дата сдачи план.',
        'Дата сдачи факт.'
    ]

    def get_data_from_file(self, filename):
        return self.parse_file(filename)

    @abstractmethod
    def parse_file(self, filename):
        pass

    def get_name(self, string):
        r_values = ('план.', ''), ('факт.', '')
        for r_value in r_values:
            string = string.replace(*r_value)
        return string.strip()


class ExcelRider(Rider):

    def parse_file(self, filename):
        workplan = []
        df = pd.read_excel(filename)
        df = df.replace(np.nan, 0)

        for index, row in df.iterrows():
            info, progress = [], {}
            for header, value in row.items():
                if header in self.reserve_headers:
                    info.append(value)
                else:
                    emp_name = self.get_name(header)
                    if emp_name not in progress:
                        progress[emp_name] = []
                    progress[emp_name].append(value)

            workplan.append({
                'info': info,
                'progress': progress
            })
        return workplan


class CsvRider(Rider):

    def parse_file(self, filename):
        pass


def mine(filename):
    try:
        file_ext = filename.split('.')[-1].lower()
        if file_ext == 'xlsx':
            rider = ExcelRider()
        elif file_ext == 'csv':
            rider = CsvRider()
        else:
            raise TypeError
        return rider.get_data_from_file(filename)
    except TypeError:
        print(f'File "{filename}" is wrong format!')
