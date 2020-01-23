import pandas as pd
import random

"""General functions for chapter data analysis"""

def compare_logic (column_dict, column_name) :
    """Generates comparison logic for specific column object"""
    if column_name in (column_dict['list_columns']):
        # Lists
        filled = lambda col: col!=[]
        empty = lambda col: col==[]
    elif column_name in (column_dict['strings_columns']):
        # Strings
        filled = lambda col: col!=''
        empty = lambda col: col==''

    return filled, empty

def information_filled (d, column_name, filled, empty) :
    """Print-output of information"""

    print('Number of records with filled {:s} {:d}, with missing {:s} {:d} => {:.1f}%'.format(
        column_name, len(filled), column_name, len(empty),
        100*len(filled)/(len(empty)+len(filled))
    ))

    return

def find_empty_in_column (dataFrame, column_dict, column_name) :
    """Find degree of filling of an attribute and print
        information as output."""

    filled, empty = compare_logic(column_dict, column_name)

    idx_filled = dataFrame[dataFrame[column_name].apply(filled)].index
    idx_empty = dataFrame[dataFrame[column_name].apply(empty)].index

    information_filled(dataFrame, column_name, idx_filled, idx_empty)

    return idx_filled, idx_empty

def two_examples (d, filled, empty) :
    """Print-output of first sample data with empty attribute
        and of first sample data with filled attribute"""

    if len(empty) > 0:
        print('\nEMPTY - index', empty[0], '\n')
        print(d.loc[empty[0]])
    else:
        print('\nEMPTY - None')
    print('\nFILLED - index', filled[0], '\n')
    print(d.loc[filled[0]])

    return

"""General functions for appendix chapter Compare Similarities"""

def apply_similarities (df, algorithm, algorithm_name) :
    print(algorithm_name)
    df[algorithm_name] = df[['str1', 'str2']].apply(
        lambda x : algorithm.normalized_similarity(x['str1'], x['str2']), axis=1)

    return df

def string_pair_list(df, attribute) :
    string2_list = list(df[attribute].unique())

    string2_element = ''
    while string2_element == '' :
        string2_element = random.choice(string2_list)
    list_string1 = [string2_element for count in range(len(string2_list))]
    df_str_pairs = pd.DataFrame({'str1' : list_string1, 'str2' : string2_list})

    return df_str_pairs
