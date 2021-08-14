import os
import pandas as pd 
from multiprocessing import Pool

# wrap your csv importer in a function that can be mapped
def read_csv(filename):
    'converts a filename to a pandas dataframe'
    return pd.read_csv(filename)


def main():

    # get a list of file names
    files = os.listdir('.')
    file_list = [filename for filename in files if filename.split('.')[1]=='csv']

    # set up your pool
    with Pool(processes=8) as pool: # or whatever your hardware can support

        # have your pool map the file names to dataframes
        df_list = pool.map(read_csv, file_list)

        # reduce the list of dataframes to a single dataframe
        combined_df = pd.concat(df_list, ignore_index=True)

if __name__ == '__main__':
    main()