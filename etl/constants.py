from enum import Enum

INPUT_DIR = "./data/"
OUTPUT_DIR = "./data/"
MIGRATION_DIR = "./migrations/"

OOF_DATA_FILENAME = "Educators_OUT_OF_FIELD_2018_JAN_24th_2019.csv"
PUBLIC_DATA_URL = f"https://download.gosa.ga.gov/2018/{OOF_DATA_FILENAME}"


class OOFFile(Enum):
    data = "oof_data.csv"


FILES_LIST = [
    {
        "needed_file_name": OOFFile.data.value,
        "extracted_path": OOF_DATA_FILENAME,
    }
]
