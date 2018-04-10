#!/usr/bin/python3

'''

timeClock.py - Asks for the users name, then records their clock-in time.
               The next time that name is typed, that person will be clocked-out.
               This information is saved as a JSON file that is imported/exported when
               the program is closed.

Verson 1

TODO: Allow employees to clock in with a PIN instead of their name.

    - Add an Admin Panel
        - Admin panel should be password protected
            - Allows the admin to create employees and login PINs
            - Employer can 0 out the employee's hours worked and export the info
                - Maybe set this up to do automatically each week?
            - Learn more about encryption.

    - Add logging of who clocked in/out and when
    - Eventually add a GUI

Author: Patrick Coyle
Last Edited: 4-10-2018

'''

import time, json, os.path, sys

def clock_in_or_out(recorded_time):

    print(recorded_time['Patrick Coyle'])
    
    while True:

        # while loop used so the user can keep clocking people in/out until
        # they decide to stop.

        try: 

            person = input('Type your name to clock in or out: ')

        except KeyboardInterrupt:

            print('Please type exit to close.')
            
            continue
      
        if person == 'exit':

            # When exit is typed, the dictionary storing the clock is exported to a text file as JSON
            # After which, the program is closed.

            with open('employee_hours.txt', 'w') as to_save:
            
                json.dump(recorded_time, to_save)
        
                sys.exit(0)
      
        exists = recorded_time.get(person, None)
        # Checks to see if the employee is already in the dict or not.
        # If they are not, an entry is created.
      
        if exists == None:
        
            worker_info = {'totalHours': 0, 'clockedIn': False, 'lastClockInTime': 0}
        
            # True is clocked in, False is clocked out.
        
            recorded_time[person] = worker_info.copy()
            
            # Creates a copy otherwise the original is modified.

        employee = recorded_time[person]
        # stored as employee to make code clearer

        work_status = employee['clockedIn']

        if work_status == False:

            employee['lastClockInTime'] = time.time()

            employee['clockedIn'] = True

            print('{} was clocked in.'.format(person))
        
            # clocks the person in and records their clock in time.
      
        else:

            startTime = employee['lastClockInTime']
        
            clockOut = time.time()
      
            hoursWorked = (clockOut - startTime) / 60 / 60
            # (clockOut - startTime)/60/60 gives the time in hours.
            # the first 60 converts seconds to minutes and the second converts
            # minutes to hours.
        
            employee['totalHours'] += hoursWorked
      
            print('{} was clocked in for {} hours.'
              .format(person, round(hoursWorked, 2)))
            # hoursWorked is rounded for readability
            # Note that hoursWorked isn't stored as a rounded number so the
            # time an employee works is very precise
        
            print('{} has worked a total of {} hours'
              .format(person, round(employee['totalHours'], 2)))
        
            print('Type exit to close the time clock.\n')

            recorded_time[person]['clockedIn'] = False
            recorded_time[person]['lastClockInTime'] = 0
            
def load():
    
    try:

        if os.path.exists('employee_hours.txt') == True:

            # If employee_hours.txt already exists, then it is loaded.

            with open('employee_hours.txt', 'r') as to_load:

                recorded_time = json.load(to_load)
                
                # Dictionary that holds the total hours each person who
                # clocks in has worked.

        else:

            recorded_time = {}

            # If it doesn't exist, an empty dictionary is created instead.

    except AttributeError:

        recorded_time = {}

        # In case of an empty file named employee_hours,
        # This uses an empty dictionary instead of the empty JSON file.

    clock_in_or_out(recorded_time)

if __name__ == '__main__':

    load()

    
