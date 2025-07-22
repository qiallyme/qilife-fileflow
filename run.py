# run.py
from fileflow.core import run
from fileflow.mover import undo_last_move

if __name__ == "__main__":
    print("🌀 QiFileFlow Mini App")
    while True:
        print("\nOptions:\n1. Start watching\n2. Undo last move\n3. Quit")
        choice = input("Select: ").strip()
        if choice == "1":
            run()
        elif choice == "2":
            undo_last_move()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
