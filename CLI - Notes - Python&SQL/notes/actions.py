import notes.note as model

class Actions:

    def create(self, user):
        print(f"Ok {user[1]}! Let's create a new note...")
        title = input("Type your note title: ")
        content = input("Type your note content: ")

        note = model.Note(user[0], title, content)
        save = note.save()

        if save[0] >= 1:
            print(f"Your note {note.title} was saved successfully!")

        else:
            print("There was an issue, note not saved successfully, please try again.")

    def show(self, user):
        print(f"Ok {user[1]}... here are your notes!")

        note = model.Note(user[0])
        notes = note.show()

        for note in notes:
            print("********************************************")
            print(note[2])
            print(note[3])
            print("********************************************\n")

    def delete(self, user):
        print(f"Ok {user[1]}... lets delete the note.")

        title = input("Type the title of the note to delete: ")

        note = model.Note(user[0], title)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"Note {note.title} was successfully deleted.")

        else:
            print(f"No note was deleted, please try again.")
