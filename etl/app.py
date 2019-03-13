from datetime import datetime

from setup_data import setup_data
from data_maker import DataMaker
from constants import OOFFile
from setup_db import setup_db
from utils import pretty_print


def main():
    start = datetime.utcnow()
    print("\n\n\n============ Out-of-Field ETL ============")
    setup_data()
    engine = setup_db()

    if(engine):
        oof_maker = DataMaker(engine, OOFFile.data.value)
        oof_maker.make_tables()
    else:
        pretty_print("ERROR: ENGINE NOT SET")

    print("\n\n=====================================\n")
    print(f"Program Completed in {datetime.utcnow() - start}\n\n\n")


if __name__ == '__main__':
    main()
