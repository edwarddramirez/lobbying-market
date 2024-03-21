import numpy as np
import pandas as pd
import ast
from tqdm import tqdm

def preprocess_data(df):
    """
    description:
        preprocesses the data by converting string columns to list or dict objects,
        converting issue codes to 0s or 1s, and turning client and registrant keys
        into columns

    inputs: 
        df (pandas dataframe) - dataframe containing the data to be preprocessed
    outputs: 
        df (pandas dataframe) - dataframe containing the preprocessed data
    """

    # format columns whose elements are strings, but are used as list or dict objs
    keys = ['lobbying_activities', 'client', 'registrant']
    for k in tqdm(keys, desc = 'string -> list/dict'):
        df[k] = df[k].apply(ast.literal_eval)

    # make a column of list of issue codes in each row
    df['issue_codes'] = df['lobbying_activities'].apply(lambda x: [i['general_issue_code'] for i in x])
    # obtain all unique issue codes in a list
    issue_codes = []
    for i in tqdm(df['issue_codes']):
        issue_codes.extend(i)
    issue_codes = list(set(issue_codes))

    # convert issue codes to 0s or 1s
    for code in tqdm(issue_codes, desc = 'issues -> 0/1s'):
        df[code] = df['issue_codes'].apply(lambda x: int(code in x) )

    # turn client keys into columns
    client_keys = list(df['client'][0].keys())
    for k in tqdm(client_keys, desc = 'client keys -> columns'):
        col_name = 'c_' + k
        df[col_name] = df['client'].apply(lambda x: x[k])

    # turn registrant keys into columns
    registrant_keys = list(df['registrant'][0].keys())
    for k in tqdm(registrant_keys, desc = 'registrant keys -> columns'):
        col_name = 'r_' + k
        df[col_name] = df['registrant'].apply(lambda x: x[k])

    return df