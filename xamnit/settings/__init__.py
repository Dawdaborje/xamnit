from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    "base.py",
    "database.py",
)
