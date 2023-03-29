"""
Write a c++ code for a gym management system.
The system should have user and admin login options. The users can enter their details
(name, contact information, gym member number, training time and gym
membership i.e. gold, silver, platinum or beginner) , make payments and see their workout plans.
It should also have an admin function to access and edit user data and monitor equipment inventor.
The system should also display the user details.
"""
import json  # This is used as a DB, for storing Logins and general credentials.
import random  # This module is to assist in generating random membership numbers.
import time  # This library is imported to enhance counters.


def logged_in_admin():
    # Activities that an Admin can do while Logged in His/Her account
    pass


def admin():
    # Requesting for the Admin's Details for verification.
    def load_admin_data():
        # Loading the data from JSON file.
        filename = "AdminLoginCredentials.json"
        with open(filename) as f_obj:
            data = json.load(f_obj)
            print("\nWelcome to Admin Page.")
            req_admin_adminnumber = str(input("Enter Admin Number: "))
            req_admin_password = str(input("Enter Password: "))
            if req_admin_adminnumber == data["adminnumber"] and \
                    req_admin_password == data['password']:
                print(f"\nWelcome {data['name'].title()}\nYou are logged in as Admin")
            else:
                print("Password or Admin Number Mismatch")
                general_requests()

    load_admin_data()

    # Activities that an Admin can do after Logging in.
    print("\nAdmin Page")
    activities = {
        1: "Add Participants.",
        2: "Remove Participants",
        3: "View all Participants",
        4: "Edit Users' Data",
        5: "Monitor Equipment"
    }
    for k, v in activities.items():
        print(f"\n{k}:", end="\t")
        print(f"\b{v}")


def logging_in_user():
    # Actions that a logging in user can do.
    filename = 'LoginCredentials.json'
    with open(filename) as f_obj:
        data = json.load(f_obj)
        print("\nInsert your Credentials to Log in.")
    req_gymmembernumber = int(input("Enter Your Gym Membership Number: "))
    req_password = input("Enter Password: ")
    if req_gymmembernumber == data["gymmembernumber"] and \
            req_password == data["password"]:
        print("You are Logged in.")
        workout_plans()
    elif req_gymmembernumber != data["gymmembernumber"] and \
            req_password != data["password"]:
        print("The credentials do not match.")
        logging_in_user()
    else:
        logging_in_user()


def workout_plans():
    # Table/ Plans of workouts
    def load_stored_data():
        # This is to load all data that is stored in the JSON file
        filename = "LoginCredentials.json"
        with open(filename) as f_obj:
            data = json.load(f_obj)

        print(f"\nAll the Workout Plans for {data['name']}")

    load_stored_data()
    table_of_workouts = {
        "Time": "\t\t\t\tActivities",
        "9:00a.m. - 11:00a.m.": ["A", "B", "C"],
        "11:00a.m. - 11:15a.m.": "Water Break",
        "11:15a.m. - 01:15p.m.": ["D", "E", "F"],
        "01:15p.m. - 01:45p.m.": "Lunch",
        "01:45p.m. - 03:45p.m.": ["G", "H", "I"],
        "03:45p.m. - __:__": "Personal Programs"
    }
    for k, v in table_of_workouts.items():
        print(f"\n{k}", end="")
        print(f"\t\t{v}")
    time.sleep(10)
    print("You have 10 seconds to revise your first Activity.")
    time.sleep(10)
    print("Have a Nice Training Session. Bye Bye!!")
    time.sleep(5)
    general_requests()


def signing_up_user():
    users_credentials_dictionary = {}
    # Actions that a Signing up User can do.
    print("\nInsert your Details to Register.")
    req_name = input("Enter your Name: ")
    users_credentials_dictionary["name"] = f"{req_name}"
    req_password = input("Enter Password: ")
    users_credentials_dictionary["password"] = req_password
    req_email = input("Enter Email: ")
    users_credentials_dictionary["email"] = req_email
    req_phonenumber = int(input("Enter Phone Number: "))
    users_credentials_dictionary["phonenumber"] = req_phonenumber

    # Generating a Random Gym Member Number for each member that Signs up
    generate_randN = random.randint(3001, 9999)
    req_gymmembernumber = generate_randN
    print(f"Your Gym Membership Number is {req_gymmembernumber}")
    users_credentials_dictionary["gymmembernumber"] = req_gymmembernumber

    # List of all the gym levels that are available.
    print("\nGym Levels available...")
    list_of_gym_levels = ["gold", "silver", "platinum", "beginner"]
    count = 0
    for i in list_of_gym_levels:
        print(f"{count + 1}.) {i.title()}")
        count += 1

    counting = 1
    anotherCounter = 4
    while counting <= 4:
        req_gymstatus = int(input("\nWhich Gym Level do you want to start with: "))
        try:
            if req_gymstatus <= 0:
                if anotherCounter == 1:
                    print(f"{anotherCounter - 1} Chances remaining:\tIndex out of Range")
                elif anotherCounter > 1:
                    print(f"{anotherCounter - 1} Chance remaining:\tIndex out of Range")
                if counting == 4:
                    user()
                counting += 1
                anotherCounter -= 1
            elif req_gymstatus == 1 or 2 or 3 or 4:
                print(f"You are about to Start your {list_of_gym_levels[req_gymstatus - 1].upper()} Level")
                users_credentials_dictionary["gymstatus"] = list_of_gym_levels[req_gymstatus - 1].title()
                break
        except IndexError:
            if anotherCounter == 1:
                print(f"{anotherCounter - 1} Chances remaining:\tIndex out of Range")
            elif anotherCounter > 1:
                print(f"{anotherCounter - 1} Chance remaining:\tIndex out of Range")
            if counting == 4:
                user()
            counting += 1
            anotherCounter -= 1
    print(f"\nWelcome {req_name.title()} for a {list_of_gym_levels[req_gymstatus - 1].upper()} session")

    # Function to make payments.
    def payments():
        if list_of_gym_levels[req_gymstatus - 1].upper() == list_of_gym_levels[0].upper():
            print(f"\n{list_of_gym_levels[0].upper()}: ${900}")
            users_credentials_dictionary["payments"] = f"${900}"
            workout_plans()
        elif list_of_gym_levels[req_gymstatus - 1].upper() == list_of_gym_levels[1].upper():
            print(f"\n{list_of_gym_levels[0].upper()}: ${700}")
            users_credentials_dictionary["payments"] = f"${700}"
            workout_plans()
        elif list_of_gym_levels[req_gymstatus - 1].upper() == list_of_gym_levels[2].upper():
            print(f"\n{list_of_gym_levels[0].upper()}: ${500}")
            users_credentials_dictionary["payments"] = f"${500}"
            workout_plans()
        elif list_of_gym_levels[req_gymstatus - 1].upper() == list_of_gym_levels[3].upper():
            print(f"{list_of_gym_levels[0].upper()}: ${300}")
            users_credentials_dictionary["payments"] = f"${300}"
            workout_plans()
        else:
            user()

    payments()
    # print(users_credentials_dictionary)
    filename = 'LoginCredentials.json'
    with open(filename, 'w') as f_obj:
        json.dump(users_credentials_dictionary, f_obj)


def user():
    # Requesting for a User's Details for verification.
    list_of_actions = ["Log in", "Register"]
    count = 0
    print("Welcome to the User Page.")
    for i in list_of_actions:
        print(f"{count + 1}.) {i.title()}")
        count += 1

    logging_in_or_signing_up = input("Log in or Sign Up: ")
    if logging_in_or_signing_up == f"{1}":
        logging_in_user()
    elif logging_in_or_signing_up == f"{2}":
        signing_up_user()
    else:
        user()


def general_requests():
    list_of_users = ["admin", "user"]
    print("Choose a number for effective responses.")
    count = 0
    for i in list_of_users:
        print(f"{count + 1}.) {i.title()}")
        count += 1

    request_current_user = input("Log in as: ")

    if request_current_user == list_of_users[0] or request_current_user == f'{1}':
        admin()
    elif request_current_user == list_of_users[1] or request_current_user == f'{2}':
        user()
    else:
        general_requests()


if __name__ == "__main__":
    general_requests()
