import os
from prompt_toolkit import prompt
import sqlite3
from typing import List, Tuple

def databaseInit():
    connection = sqlite3.connect("notes_manager.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS folders (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        parentId INTEGER,
        FOREIGN KEY (parentId) REFERENCES folders (id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT,
        folderId INTEGER,
        FOREIGN KEY (folderId) REFERENCES folders (id)
    )''')

    connection.commit()
    connection.close()

def connectionGet():
    return sqlite3.connect("notes_manager.db")

def folderCreate(name: str, parentId: int = None):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO folders (name, parentId) VALUES (?, ?)", (name, parentId))
        conn.commit()
        print(f"Folder '{name}' created successfully.")

def folderList(parentId: int = None, level: int = 0):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM folders WHERE parentId IS ?", (parentId,))
        folders = cursor.fetchall()
        for folderId, name in folders:
            print(f"{' ' * level * 2}[{folderId}] {name}")
            folderList(folderId, level + 1)

def folderDalete(folderId: int):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM folders WHERE id = ?", (folderId,))
        cursor.execute("DELETE FROM notes WHERE folderId = ?", (folderId,))
        cursor.execute("DELETE FROM folders WHERE parentId = ?", (folderId,))
        conn.commit()

def FolderEdit(folderId: int, name: str, parentId: int = None):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE folders SET name = ?, parentId = ? WHERE id = ?", (name, parentId, folderId))
        conn.commit()

def noteCreate(title: str, content: str, folderId: int):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content, folderId) VALUES (?, ?, ?)", (title, content, folderId))
        conn.commit()
        print(f"Note '{title}' created successfully.")

def NotesList(folderId: int = None):
    with connectionGet() as conn:
        cursor = conn.cursor()
        if folderId is None:
            cursor.execute("SELECT notes.id, notes.title, notes.content, folders.name FROM notes LEFT JOIN folders ON notes.folderId = folders.id")
        else:
            cursor.execute("SELECT notes.id, notes.title, notes.content, folders.name FROM notes LEFT JOIN folders ON notes.folderId = folders.id WHERE notes.folderId = ?", (folderId,))
        return cursor.fetchall()

def noteDelete(noteId: int):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (noteId,))
        conn.commit()

def noteEdot(noteId: int, title: str, content: str):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, noteId))
        conn.commit()

def NoteSearch(keyword: str):
    with connectionGet() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT notes.id, notes.title, notes.content, folders.name FROM notes LEFT JOIN folders ON notes.folderId = folders.id WHERE notes.title LIKE ? OR notes.content LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()

def notePrint(notes: List[Tuple[int, str, str, str]]):
    print("Notes:")
    for noteId, title, content, folder_name in notes:
        print(f"[{noteId}] {title} (Folder: {folder_name})")
        print(f"    Content: {content}")

def main():
    databaseInit()

    while True:
        print("\n--- Notes Manager ---")
        print("1. Create Folder")
        print("2. List Folders")
        print("3. Delete Folder")
        print("4. Create Note")
        print("5. List Notes")
        print("6. Edit Note")
        print("7. Delete Note")
        print("8. Search Notes")
        print("9. Edit Folder")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter folder name: ")
            parentId = input("Enter parent folder ID (or leave blank for root): ")
            folderCreate(name, int(parentId) if parentId else None)

        elif choice == "2":
            print("Folder Structure:")
            folderList()

        elif choice == "3":
            folderId = int(input("Enter folder ID to delete: "))
            folderDalete(folderId)

        elif choice == "4":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            folderId = int(input("Enter folder ID: "))
            noteCreate(title, content, folderId)

        elif choice == "5":
            folderId = input("Enter folder ID (or leave blank to list all notes): ")
            notes = NotesList(int(folderId) if folderId else None)
            notePrint(notes)

        elif choice == "6":
            noteId = int(input("Enter note ID to edit: "))
            with connectionGet() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT title, content FROM notes WHERE id = ?", (noteId,))
                note = cursor.fetchone()

            if note:
                title = prompt("Enter new title: ", default=note[0])
                content = prompt("Enter new content: ", default=note[1])
                noteEdot(noteId, title, content)
                print("Note updated successfully.")
            else:
                print("Note not found.")

        elif choice == "7":
            noteId = int(input("Enter note ID to delete: "))
            noteDelete(noteId)

        elif choice == "8":
            keyword = input("Enter keyword to search: ")
            results = NoteSearch(keyword)
            notePrint(results)

        elif choice == "9":
            folderId = int(input("Enter folder ID to edit: "))
            with connectionGet() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name, parentId FROM folders WHERE id = ?", (folderId,))
                folder = cursor.fetchone()

            if folder:
                name = prompt("Enter new folder name: ", default=folder[0])
                parentInput = prompt("Enter new parent folder ID (leave blank for root): ", default=str(folder[1]) if folder[1] else "")
                parentId = int(parentInput) if parentInput else None
                FolderEdit(folderId, name, parentId)
                print("Folder updated successfully.")
            else:
                print("Folder not found.")

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
