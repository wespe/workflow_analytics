from tabulate import tabulate

from progress import efficiency_calc
from progress.criteria import *

work_dir = 'data/test_2'
employee_list = efficiency_calc(work_dir, criterion=average)

print('Employees rating:')
output = [[i+1, employee] for i, employee in enumerate(employee_list)]
print(tabulate(output))

