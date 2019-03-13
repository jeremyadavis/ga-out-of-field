import pandas

from constants import (
    INPUT_DIR,
    DATAFRAME_COLUMNS
)


def get_data_file(filename):
    df = pandas.read_csv(INPUT_DIR+filename,
                         encoding='LATIN-1',
                         low_memory=False,
                         header=0,
                         names=DATAFRAME_COLUMNS
                         )

    df.columns = df.columns.map(lambda x: x.lower())

    # print('df', df.head(200))
    return df
