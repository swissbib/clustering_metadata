import pandas as pd
import numpy as np
import re as re

"""General functions for chapter data preparation"""

def transform_dictionary_to_list (df, column, dict_element) :
    df[column+'_'+dict_element] = [dictionary_pair.get(dict_element) for dictionary_pair in df[column]]
    # Fill missing values
    df[column+'_'+dict_element].fillna('', inplace=True)

    return df

def extract_number_digits_from_string (df, attrib) :
    df[attrib] = df[attrib].apply(lambda x : re.findall(r'\d+', x))
    df = transform_list_to_string(df, attrib, ' ')

    return df

def extract_scaling_from_scale (df) :
    # Only this attriubte is affected
    attrib = 'scale'

    # The '1: ' shall be removed
    df[attrib] = df[attrib].apply(lambda x : x.replace('1 ', ''))

    return df

def transform_list_to_string (df, attrib, separator=', ') :
    df[attrib] = [separator.join(map(str, list_element)) for list_element in df[attrib]]
    df[attrib] = df[attrib].str.lower()

    return df

def split_dictionary_column (df, attrib, split_columns) :
    for ending in split_columns:
        df = transform_dictionary_to_list(df, attrib, ending)
        df = transform_list_to_string(df, attrib+'_'+ending)
    df = df.drop(columns=[attrib])

    return df

def isolate_doi (x_list) :
    # Dedupe list
    x_list = list(dict.fromkeys(x_list))

    for x_element in x_list :
        # A doi starts with '10.'
        if x_element.startswith('10.') :
            # Return first list element starting with '10.'
            return x_element.lower()

    # Return empty string if no doi element has been found
    return ''

def isolate_ismn (x_list) :
    # Dedupe list
    x_list = list(dict.fromkeys(x_list))

    for x_element in x_list :
        # A ismn starts with '979' or 'm'
        if (x_element.startswith('979') | x_element.lower().startswith('m')) :
            # Return first list element starting with '10.'
            return x_element.lower()

    # Return empty string if no doi element has been found
    return ''

def reduce_to_attrib_element (df, attrib) :
    if attrib == 'doi' :
        apply_function = lambda x : isolate_doi(x)
    elif attrib == 'ismn' :
        apply_function = lambda x : isolate_ismn(x)
    df[attrib] = df[attrib].apply(apply_function)

    return df

def isolate_number_from_string (df, attrib) :
    df[attrib] = df[attrib].str.extract(r'(\d+)').fillna('')

    return df

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

def build_delta_feature (df, attrib, algorithm, metadata_dict) :
    if attrib in ['isbn'] :
        df[attrib+'_delta'] = df[[attrib+'_x', attrib+'_y']].apply(lambda x : build_delta_isbn(x[attrib+'_x'], x[attrib+'_y'], algorithm), axis=1)
    else :
        df[attrib+'_delta'] = df[[attrib+'_x', attrib+'_y']].apply(lambda x : algorithm.normalized_similarity(x[attrib+'_x'], x[attrib+'_y']), axis=1)

    metadata_dict['features'].append(attrib+'_delta')

    return df, metadata_dict

def concatenate_corporate_keys (df):
    # Initial filling
    df['corporate_full'] = df['corporate_110']
    df['corporate_full'] = df[['corporate_full', 'corporate_710']].apply(lambda x : x['corporate_full']+' '+x['corporate_710']
        if ( (len(x['corporate_full'])>0) & (len(x['corporate_710'])>0) & (x['corporate_full']!=x['corporate_710']) ) else ( x['corporate_710'] if ((len(x['corporate_full'])==0) & (len(x['corporate_710'])>0))
            else x['corporate_full']), axis=1)

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

# Full preprocessing of all attributes of Swissbib's goldstandard
def attribute_preprocessing(df, columns, strip_digits) :
    for attrib in columns:
        if attrib in ['isbn' # Take as is
                      , 'coordinate_N' # See 'coordinate_E'
                      , 'format_postfix' # See 'format_prefix'
                      , 'person_100', 'person_700' # See 'person_245c'
                      , 'ttlfull_246' # See 'ttlfull_245'
                     ]:
            continue # Explicitly : do nothing!
        elif attrib in ['coordinate_E']:
            df = split_coordinate(df)
        elif attrib in ['corporate_full']:
            df = split_dictionary_column(df, 'corporate', ['110', '710'#, '810
            ])
            df = concatenate_corporate_keys(df)
        elif attrib in ['doi', 'ismn']:
            df = reduce_to_attrib_element(df, attrib)
        elif attrib in ['edition', 'musicid']:
            df = isolate_number_from_string(df, attrib)
        elif attrib in ['exactDate']:
            df = clean_exactDate_string(df)
        elif attrib in ['format_prefix']:
            df = transform_list_to_string(df, 'format')
            df = split_format(df)
        elif attrib in ['person_245c']:
            df = split_dictionary_column(
                df, 'person', ['100', '700', #'800',
                    '245c']
            )
        elif attrib in ['scale'] and strip_digits :
            # Remove non-number digits
            df = extract_number_digits_from_string(df, attrib)
            # Remove '1: ' parts
            df = extract_scaling_from_scale(df)
        elif attrib in ['ttlfull_245']:
            df = split_dictionary_column(
                df, 'ttlfull', ['245', '246']
            )
        elif attrib in ['part', 'pubinit', 'volumes']:
            df = transform_list_to_string(df, attrib)
            if attrib in ['part', 'volumes'] and strip_digits:
                df = extract_number_digits_from_string(df, attrib)
        else: # Not explicitly handled, yet
            print('Attribute', attrib, 'is missing in this processing step!')

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

def mark_both_missing (df, attrib, target_value) :
    pd.set_option('mode.chained_assignment', None) # Suppress SettingWithCopyWarning.
    df[attrib+'_delta'][df[attrib+'_x'].apply(lambda x : len(x) == 0) & df[attrib+'_y'].apply(lambda x : len(x) == 0)] = target_value

    return df

def mark_one_missing (df, attrib, target_value) :
    pd.set_option('mode.chained_assignment', None) # Suppress SettingWithCopyWarning.
    # XOR on one single attribute is empty
    df[attrib+'_delta'][df[attrib+'_x'].apply(lambda x : len(x) == 0) ^ df[attrib+'_y'].apply(lambda x : len(x) == 0)] = target_value

    return df

def mark_missing (df, attrib, fctr, one_or_two='all') :
    value_ob_missing = [-0.5*fctr, -1.0*fctr]

    if one_or_two == 'all' :
        df = mark_both_missing(df, attrib, value_ob_missing[1])
        df = mark_one_missing(df, attrib, value_ob_missing[0])
    elif one_or_two == 'both' :
        df = mark_both_missing(df, attrib, value_ob_missing[1])
    elif one_or_two == 'one' :
        df = mark_one_missing(df, attrib, value_ob_missing[0])

    return df

def determine_similarity_values (df, attrib):
    attribute_uniques = np.sort(df[attrib+'_delta'].unique())
    attribute_uniques_len = len(attribute_uniques)
    print(attrib, 'values range', attribute_uniques)

    return attribute_uniques, attribute_uniques_len
