import uuid
from collections import namedtuple

Employee = namedtuple('Employee', 'name')


class Project:

    def __init__(self, _id, project_name, project_leader, project_is_expired, project_progress):
        self.id = _id or str(uuid.uuid4())
        self.name = project_name
        self.leader = project_leader
        self.is_expired = project_is_expired
        self.progress = project_progress

    def result(self):
        sign_1, sign_2 = 'not_expired', 'in_time'
        fixed_term, real_term = self.progress
        if self.is_expired:
            sign_1 = 'expired'
        if fixed_term == 0:
            sign_2 = 'voluntarily'
        elif fixed_term < real_term:
            sign_2 = 'over_time'
        elif fixed_term > real_term:
            sign_2 = 'small_time'
        return sign_1, sign_2

    def __repr__(self):
        return f"<Project id: {self.id}, name: {self.name}>"


class WorkPlan:

    def __init__(self, employee, projects, criterion=None):
        self.employee = employee
        self.projects = list(projects)
        self.criterion = criterion

    def result(self):
        if not hasattr(self, '__result'):
            self.__result = {}
            for project in self.projects:
                sign_1, sign_2 = project.result()
                if sign_1 not in self.__result:
                    self.__result[sign_1] = 0
                if sign_2 not in self.__result:
                    self.__result[sign_2] = 0
                self.__result[sign_1] += 1
                self.__result[sign_2] += 1
        return self.__result

    def efficiency(self):
        if self.criterion is None:
            efficiency = 0
        else:
            efficiency = self.criterion(self)
        return efficiency

    def __repr__(self):
        fmt = '<WorkPlan result: {} efficiency: {}>'
        return fmt.format(self.result(), self.efficiency())
