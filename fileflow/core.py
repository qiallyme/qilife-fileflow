# fileflow/core.py

from fileflow.watcher import start_watcher
from fileflow.batcher import process_batch
from fileflow.mover import undo_last_move
from config.env import load_env
import time

def run():
    print("🌀 Initializing QiFileFlow... please wait")
    queue = []
    cfg = load_env()
    print(f"📂 Source folder: {cfg['SOURCE_FOLDER']}")
    print(f"📁 Processed folder: {cfg['PROCESSED_FOLDER']}")
    print(f"🔁 Batch size: {cfg['BATCH_SIZE']}")

    observer = start_watcher(queue, cfg["SOURCE_FOLDER"])
    print(f"👁️ Watching folder: {cfg['SOURCE_FOLDER']} (Ctrl+C to stop)")

    try:
        while True:
            if queue:
                print(f"🧾 Queue size: {len(queue)}")
                process_batch(queue, cfg)
            time.sleep(2)
    except KeyboardInterrupt:
        print("🛑 Stopping watcher...")
        observer.stop()
    observer.join()
    print("✅ Done.")

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