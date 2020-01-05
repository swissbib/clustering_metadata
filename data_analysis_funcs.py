"""General functions for chapter data analysis"""

def compare_logic (column_dict, column_name):
    """Generates comparison logic for specific column object"""
    if column_name in (column_dict['list_columns']):
        # Lists
        filled = lambda col: col!=[]
        empty = lambda col: col==[]
    elif column_name in (column_dict['strings_columns']):
        # Strings
        filled = lambda col: col!=''
        empty = lambda col: col==''
    elif column_name in (column_dict['array_of_strings_columns']):
        # Array of Strings
        filled = lambda col: col!=['']
        empty = lambda col: col==['']

    return filled, empty

def information_filled (d, column_name, filled, empty):
    """Print-output of information"""

    print('Number of records with filled {:s} {:d}, with missing {:s} {:d} => {:.1f}%'.format(
        column_name, len(filled), column_name, len(empty),
        100*len(filled)/(len(empty)+len(filled))
    ))

    return

def find_empty_in_column (dataFrame, column_dict, column_name):
    """Find degree of filling of an attribute and print
        information as output."""

    filled, empty = compare_logic(column_dict, column_name)

    idx_filled = dataFrame[dataFrame[column_name].apply(filled)].index
    idx_empty = dataFrame[dataFrame[column_name].apply(empty)].index

    information_filled(dataFrame, column_name, idx_filled, idx_empty)

    return idx_filled, idx_empty

def two_examples (d, filled, empty):
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
