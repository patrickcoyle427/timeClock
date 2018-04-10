# timeClock

timeClock.py - Asks for the users name, then records their clock-in time.
               The next time that name is typed, that person will be clocked-out.
               This information is saved as a JSON file that is imported/exported when
               the program is closed.

Verson 1

TODO: 
    - Allow employees to clock in with a PIN instead of their name.
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
