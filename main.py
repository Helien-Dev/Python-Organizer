import os
import shutil
from pathlib import Path
import format

folder_location = input("Folder direction: ")

def print_summary(moved_files):
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("SUMMARY"))
    print("+" + "-" * 40 + "+")
    for category, count in moved_files.items():
        print("| {:<30} {:>6} |".format(category, count))
    print("+" + "-" * 40 + "+")

def seeya_later():
    print("\n   -------------")
    print("   |   ( ^_^)   |  Seeya Later!")
    print("   -------------")

def organizer(path):
    os.chdir(path)
    moved_files = {}
    for file in os.listdir():
        path_file = Path(file)
        if path_file.is_file():
            name, extension = path_file.stem, path_file.suffix
            moved = False
            for key, lista in format.fileFormats.items():
                if extension in lista:
                    Path(key).mkdir(exist_ok=True)
                    shutil.move(file, f"{key}/{file}")
                    moved_files[key] = moved_files.get(key, 0) + 1
                    moved = True
                    break 
                
            if not moved:
                Path("Otros").mkdir(exist_ok=True)
                shutil.move(file, f"Otros/{file}")
                moved_files["Otros"] = moved_files.get("Otros", 0) + 1

    print_summary(moved_files)    
    seeya_later()
    return


organizer(folder_location)
