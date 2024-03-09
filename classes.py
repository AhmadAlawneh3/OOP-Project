from abc import ABC, abstractmethod


class Member:
    @abstractmethod
    def __init__(self, name='_', DOB='_', status='_', numOfChildren=-1, DateOfHire='_', DateOfResignation='_',
                 specialist='_', UniversityDegree='_', finished=False):
        name = name.split('_')
        self.name = name
        self.DOB = DOB
        self.status = status
        self.numOfChildren = numOfChildren
        self.DateOfHire = DateOfHire
        self.DateOfResignation = DateOfResignation
        self.specialist = specialist
        self.UniversityDegree = UniversityDegree
        self.finished = finished
        
        

    @abstractmethod
    def sal(self):
        pass

    def save(self):
        st = self.name[0] + '_'+self.name[1]+'_'+self.name[2] + ' ' + self.DOB + ' ' + self.status + ' ' + str(
            self.numOfChildren) + ' ' + self.DateOfHire + ' ' + \
             self.DateOfResignation + ' ' + self.specialist + ' ' + self.UniversityDegree + ' ' + str(self.finished)
        return st

    def __repr__(self):
        st = ''
        st = 'Name: ' + self.name[0] + ' '+self.name[1]+' '+self.name[2] + '  DOB:' + self.DOB + '  status:' + self.status + '\nNumber of children:' + \
             str(self.numOfChildren) + '  Date of Hire: ' + self.DateOfHire + '  Date of resignation: ' + self.DateOfResignation + \
             '\nSpecialist: ' + self.specialist + '  University degree: ' + self.UniversityDegree + '  Finished: ' + str(
            self.finished)
        return st

    def get_name(self):
        return self.name

    def get_DOB(self):
        return self.DOB

    def get_status(self):
        return self.status

    def get_numOfChildren(self):
        return self.numOfChildren

    def get_DateOfHire(self):
        return self.DateOfHire

    def get_DateOfResignation(self):
        return self.DateOfResignation

    def get_specialist(self):
        return self.specialist

    def get_UniversityDegree(self):
        return self.UniversityDegree

    def get_finished(self):
        return self.finished

    # ..........................................
    def set_name(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.name = name

    def set_DOB(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.DOB = name

    def set_status(self, name):
        if type(name) != bool:
            raise TypeError('Enter a boolean')
        self.status = name

    def set_numOfChildren(self, name):
        if type(name) != int:
            raise TypeError('Enter an integer')
        self.numOfChildren = name

    def set_DateOfHire(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.DateOfHire = name

    def set_DateOfResignation(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.DateOfResignation = name

    def set_specialist(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.specialist = name

    def set_UniversityDegree(self, name):
        if type(name) != str:
            raise TypeError('Enter a text')
        self.UniversityDegree = name

    def set_finished(self, name):
        if type(name) != bool:
            raise TypeError('Enter a boolean')
        self.finished = name

    @abstractmethod
    def detailed_salary(self):
        pass


class regular_employees(Member):
    def __init__(self, name='_', DOB='_', status='_', numOfChildren=-1, DateOfHire='_', DateOfResignation='_',
                 specialist='_', UniversityDegree='_', finished=False):
        super().__init__(name, DOB, status, numOfChildren, DateOfHire, DateOfResignation, specialist, UniversityDegree,
                         finished)
        self.salary = 0
        self._BaseSalary = 220
        self.Diploma_rate = 50
        self.BSc_rate = 100
        self.Master_rate = 120
        self.PhD_rate = 300
        self.married_rate = 50
        self.children_rate = 20
        self.taxRate = 0.05
        self.salary = self.sal()

    # For changing rates :
    def set_Diploma_Rate(self, rate):
        self.Diploma_rate = rate

    def set_BSc_rate(self, rate):
        self.BSc_rate = rate

    def set_Master_rate(self, rate):
        self.Master_rate = rate

    def set_PhD_rate(self, rate):
        self.PhD_rate = rate

    def set_tax_rate(self, rate):
        self.tax_Rate = rate

    def set_married_rate(self, rate):
        self.married_rate = rate

    def set_children_rate(self, rate):
        self.children_rate = rate

    # Calculate Salary
    def sal(self):
        self.salary += self._BaseSalary
        if self.UniversityDegree == "Diploma":
            self.salary += self.Diploma_rate
        elif self.UniversityDegree == "BSc":
            self.salary += self.BSc_rate
        elif self.UniversityDegree == "Master":
            self.salary += self.Master_rate
        elif self.UniversityDegree == "Ph.D":
            self.salary += self.PhD_rate

        if self.status == "married":
            self.salary += self.married_rate

        if int(self.numOfChildren) >= 3:
            for i in range(1, 4):
                self.salary += 20
        else:
            for i in range(1, int(self.numOfChildren) + 1):
                self.salary += self.children_rate

        self.salary -= self.salary * self.taxRate
        return self.salary

    def detailed_salary(self):
        print('\tBase salary:%5d' % self._BaseSalary)
        if self.UniversityDegree == "Diploma":
            print('\tDiploma rate:%5d' % self.Diploma_rate)
        elif self.UniversityDegree == "BSc":
            print('\tBSc rate:%5d' % self.BSc_rate)
        elif self.UniversityDegree == "Master":
            print('\tMaster rate:%5d' % self.Master_rate)
        elif self.UniversityDegree == "Ph.D":
            print('\tPh.D rate:%5d' % self.PhD_rate)

        if self.status == "married":
            print('\tMarried:%5d' % self.married_rate)

        if int(self.numOfChildren) >= 3:
            for i in range(1, 4):
                print('\tChild', i, 'rate:%5d' % int(self.children_rate))
        else:
            for i in range(1, int(self.numOfChildren) + 1):
                print('\tChild', i, 'rate:%5d' % self.children_rate)

        print('\tTax:%5.2f' % float(self.salary * self.taxRate), '\n\tSalary:%5.2f' % float(self.get_salary()))

    def save(self):
        st = super().save()
        st = 'Regular_employees' + ' ' + st + ' ' + str(self._BaseSalary) + ' ' + str(self.salary) + ' ' + str(
            self.Diploma_rate) + ' ' + \
             str(self.BSc_rate) + ' ' + str(self.Master_rate) + '' + str(self.PhD_rate) + ' ' + str(
            self.taxRate) + ' ' + \
             ' ' + str(self.married_rate) + ' ' + str(self.children_rate)
        return st

    def __repr__(self):
        st = ''
        st = super().__repr__() + ' Salary: ' + str(self.sal()) + ' Tax: ' + str(self.salary * self.taxRate)
        return st

    def get_salary(self):
        return self.salary


class workers(Member):
    def __init__(self, name='_', DOB='_', status='_', numOfChildren=-1, DateOfHire='_', DateOfResignation='_',
                 specialist='_', UniversityDegree='_', finished='_', pay_rate=0, hours=0):
        super().__init__(name, DOB, status, numOfChildren, DateOfHire, DateOfResignation, specialist,
                         UniversityDegree,
                         finished)
        self.pay_rate = pay_rate
        self.hours = hours
        self.salary = self.sal()

    def sal(self):
        return float(self.pay_rate) * float(self.hours)

    def detailed_salary(self):
        print('\tPay rate:%5.2f' % float(self.pay_rate), '\n\tHours:%5d' % int(self.hours),
              '\n\tSalary:%5.2f' % float(self.get_salary()))

    def save(self):
        st = super().save()
        st = 'workers' + ' ' + st + ' ' + str(self.pay_rate) + ' ' + str(self.hours)
        return st

    def __repr__(self):
        st = super().__repr__()
        st = st + '  pay_rate: ' + str(self.pay_rate) + '  hours: ' + str(self.hours)
        return st

    def get_pay_rate(self):
        return self.pay_rate

    def get_hours(self):
        return self.hours

    def get_salary(self):
        return self.salary

    def set_pay_rate(self, name):
        if type(name) != int:
            raise TypeError('Enter an integer')
        self.pay_rate = name

    def set_hours(self, name):
        if type(name) != int:
            raise TypeError('Enter an integer')
        self.hours = name

    def set_salary(self, name):
        if type(name) != int:
            raise TypeError('Enter an integer')
        self.salary = name


class traine(Member):

    def __init__(self, name='_', DOB='_', status='_', numOfChildren=-1, DateOfHire='_', DateOfResignation='_',
                 specialist='_', UniversityDegree='_', finished='_', institution='_'):
        super().__init__(name, DOB, status, numOfChildren, DateOfHire, DateOfResignation, specialist, UniversityDegree,
                         finished)
        self.institution = institution
        self.salary = 50

    def sal(self):
        return self.salary

    def detailed_salary(self):
        print('\tSalary:%5d' % self.salary)

    def save(self):
        st = super().save()
        st = 'traine' + ' ' + st + ' ' + self.institution + ' ' + str(self.salary)
        return st

    def __repr__(self):
        st = super().__repr__()
        st = st + '  institution: ' + self.institution + '  salary: ' + str(self.salary)
        return st

    def get_salary(self):
        return self.salary

    def get_institution(self):
        return self.institution

    def set_salary(self, name):
        if type(name) != int:
            raise ValueError('Enter an integer')
        self.salary = name

    def set_institution(self, name):
        if type(name) != str:
            raise ValueError('Enter a text')
        self.institution = name