import os
from utils import (
    create_directory,
    fetch_file,
    pretty_print
)
from constants import (
    PUBLIC_DATA_URL,
    OOFFile,
    INPUT_DIR,
    MIGRATION_DIR,
    FILES_LIST
)


def needed_files_exists():
    if(os.path.isdir(INPUT_DIR)):
        curr_input_files = os.listdir(INPUT_DIR)
        needed_files_list = [OOFFile.data.value]

        return set(needed_files_list).issubset(curr_input_files)
    else:
        return False


def setup_data():
    pretty_print("SETUP DATA")

    """
    See if needed files currently exist in input directory.
    If not, see if extract file already exists correctly
    If not, retrieve and extract accordingly
    Move extracted files to correct directory and simplified filename
    Remove extra directory and files
    """
    if (needed_files_exists()):
        pretty_print("Needed Files Already Exist", True)
    else:
        create_directory(INPUT_DIR)
        pretty_print("Fetching Out-of-Field Data From Public Website", True)

        fetch_file(PUBLIC_DATA_URL, INPUT_DIR, OOFFile.data.value)

    create_directory(MIGRATION_DIR, True)
    pretty_print("Setup Data Complete", True)
