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

def build_delta_feature (df, attribute, algorithm) :
    df[attribute+'_delta'] = df[[attribute+'_x', attribute+'_y']].apply(lambda x : algorithm.normalized_similarity(x[attribute+'_x'], x[attribute+'_y']), axis=1)

    return df

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
    df['coordinate'+suffix] = df['coordinate'+suffix].map(lambda x : x[0] if len(x)>0 else '').str.replace('.', '').str[:8].str.lower()

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
