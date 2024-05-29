import argparse
import os
import re
import subprocess

def create_note(title, content=None):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    note_file = os.path.join(script_dir, f"{title}.txt")

    if content:
        mode = "a" if os.path.exists(note_file) else "w"
        with open(note_file, mode) as f:
            if mode == "a":
                f.write("\n")  # Add a new line before appending content if file exists
            f.write(content)
        print(f"Your Note Created: {note_file}")
    else:
        subprocess.run(["vim", note_file])

def view_note(title):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    note_file = os.path.join(script_dir, f"{title}.txt") 
    if os.path.exists(note_file):
        with open(note_file, "r") as f:
            content = f.read()
        print(content)
    else:
        print(f"Nothing Found With This Title: {title}")


def delete_note(title):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    note_file = os.path.join(script_dir, f"{title}.txt")
    if os.path.exists(note_file):
        os.remove(note_file)
        print(f"Note deleted: {note_file}")
    else:
        print(f"Nothing Found with This Title: {title}")

def list_notes():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    notes = [f for f in os.listdir(script_dir) if re.match(r"^[a-zA-Z0-9_-]+.txt$", f)]
    if notes:
        print("Notes:")
        for note in notes:
            print(f"- {note[:-4]}")
    else:
        print("No notes found")

parser = argparse.ArgumentParser(description="Your Bash Note App\nBy ixi_flower")
subparsers = parser.add_subparsers(dest="command")

create_parser = subparsers.add_parser("c", help="You can create your new note")
create_parser.add_argument("title", help="The title of the note")
create_parser.add_argument("content", nargs="?", help="The content of the note", default=None)

view_parser = subparsers.add_parser("v", help="You can See Your Notes")
view_parser.add_argument("title", help="The title of the note")

delete_parser = subparsers.add_parser("r", help="You can Delete Your Note")
delete_parser.add_argument("title", help="The title of the note")

list_parser = subparsers.add_parser("l", help="List Of All Your Notes")

args = parser.parse_args()

if args.command == "c":
    create_note(args.title, args.content)
elif args.command == "v":
    view_note(args.title)
elif args.command == "r":
    delete_note(args.title)
elif args.command == "l":
    list_notes()
else:
    parser.print_help()
