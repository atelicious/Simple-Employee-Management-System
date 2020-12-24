import sqlite3
from sqlite_functions import *
from employee import Employee

is_playing = True

while is_playing == True:
    print('\n**********Employee Management System**********\n')
    print('                     Menu                     ')
    print('\n1. Create new Employee\n2. Search Employee\n3. Update Employee Details\n4. Delete Employee\n5. Exit\n')

    ans = input('Your choice? (1-5): ')
    if ans == '1':
        print('Create New Employee Profile\n')
        first_name = input('First Name: ').lower().strip()
        last_name = input('Last Name: ').lower().strip()

        try:
            payrate = int(input('Pay: ').strip())
        except ValueError:
            print('Pay should be in whole numbers only.')
            continue

        pos = input('Position: ').lower().strip()
        department = input('Department: ').lower().strip()
        supervisor = input('Supervisor: ').lower().strip()

        new_employee = Employee(first_name, last_name, payrate, pos, department, supervisor)
        insert_emp(new_employee)
        print(f'\nEmployee {new_employee.fullname.title()} successfully created\n')
        
    elif ans == '2':
        print('Search Employee Profile\n')
        print('1. Search by First Name\n2. Search by Last Name\n3. Show all employees\n4. Return to Main Menu\n')
        ans = input('Your choice? (1-4): ').strip()

        if ans == '1':
            name = input('First Name ex. Mary : ').lower().strip()
            names = get_emp_by_first_name(name)

            if not names:
                print(f'\nNo employees found with the first name of {name.title()}')
            else:
                print(f'\nEmployees with First Name of: {name.title()}')
                for values in names:
                    print(f'\nFirst Name: {values[0].title()}')
                    print(f'Last Name: {values[1].title()}')
                    print(f'Pay: {values[2]}')
                    print(f'Position: {values[3].title()}')
                    print(f'Department: {values[4].title()}')
                    print(f'Supervisor: {values[5].title()}\n')

        elif ans == '2':
            name = input('Last Name ex. Sutherland : ').lower().strip()
            names = get_emp_by_last_name(name)
            
            if not names:
                print(f'\nNo employees found with the last name of {name.title()}')
            else:
                print(f'\nEmployees with Last Name of: {name.title()}')
                for values in names:
                    print(f'\nFirst Name: {values[0].title()}')
                    print(f'Last Name: {values[1].title()}')
                    print(f'Pay: {values[2]}')
                    print(f'Position: {values[3].title()}')
                    print(f'Department: {values[4].title()}')
                    print(f'Supervisor: {values[5].title()}\n')


        elif ans == '3':
            list_emp = show_all_emp()
            print('Current Employees in Database:\n')
            for values in list_emp:
                    print(f'\nFirst Name: {values[0].title()}')
                    print(f'Last Name: {values[1].title()}')
                    print(f'Pay: {values[2]}')
                    print(f'Position: {values[3].title()}')
                    print(f'Department: {values[4].title()}')
                    print(f'Supervisor: {values[5].title()}\n')

        elif ans == '4':
            continue

        else:
            print('input not recognized, please try again.')

    elif ans == '3':
        print('Update Employee Details\n')
        first_name = input('First Name ex. Mary : ').lower().strip()
        last_name = input('Last Name ex. Sutherland : ').lower().strip()

        emp = search_employee(first_name, last_name)
        
        if not emp:
            print(f'\nEmployee {first_name.title()} {last_name.title()} not found, please try again.')
        else:
            print(f'\n{first_name.title()} {last_name.title()}\'s Profile')
            print(f'\nFirst Name: {emp[0].title()}\nLast Name: {emp[1].title()}\nCurrent Pay: {emp[2]}')

        print('\nSelect Details to be Updated:\n1. First Name\n2. Last Name\n3. Pay\n4. Position\n5. Department\n6. Supervisor\n')
        ans = input('Your Choice (1-6): ')

        if ans == '1':
            print('\nUpdate Employee\'s First Name\n')

            ans = input(f'\nDo you want to change {first_name.title()} {last_name.title()}\'s First Name? (y/n): ').lower().strip()
            
            if ans == 'y':
                new_first = input('Enter new First Name: ').lower().strip()
                update_first(first_name, last_name, new_first)
                print(f'\n{first_name.title()} {last_name.title()}\'s succesfully changed from {emp[0]} to {new_first}')

            elif ans == 'n':
                continue

        elif ans == '2':
            pass
        
        elif ans == '3':
            print('Update Employee Pay\n')
            emp = search_employee(first_name, last_name)
            
            ans = input(f'\nDo you want to change {first_name.title()} {last_name.title()}\'s Pay? (y/n): ').lower().strip()

            if ans.lower() == 'y':
                try:
                    pay = int(input('Updated Pay: ').strip())
                except ValueError:
                    print('Updated Pay should be in whole numbers only')
                    continue

                update_pay(first_name, last_name, pay)
                print(f'\n{first_name.title()} {last_name.title()}\'s succesfully changed from {emp[2]} to {pay}')
            elif ans.lower() == 'n':
                break

        elif ans == '4':
            pass

        elif ans == '5':
            pass

        elif ans == '6':
            pass

    elif ans == '4':
        print('Delete Employee \n')
        list_emp = show_all_emp()
        print('Current Employees in Database: \n')
        for values in list_emp:
            print(f'\nFirst Name: {values[0].title()}')
            print(f'Last Name: {values[1].title()}')
            print(f'Pay: {values[2]}')
            print(f'Position: {values[3].title()}')
            print(f'Department: {values[4].title()}')
            print(f'Supervisor: {values[5].title()}\n')
        
        ans = input('Delete a Profile? (y/n): ').lower().strip()

        if ans.lower() == 'y':
            first_name = input('First Name ex. Mary : ').lower().strip()
            last_name = input('Last Name ex. Sutherland : ').lower().strip()
            emp = search_employee(first_name, last_name)
            if not emp:
                print(f'\nEmployee {first_name} {last_name} not found, please try again.')
            else:
                print(f'\n{first_name.title()} {last_name.title()}\'s Profile')
                print(f'\nFirst Name: {emp[0]}\nLast Name: {emp[1]}\nCurrent Pay: {emp[2]}')

        elif ans.lower() == 'n':
            continue

        ans = input(f'\nDo you want to delete {first_name.title()} {last_name.title()}\'s profile? (y/n): ').lower().strip()

        if ans.lower() == 'y':
            remove_emp(first_name, last_name)
            print(f'\n{first_name.title()} {last_name.title()}\'s profile succesfully deleted.')
        elif ans.lower() == 'n':
            break  
    
    elif ans == '5':
        print('Logging out......')
        is_playing = False
        conn.close()
        break
    else:
        print('Invalid Choice, Please try again.\n')



