from enum import Enum
import os


SCRIPT_DIR = os.path.dirname(__file__)

INPUT_DIR = f"{SCRIPT_DIR}/data/"
OUTPUT_DIR = f"{SCRIPT_DIR}/data/"
MIGRATION_DIR = f"{SCRIPT_DIR}/migrations/"

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

DATAFRAME_COLUMNS = [
    "SCHOOL_YEAR",
    "DISTRICT",
    "NAME",
    "LVL_3_DESC",
    "LVL_2_DESC",
    "FTE",
    "OUTOFFIELD_FTE",
    "OUTOFFIELD_FTE_PCT"
]

TABLE_NAME = "out_of_field"
