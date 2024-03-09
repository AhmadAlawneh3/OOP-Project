import classes
from classes import Member, workers, traine, regular_employees

PASSWORD_FLAG = False
CORRECTPASS = False
MEMBERS = []

def load():
    global MEMBERS

    with open('test.txt', 'r') as infile:
        for line in infile:
            line = line.split()
            if line[0] == 'traine':
                MEMBERS.append(traine(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                                      line[10]))
            elif line[0] == 'workers':
                MEMBERS.append(workers(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                                       line[10], line[11]))
            elif line[0] == 'Regular_employees':
                MEMBERS.append(regular_employees(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                                                 line[9]))

def save_and_exit():
    global MEMBERS
    with open('save.txt', 'w') as outfile:
        for obj in MEMBERS:
            outfile.write(obj.save()+'\n')
    exit()

def search(key, value, job = 'none'):# this is done no nead to change anything
    global MEMBERS
    new = []

    if job == 'none':
        for obj in MEMBERS:
            if isinstance(obj, Member):
                if key != 'name':
                    if value.lower() in obj.__dict__.get(key).lower()  :
                        new.append(obj)
                else:
                    name_list = obj.__dict__.get(key)
                    if value.lower() in name_list[0].lower() +' '+ name_list[1].lower() +' '+ name_list[2].lower():
                        new.append(obj)
    else:
        job = traine if job == '<class \'classes.traine\'>' else workers if job == '<class \'classes.workers\'>' else\
            regular_employees
        for obj in MEMBERS:
            if isinstance(obj, job):
                if key != 'name':
                    if value.lower() in obj.__dict__.get(key).lower():
                        new.append(obj)
                else:
                    name_list = obj.__dict__.get(key)
                    if value.lower() in name_list[0].lower() + ' ' + name_list[1].lower() + ' ' + name_list[2].lower():
                        new.append(obj)
    return new

def search_menu_job():
    options = ('1', '2', '3', '4', 'q')
    print('-' * 10 + 'search menu' + '-' * 10)
    print('1- Trainers\n2- Workers\n3- Regular employees\n4- All\nQ- Exit')
    choice = input('Choose an option: ')
    while choice.lower() not in options:
        print('invalid option, try again')
        print('-' * 10 + 'search menu' + '-' * 10)
        print('1- Trainers\n2- Workers\n3- Regular employees\n4- All\nQ- Exit')
        choice = input('Choose an option: ')
    if choice.lower() == 'q':
        main_menu()

    if choice == '1':
        choice_type = search_menu_type('<class \'classes.traine\'>')
        job = '<class \'classes.traine\'>'
    elif choice == '2':
        choice_type = search_menu_type('<class \'classes.workers\'>')
        job = '<class \'classes.workers\'>'
    if choice == '3':
        choice_type = search_menu_type('<class \'classes.regular_employees\'>')
        job = '<class \'classes.regular_employees\'>'
    elif choice == '4':
        choice_type = search_menu_type()
        job = 'none'

    return (job, choice_type) # will return the job and choice to manager_choices_menu

def search_menu_type(job = 'none'):
    obj_dic_num = {}

    # to print all atterputes 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧
    print('-' * 10 + 'search_menu' + '-' * 10)
    if job == '<class \'classes.traine\'>':
        obj_dic = traine().__dict__
        print('-' * 10 + 'search menu' + '-' * 10)
        for i, val in enumerate(obj_dic.keys()):
            if i == 10: break
            obj_dic_num[i + 1] = val
            print(str(i + 1) + '- ' + str(val))
    elif job == '<class \'classes.regular_employees\'>':
        obj_dic = regular_employees().__dict__
        print('-' * 10 + 'search menu' + '-' * 10)
        for i, val in enumerate(obj_dic.keys()):
            if i == 17: break
            obj_dic_num[i + 1] = val
            print(str(i + 1) + '- ' + str(val))
    elif job == '<class \'classes.workers\'>':
        obj_dic = workers().__dict__
        print('-' * 10 + 'search menu' + '-' * 10)
        for i, val in enumerate(obj_dic.keys()):
            if i == 11:break
            obj_dic_num[i + 1] = val
            print(str(i+1)+'- '+str(val))
    elif job == 'none':
        obj_dic = classes.Member().__dict__
        print('-' * 10 + 'search menu' + '-' * 10)
        for i, val in enumerate(obj_dic.keys()):
            if i == 11: break
            obj_dic_num[i + 1] = val
            print(str(i + 1) + '- ' + str(val))
    #🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧

    # to ask the user what is he looking for 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
    choice = input('What are you looking for: ')
    while choice.lower() not in str(obj_dic_num.keys()) and choice.lower() != 'q':
        print('invalid option, try again')
        for i, val in enumerate(obj_dic.keys()):
            if i == 11: break
            obj_dic_num[i + 1] = val
            print(str(i + 1) + '- ' + str(val))
        choice = input('What are you looking for: ')
    if choice.lower() == 'q':
        main_menu()
    # 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

    return obj_dic_num.get(int(choice))  # will return the type to search_menu_job

def edit_print_obj(choice_type, job):# this will be called after manager_choices_menu calls search_menu_job
    value = input('what value are you looking for? ')
    wanted_obj = search(choice_type, value, job)

    print('-' * 10 + 'manager menu' + '-' * 10)
    print('Search results:')
    for i, val in enumerate(wanted_obj):
        print(str(i + 1) + '- ' + str(val))

    obj_choice = input('which one do u wanna change or Q to Exit: ')
    while int(obj_choice.lower()) not in (range(len(wanted_obj)+1)):
        print('invalid option, try again')
        for i, val in enumerate(wanted_obj):
            print(str(i + 1) + '- ' + str(val))
        obj_choice = input('which one do u wanna change or Q to Exit : ')
    if obj_choice.lower() == 'q':
        manager_choices_menu()

    new_val = input('What do you want to set it to: ')
    setattr(wanted_obj[int(obj_choice) - 1], choice_type, new_val if choice_type != 'name' else new_val.split())
    print('Edited!')

def edit_main_vars():
    global MEMBERS
    regular_employe_obj = regular_employees()
    my_list = list(regular_employe_obj.__dict__)
    print('-' * 10 + 'manager menu' + '-' * 10)
    for i, st in enumerate(my_list[::-1]):
        if i == 8:
            break
        print(str(i+1) +'- '+ st)
    options = [str(i) for i in range(1, 9)]
    options_names = {i:j for i, j in enumerate(my_list[::-1])}
    choice = input('which one do you want to change? ')
    while choice.lower() not in options:
        print('invalid option, try again')
        for i, st in enumerate(my_list[::-1]):
            if i == 8:
                break
            print(str(i + 1) + '- ' + st)

        choice = input('which one do you want to change? ')
        if choice.lower() == 'q':
            break

    print(f'curent value:\n{options_names.get((int(choice)-1))}:'
          f' {getattr(regular_employe_obj, options_names.get((int(choice)-1)))}')
    print(f'new value:\n{options_names.get((int(choice) - 1))}:',end=' ')
    new_val = input()

    for obj in MEMBERS:
        if isinstance(obj, regular_employees):
            setattr(obj, options_names.get((int(choice) - 1)), new_val)

def main_menu():
    options = ('1', '2', 'q')
    print('-'*10 + 'main menu'+ '-'*10)
    print('1- Manager\n2- User\nQ- Exit')
    choice = input('Choose an option: ')
    while choice.lower() not in options:
        print('invalid option, try again')
        print('-'*10 + 'main menu'+ '-'*10+'\n1- Manager\n2- User\nQ- Exit')
        choice = input('Choose an option: ')
        if choice.lower() == 'q':
            break

    if choice == '1':
        manager_menu()
    elif choice == '2':
        user_menu()

def manager_menu(): # this is only for the password
    counter = 0
    global PASSWORD_FLAG
    global CORRECTPASS
    print('-' * 10 + 'manager menu' + '-' * 10)
    if not PASSWORD_FLAG :
        password = input('Enter the password: ')
    while not PASSWORD_FLAG :
        if CORRECTPASS:
            break

        if password == '123':
            manager_choices_menu()
            CORRECTPASS = True
        elif counter > 1:
            PASSWORD_FLAG = True
            main_menu()
        elif password != '123':
            print('Wrong password!')
            print('-' * 10 + 'manager menu' + '-' * 10)
            password = input('Enter the password : ', )
            counter += 1
    if PASSWORD_FLAG:
        print('You can\'t login')
        main_menu()

def manager_choices_menu(): # after manager_menu
    choice = ''
    while choice.lower() != 'q':
        options = ('1', '2', '3', '4', '5', '6', '7', '8', 'q')
        print('-' * 10 + 'manager menu' + '-' * 10 + '\n1- Search\n2- Edit main vars\n3- Add member\n'
              '4- Employee name with the highest salary\n5- Financial report' +
              'of the month\n6- Full report\n7- Delete member\nQ- Exit')
        choice = input('Choose an option: ')
        while choice.lower() not in options:
            print('invalid option, try again')
            print('-' * 10 + 'manager menu' + '-' * 10 + '\n1- Search\n2- Edit main vars\n3- Add member\n'
                '4- Employee name with the highest salary\n5- Financial report' +
                'of the month\n6- Full report\n7- Delete member\nQ- Exit')
            choice = input('Choose an option: ')
        if choice == '1':
            job, choice_type = search_menu_job()
            edit_print_obj(choice_type, job)
        elif choice == '2':
            edit_main_vars()  # choce which var to adit
        elif choice == '3':
            add_member()
        elif choice == '4':
            highest_salary()
        elif choice == '5':
            financial_report()
        elif choice == '6':
            full_report()
        elif choice == '7':
            delete_member()

    save_and_exit()

def add_member():
    global MEMBERS
    # display members types
    print('-' * 10 + 'add' + '-' * 10)
    print('What type of member you want to add?')
    print('1- workers\n2- Trainee\n3- Regular employees\nQ- Quit')
    choice = input('Choose an option: ')
    # check for valid options
    options = ('1', '2', '3', 'q')
    while choice.lower() not in options:
        print('invalid option, try again')
        print('-' * 10 + 'user menu' + '-' * 10 + '\n1- workers\n2- Traine\n3- Regular_employees\n')
        choice = input('Choose an option: ')
        if choice.lower() == 'q':
            break
    # action
#1️⃣
    if choice == '1':
        print('-' * 10 + 'Adding Worker' + '-' * 10)
        name = input('Name:')
        name = name.split()
        for i in name:
            while i.isalpha()==False :
                name = input('Name(Characters only):')
            

        print('Date of birth:')

        day=input('\tDay:')
        while day.isdigit()==False :
            day=input('\tDay(Numbers only):')
        while int(day)>31:
            day=input('\tDay(Should be less than or equal to 31):') 
          
        month=input('\tMonth:')
        while month.isdigit()==False:
            month=input('\tMonth(Numbers only):')
        while  int(month)>12:
            month=input('\tMonth(Should be less than or equal to 12):')

        year=input('\tYear:')
        while  year.isdigit()==False:
            year=input('\tYear(Numbers only):')
        while int(year)<1900 or int(year)>2023:#approximation
            year=input('\tYear(Should be greater than or equal to 1900):')

        DOB=day+'/'+month+'/'+year

        status = input('Status(married/single):')
        if status == 'married':
            numofchildren = input('Number of children:')
        else:
            numofchildren = 0

        print('Date of hire:')
        
        hday=input('\tDay:')
        while hday.isdigit()==False :
            hday=input('\tDay(Numbers only):')
        while int(hday)>31:
            hday=input('\tDay(Should be less than or equal to 31):') 
          
        hmonth=input('\tMonth:')
        while hmonth.isdigit()==False:
            hmonth=input('\tMonth(Numbers only):')
        while  int(hmonth)>12:
            hmonth=input('\tMonth(Should be less than or equal to 12):')

        hyear=input('\tYear:')
        while  hyear.isdigit()==False:
            hyear=input('\tYear(Numbers only):')
        while int(hyear)<1900 or int(hyear)>2023:#approximation
            hyear=input('\tYear(Should be greater than or equal to 1900):')

        dateofhire=hday+'/'+hmonth+'/'+hyear
           
        finished = input('Finished (True/False):')
        finished=finished[0].upper()+finished[1:]
        if finished=='True':
            print('Date of resignation:')
            rday=input('\tDay:')
            while rday.isdigit()==False :
                rday=input('\tDay(Numbers only):')
            while int(rday)>31:
                rday=input('\tDay(Should be less than or equal to 31):') 
            
            rmonth=input('\tMonth:')
            while rmonth.isdigit()==False:
                rmonth=input('\tMonth(Numbers only):')
            while  int(rmonth)>12:
                rmonth=input('\tMonth(Should be less than or equal to 12):')

            ryear=input('\tYear:')
            while  ryear.isdigit()==False:
                ryear=input('\tYear(Numbers only):')
            while int(ryear)<1900 or int(ryear)>2023:#approximation
                ryear=input('\tYear(Should be greater than or equal to 1900):')

            dateOfRes=rday+'/'+rmonth+'/'+ryear
        else:
            dateOfres='--/--/----'

        specialist = input('Specialist:')
        degree = input('Degree (Diploma/BSc/Master/Ph.D):')                                                   
        payRate = input('Enter pay rate:')
        hours = input('Hours:')
        name = name[0] + '_' + name[1] + '_' + name[2]
        MEMBERS.append(
            workers(name, DOB, status, numofchildren, dateofhire, dateOfres, specialist, degree, finished, payRate,
                    hours))
#2️⃣
    elif choice == '2':
        print('-' * 10 + 'Adding Trainee' + '-' * 10)
        name = input('Name:')
        name = name.split()
        for i in name:
            while i.isalpha()==False :
                name = input('Name(Characters only):')
            

        print('Date of birth:')

        day=input('\tDay:')
        while day.isdigit()==False :
            day=input('\tDay(Numbers only):')
        while int(day)>31:
            day=input('\tDay(Should be less than or equal to 31):') 
          
        month=input('\tMonth:')
        while month.isdigit()==False:
            month=input('\tMonth(Numbers only):')
        while  int(month)>12:
            month=input('\tMonth(Should be less than or equal to 12):')

        year=input('\tYear:')
        while  year.isdigit()==False:
            year=input('\tYear(Numbers only):')
        while int(year)<1900 or int(year)>2023:#approximation
            year=input('\tYear(Should be greater than or equal to 1900):')

        DOB=day+'/'+month+'/'+year
        status = input('Status(married/single):')
        if status == 'married':
            numofchildren = input('Number of children:')
        else:
            numofchildren = 0

        
        print('Date of hire:')
        
        hday=input('\tDay:')
        while hday.isdigit()==False :
            hday=input('\tDay(Numbers only):')
        while int(hday)>31:
            hday=input('\tDay(Should be less than or equal to 31):') 
          
        hmonth=input('\tMonth:')
        while hmonth.isdigit()==False:
            hmonth=input('\tMonth(Numbers only):')
        while  int(hmonth)>12:
            hmonth=input('\tMonth(Should be less than or equal to 12):')

        hyear=input('\tYear:')
        while  hyear.isdigit()==False:
            hyear=input('\tYear(Numbers only):')
        while int(hyear)<1900 or int(hyear)>2023:#approximation
            hyear=input('\tYear(Should be greater than or equal to 1900):')

        dateofhire=hday+'/'+hmonth+'/'+hyear

        finished = input('Finished (True/False):')
        finished=finished[0].upper()+finished[1:]
        if finished=='True':
            print('Date of resignation:')
        
            rday=input('\tDay:')
            while rday.isdigit()==False :
                rday=input('\tDay(Numbers only):')
            while int(rday)>31:
                rday=input('\tDay(Should be less than or equal to 31):') 
            
            rmonth=input('\tMonth:')
            while rmonth.isdigit()==False:
                rmonth=input('\tMonth(Numbers only):')
            while  int(rmonth)>12:
                rmonth=input('\tMonth(Should be less than or equal to 12):')

            ryear=input('\tYear:')
            while  ryear.isdigit()==False:
                ryear=input('\tYear(Numbers only):')
            while int(ryear)<1900 or int(ryear)>2023:#approximation
                ryear=input('\tYear(Should be greater than or equal to 1900):')

            dateOfRes=rday+'/'+rmonth+'/'+ryear
        else:
            dateOfres='--/--/----'

        
        specialist = input('Specialist:')
        degree = input('Degree (Diploma/BSc/Master/Ph.D):')
        institution = input('Name of institution:')
        name = name[0] + '_' + name[1] + '_' + name[2]
        MEMBERS.append(
            traine(name, DOB, status, numofchildren, dateofhire, dateOfres, specialist, degree, finished, institution))
#3️⃣            
    elif choice == '3':
        print('-' * 10 + 'Adding regular employe' + '-' * 10)
        name = input('Name:')
        name = name.split()
        for i in name:
            while i.isalpha()==False :
                name = input('Name(Characters only):')
            

        print('Date of birth:')

        day=input('\tDay:')
        while day.isdigit()==False :
            day=input('\tDay(Numbers only):')
        while int(day)>31:
            day=input('\tDay(Should be less than or equal to 31):') 
          
        month=input('\tMonth:')
        while month.isdigit()==False:
            month=input('\tMonth(Numbers only):')
        while  int(month)>12:
            month=input('\tMonth(Should be less than or equal to 12):')

        year=input('\tYear:')
        while  year.isdigit()==False:
            year=input('\tYear(Numbers only):')
        while int(year)<1900 or int(year)>2023:#approximation
            year=input('\tYear(Should be greater than or equal to 1900):')

        DOB=day+'/'+month+'/'+year
        status = input('Status(married/single):')
        if status == 'married':
            numofchildren = input('Number of children:')
        else:
            numofchildren = 0
        
        print('Date of hire:')
        
        hday=input('\tDay:')
        while hday.isdigit()==False :
            hday=input('\tDay(Numbers only):')
        while int(hday)>31:
            hday=input('\tDay(Should be less than or equal to 31):') 
          
        hmonth=input('\tMonth:')
        while hmonth.isdigit()==False:
            hmonth=input('\tMonth(Numbers only):')
        while  int(hmonth)>12:
            hmonth=input('\tMonth(Should be less than or equal to 12):')

        hyear=input('\tYear:')
        while  hyear.isdigit()==False:
            hyear=input('\tYear(Numbers only):')
        while int(hyear)<1900 or int(hyear)>2023:#approximation
            hyear=input('\tYear(Should be greater than or equal to 1900):')

        dateofhire=hday+'/'+hmonth+'/'+hyear

        finished = input('Finished (True/False):')
        finished=finished[0].upper()+finished[1:]
        if finished=='True':
            print('Date of resignation:')
        
            rday=input('\tDay:')
            while rday.isdigit()==False :
                rday=input('\tDay(Numbers only):')
            while int(rday)>31:
                rday=input('\tDay(Should be less than or equal to 31):') 
            
            rmonth=input('\tMonth:')
            while rmonth.isdigit()==False:
                rmonth=input('\tMonth(Numbers only):')
            while  int(rmonth)>12:
                rmonth=input('\tMonth(Should be less than or equal to 12):')

            ryear=input('\tYear:')
            while  ryear.isdigit()==False:
                ryear=input('\tYear(Numbers only):')
            while int(ryear)<1900 or int(ryear)>2023:#approximation
                ryear=input('\tYear(Should be greater than or equal to 1900):')

            dateOfRes=rday+'/'+rmonth+'/'+ryear
        else:
            dateOfres='--/--/----'
        specialist = input('Specialist:')
        degree = input('Degree (Diploma/BSc/Master/Ph.D):')
        name = name[0] + '_' + name[1] + '_' + name[2]
        MEMBERS.append(
            regular_employees(name, DOB, status, numofchildren, dateofhire, dateOfres, specialist, degree, finished))

def delete_member():
    global MEMBERS
    job, choice_type = search_menu_job()
    value = input('what value are you looking for? ')
    wanted_obj = search(choice_type, value, job)
    print('-' * 10 + 'delete menu' + '-' * 10)
    print('Search results:')
    for i, val in enumerate(wanted_obj):
        print(str(i + 1) + '- ' + str(val))

    obj_choice = input('which one do u wanna delete or Q to Exit: ')


    while obj_choice >= str(len(wanted_obj) + 1)  and obj_choice.lower() != 'q':
        print('Invalid input!')
        for i, val in enumerate(wanted_obj):
            print(str(i + 1) + '- ' + str(val))

        obj_choice = input('which one do u wanna delete or Q to Exit: ')
    if obj_choice.lower() == 'q':
        main_menu()

    MEMBERS.remove(wanted_obj[int(obj_choice) - 1])

def highest_salary():
    global MEMBERS
    max = 0
    for i in MEMBERS:
        if float(i.get_salary()) > max:
            max = i.get_salary()
            name = i.get_name()
    print(f'{name[0]} {name[1]} {name[2]} tkes the highest salary ', max)

def financial_report():
    print('#' * 10, 'Financial report', '#' * 10)
    global MEMBERS
    total_salaries = 0
    for i in MEMBERS:
        total_salaries += float(i.get_salary())
        name = i.get_name()
        print(name[0] + ' '+name[1] +' '+ name[2])
        i.detailed_salary()
        print('*' * 10)
    print('Total salaries', total_salaries)

def full_report():
    global MEMBERS
    print('-' * 10, 'Categories', '-' * 10)
    print('1- Trainers\n2- Workers\n3- Regular employees\n4- All\nQ- Exit')
    choice = input('Choose category:')
    print('*' * 100)
    options = ('1', '2', '3', '4', 'q')
    while choice.lower() not in options:
        print('invalid option, try again')
        print('1- Trainers\n2- Workers\n3- Regular employees\n4- All\nQ- Exit')
        choice = input('Choose an option: ')
        print('*' * 100)

    if choice == '1':
        for i in MEMBERS:
            if isinstance(i, traine):
                print(i)
                print('*' * 100)
    if choice == '2':
        for i in MEMBERS:
            if isinstance(i, workers):
                print(i)
                print('*' * 100)
    if choice == '3':
        for i in MEMBERS:
            if isinstance(i, regular_employees):
                print(i)
                print('*' * 100)
    if choice == '4':
        for i in MEMBERS:
            print(i)
            print('*' * 100)

def user_menu():
    choice = ''
    while choice.lower() != 'q':
        print('-' * 10 + 'User menu' + '-' * 10)
        print("1- Add member")
        print('2- Search')
        print('3- Employee name with the highest salary')
        print("4- Financial report of the month")
        print('5- Full report')
        print('6- Delete member')
        print('Q- Save and quit')
        choice = input('Choose an option: ')
        options = ('1', '2', '3', '4', '5', '6', 'q')
        while choice.lower() not in options:
            print('invalid option, try again')
            print(
                '-' * 10 + 'user menu' + '-' * 10 + '\n1- Add member\n2- Search\n3- Employee name with the highest salary\n4- Financial report' + \
                'of the month\n5- Full report\n6- Delete member\nQ- Exit')
            choice = input('Choose an option: ')

        if choice == '1':
            add_member()
        elif choice == '2':
            job, choice_type = search_menu_job()
            value = input('what value are you looking for? ')
            wanted_obj = search(choice_type, value, job)
            for i, val in enumerate(wanted_obj):
                print(str('*'*100 +'\n'+ str(val)))
        elif choice == '3':
            highest_salary()
        elif choice == '4':
            financial_report()
        elif choice == '5':
            full_report()
        elif choice == '6':
            delete_member()
    if choice.lower() == 'q':
        save_and_exit()

def main():
    global MEMBERS
    load()
    main_menu()
    # print(MEMBERS[0].get_name())

main()

