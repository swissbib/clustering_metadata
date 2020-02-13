import pandas as pd

"""General functions for chapter data preparation"""

def transform_list_to_string (df, column) :
    df[column] = [', '.join(map(str, list_element)) for list_element in df[column]]
    df[column] = df[column].str.lower()

    return df

def transform_dictionary_to_list (df, column, dict_element) :
    df[column+'_'+dict_element] = [dictionary_pair.get(dict_element) for dictionary_pair in df[column]]
    # Fill missing values
    df[column+'_'+dict_element].fillna('', inplace=True)

    return df

def build_delta_feature (df, attribute, algorithm, metadata_dict) :
    if attribute in ['doi', 'isbn'] :
        df[attribute+'_delta'] = df[[attribute+'_x', attribute+'_y']].apply(lambda x : build_delta_isbn(x[attribute+'_x'], x[attribute+'_y'], algorithm), axis=1)
    else :
        df[attribute+'_delta'] = df[[attribute+'_x', attribute+'_y']].apply(lambda x : algorithm.normalized_similarity(x[attribute+'_x'], x[attribute+'_y']), axis=1)

    metadata_dict['columns_for_comparison'].append(attribute+'_delta')

    return df, metadata_dict

def build_delta_isbn (x_list, y_list, algorithm) :
    # Dedupe list
    x_list = list(dict.fromkeys(x_list))
    y_list = list(dict.fromkeys(y_list))

    if len(x_list) == 0 and len(y_list) == 0 :
        # Return fix value in case of both lists empty
        return 1.0
    else :
        length_min = min(len(x_list), len(y_list))
        if length_min == 0 :
            # Return fix value in case of one list empty
            return 0.0
        else : # Both lists hold elements
            # Initialize similarity sum
            similarity_sum = 0.0
            # Calculate sum of similarities for each element
            for x_element in x_list :
                for y_element in y_list :
                    similarity_sum += algorithm.normalized_similarity(x_element, y_element)
            # Normalize
            return similarity_sum / length_min

def split_dictionary_column (df, attribute, split_columns) :
    for ending in split_columns:
        df = transform_dictionary_to_list(df, attribute, ending)
        df = transform_list_to_string(df, attribute+'_'+ending)
    df = df.drop(columns=[attribute])

    return df

def clean_exactDate_string (df) :
    df['exactDate'] = df.exactDate.str.replace('\D', 'u')

    return df

def norm_first_coordinate (df, suffix) :
    df['coordinate'+suffix] = df['coordinate'+suffix].map(lambda x : x[0] if len(x)>0 else '').str.replace(' ', '').str.replace('.', '').str[:8].str.lower()

    return df

def reduce_list_to_north (df) :
    for i in range(len(df)):
        if len(df.coordinate_N[i]) > 0:
            to_be_used = df.coordinate_N[i].copy()
            while (df.coordinate_N[i][0][0] == 'E') | (df.coordinate_N[i][0][0] == 'W'):
                df.coordinate_N[i].remove(df.coordinate_N[i][0])

    return df

def split_coordinate (df) :
    df['coordinate_E'] = df['coordinate']
    df = norm_first_coordinate(df, '_E')
    # Recuce list to N and S and then same procedure
    df['coordinate_N'] = df['coordinate']
    df = reduce_list_to_north(df)
    df = norm_first_coordinate(df, '_N')

    return df

def split_format (df) :
    df['format_prefix'] = df['format'].str[:2]
    df['format_postfix'] = df['format'].str[2:8]
    # Fill empty pre/postfix attributes with spaces for comparison
    df['format_prefix'][df['format_prefix']==''] = '  '
    df['format_postfix'][df['format_postfix']==''] = '      '
    df = df.drop(columns=['format'])

    return df

def show_samples_interval (df, attrib, lower, upper, no_sample=5) :
    # If not enough number of samples then take least possible number.
    no_sample = min(len(df[['duplicates', attrib+'_delta', attrib+'_x', attrib+'_y']][(df[attrib+'_delta'] >= lower) & (df[attrib+'_delta'] <= upper)]), no_sample)
    display(df[['duplicates', attrib+'_delta', attrib+'_x', attrib+'_y']][(df[attrib+'_delta'] >= lower) & (df[attrib+'_delta'] <= upper)].sample(n=no_sample))
    print(f'{lower} <= {attrib}_delta <= {upper}')

    return None

def show_samples_distinct (df, attrib, pos_value, no_sample=5) :
    # If not enough number of samples then take least possible number.
    no_sample = min(len(df[['duplicates', attrib+'_delta', attrib+'_x', attrib+'_y']][df[attrib+'_delta'] == pos_value]), no_sample)
    display(df[['duplicates', attrib+'_delta', attrib+'_x', attrib+'_y']][df[attrib+'_delta'] == pos_value].sample(n=no_sample))

    return None

def mark_both_missing (df, attrib, target_value=-1.0) :
    pd.set_option('mode.chained_assignment', None) # Suppress SettingWithCopyWarning.
    df[attrib+'_delta'][df[attrib+'_x'].apply(lambda x : len(x) == 0) & df[attrib+'_y'].apply(lambda x : len(x) == 0)] = target_value

    return df
