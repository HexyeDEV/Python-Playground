# There is no need to create a class this could just be static methods,
# I did this way just to get more comfortable with OOP in Python

import users.user as model
import notes.actions

class Actions:

    def register(self):

        print("Great! Let's create an account for you...")

        name = input("Type your name please: ")
        surname = input("Type your surname please: ")
        email = input("Type your email please: ")
        password = input("Type your password please: ")

        user = model.User(name, surname, email, password)
        register = user.register()

        if register[0] >= 1:
            print(f"Perfect! {register[1].name} you are registered with the email: {register[1].email}")
            self.nextActions(register)
        else:
            print("There was an issue with your register, please try again.")

    def login(self):

        print("Great! Please identify yourself")

        try:
            email = input("Type your email please: ")
            password = input("Type your password please: ")

            user = model.User("", "", email, password)
            login = user.identify()

            if email == login[3]:
                print(f"Welcome {login[1]}!")
                self.nextActions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("There was an issue with your login, please try again.")


    def nextActions(self, user):

        print("""
            Available actions:
            - Create notes (create)
            - Show notes (show)
            - Delete note (delete)
            - Exit (exit)
        """)

        action = input("What do you want to do? ")
        do = notes.actions.Actions()

        if action == "create":
            do.create(user)
            self.nextActions(user)

        elif action == "show":
            do.show(user)
            self.nextActions(user)

        elif action == "delete":
            do.delete(user)
            self.nextActions(user)

        elif action == "exit":
            print(f"Ok {user[1]}, see you soon!")
            exit()
