'''
AUTHOR:     Nathan James
DATE:       02/11/2019
UPDATED:    ---
DESCRIPTION:
    This python file contains functions written and used for the Denver Crime
    dataset analysis.
'''


import pandas as pd
import numpy as np
from scipy.stats import ttest_rel


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


def compare_columns(df, alpha=0.05):
    results = {}
    for idx, a in enumerate(df.columns[:-1],1):
        for b in df.columns[idx:]:
            t, p = ttest_rel(df[a],df[b], nan_policy='omit')
            results['test'] = results.get('test', []) + [f'{a}/{b}']
            results['t'] = results.get('t', []) + [t]
            results['p'] = results.get('p', []) + [p]

    df_results = pd.DataFrame(results)
    alpha /= len(df_results.index)
    return df_results.assign(Reject_Null=df_results.loc[:,'p'] <= alpha)


if __name__ == "__main__":
    df = pd.DataFrame({'a':[1,3,5,7], 'b':[np.nan, 2,4,6], 'c':[7,1,1,0]})
    print(df)
    print(df.describe())

    df_compare = compare_columns(df)
    print(df_compare)

    print('\n\n\n### With randome ints ###\n\n\n')

    df = pd.DataFrame(np.random.randint(0,50,size=(100,4)),
                        columns='A B C D'.split())
    df.loc[3,'B'] = np.nan
    print(df.head())
    print(df.describe())
    df_compare = compare_columns(df)
    print(df_compare)
