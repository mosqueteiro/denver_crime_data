'''
AUTHOR:     Nathan James
DATE:       02/11/2019
UPDATED:    ---
DESCRIPTION:
    This python file contains functions written and used for the Denver Crime
    dataset analysis.
'''


import pandas as pd


def table_info(df1, df2, write='w'):
    '''
    Writes the tables and their columns to specified text file

    Arguments:
        df1, df2 (pandas.DataFrame): Pandas dataframes or series to be printed
        write (string): whether to write or append to the file, default: write
    '''
    f = open('data/table_info.txt', 'w')
    print('Crime data columns', *df1.columns,
            sep='\n\t', file=f, end='\n\n')
    print('Offense code columns', *df2.columns,
            sep='\n\t', file=f, end='\n\n')
    f.close()
