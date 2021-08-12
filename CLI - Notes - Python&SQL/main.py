# CLI program for taking notes

from users import actions

print("""
    Available actions:
        - Register
        - Login
""")

actions = actions.Actions()
action = input("What do you want to do? ")

if action.lower() == "register":

    actions.register()

elif action.lower() == "login":

    actions.login()
