from fileflow.watcher import start_watcher
from fileflow.batcher import process_batch
from fileflow.mover import undo_last_move
from config.env import load_env
import time

def run():
    queue = []
    cfg = load_env()
    observer = start_watcher(queue, cfg["SOURCE_FOLDER"])
    print(f"📂 Watching folder: {cfg['SOURCE_FOLDER']}...")

    try:
        while True:
            if queue:
                process_batch(queue, cfg)
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    print("🌀 QiFileFlow Mini App")
    while True:
        print("\nOptions:\n1. Start watching\n2. Undo last\n3. Quit")
        choice = input("Select: ")
        if choice == "1":
            run()
        elif choice == "2":
            undo_last_move()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
