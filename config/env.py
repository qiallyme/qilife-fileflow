from dotenv import load_dotenv, set_key
import os

ENV_FILE = ".env"

def ask_user_for_folder(prompt):
    folder = input(f"{prompt}\n> ").strip()
    while not os.path.isdir(folder):
        print("❌ That path doesn't exist. Try again.")
        folder = input("> ").strip()
    return os.path.abspath(folder)

def setup_env():
    if not os.path.exists(ENV_FILE):
        open(ENV_FILE, "w").close()

    load_dotenv()

    source = os.getenv("SOURCE_FOLDER")
    processed = os.getenv("PROCESSED_FOLDER")

    if not source or not os.path.isdir(source):
        source = ask_user_for_folder("Enter a folder to watch for new files:")
        set_key(ENV_FILE, "SOURCE_FOLDER", source)

    if not processed:
        processed = os.path.join(source, "Processed")
        os.makedirs(processed, exist_ok=True)
        set_key(ENV_FILE, "PROCESSED_FOLDER", processed)

    batch_size = os.getenv("BATCH_SIZE", "5")
    set_key(ENV_FILE, "BATCH_SIZE", batch_size)

    return {
        "SOURCE_FOLDER": source,
        "PROCESSED_FOLDER": processed,
        "BATCH_SIZE": int(batch_size)
    }

def load_env():
    return setup_env()
