"""General functions for chapter data preparation"""

def transform_attributes (df, a) :
    if a in ['volumes']:
        df = transform_list_to_string(df, a)
    elif a in ['format']:
        df = transform_list_to_string(df, a)
        df = split_format(df)
    elif a in ['person', 'corporate']:
        split_dictionary = {'person' : ['100', '700', '800', '245c'], 'corporate' : ['110', '710', '810']}
        df = split_person_corporate(df, a, split_dictionary)
    elif a in ['ttlfull']:
        df = split_ttlfull(df)
    elif a in ['century', 'edition', '035liste']:
        # Do nothing
        return df
    else:
        print('AJ ...', a, '... ATTRIUBTE IS MISSING!')

    return df

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

def split_person_corporate (df, attribute, split_dict) :
    for ending in split_dict[attribute]:
        df = transform_dictionary_to_list(df, attribute, ending)
        df = transform_list_to_string(df, attribute+'_'+ending)
    df = df.drop(columns=[attribute])

    return df

def split_ttlfull (df) :
    for ending in ['245', '246']:
        df = transform_dictionary_to_list(df, 'ttlfull', ending)
        df = transform_list_to_string(df, 'ttlfull_'+ending)
    df = df.drop(columns=['ttlfull'])

    return df

def split_format (df) :
    df['format_prefix'] = df['format'].str[:2]
    df['format_postfix'] = df['format'].str[2:8]
    # Fill empty pre/postfix attributes with spaces for comparison
    df['format_prefix'][df['format_prefix']==''] = '  '
    df['format_postfix'][df['format_postfix']==''] = '      '
    df = df.drop(columns=['format'])

    return df
