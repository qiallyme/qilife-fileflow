from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "SOURCE_FOLDER": os.getenv("SOURCE_FOLDER"),
        "PROCESSED_FOLDER": os.getenv("PROCESSED_FOLDER"),
        "BATCH_SIZE": int(os.getenv("BATCH_SIZE", "3"))
    }
