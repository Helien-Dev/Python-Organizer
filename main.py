import os
import time
import shutil
import format
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

folder_location = input("Folder direction: ")

def print_summary(moved_files):
    print(f"{Fore.GREEN}+" + "-" * 40 + "+")
    print(f"{Fore.GREEN}| {Fore.YELLOW}{'SUMMARY':^38} {Fore.GREEN}|")
    print(f"{Fore.GREEN}+" + "-" * 40 + "+")
    for category, count in moved_files.items():
        print(f"{Fore.CYAN}| {category:<30} {Fore.MAGENTA}{count:>6} {Fore.CYAN}|")
    print(f"{Fore.GREEN}+" + "-" * 40 + "+")

def show_houston_message():
    time.sleep(1)
    print(f"\n  {Fore.WHITE}┌─────────────────────────────────────────────────────┐")
    print(f"  |                                                     |")
    print(f"  | {Fore.GREEN}( •◡• ){Style.RESET_ALL} {Fore.CYAN}Houston:{Style.RESET_ALL}                                    |")
    print(f"  | {Fore.YELLOW}Seeya Later, astronaut.{Style.RESET_ALL}                          |")
    print(f"  |                                                     |")
    print(f"  └─────────────────────────────────────────────────────┘\n")
    time.sleep(1)

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
    show_houston_message()
    return


organizer(folder_location)
