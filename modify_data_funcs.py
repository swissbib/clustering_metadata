import random as rand
import string

# Remove character at random position
def remove_one_character (df, attrib, idx_of_samples) :
    for i in idx_of_samples:
        pos = rand.randrange(len(df[attrib].iloc[i]))

        # Remove character
        df[attrib].iloc[i] = df[attrib].iloc[i][:pos] + df[attrib].iloc[i][pos+1:]

    return df

# Switch two neighboring characters at random position
def switch_two_characters (df, attrib, idx_of_samples) :
    for i in idx_of_samples:
        pos1 = rand.randrange(len(df[attrib].iloc[i]))
        c1 = df[attrib].iloc[i][pos1]
        if pos1 < len(df[attrib].iloc[i])-1 :
            pos2 = pos1+1
        else :
            pos2 = pos1-1
        c2 = df[attrib].iloc[i][pos2]

        # Switch characters
        df[attrib].iloc[i] = df[attrib].iloc[i][:pos1] + c2 + df[attrib].iloc[i][pos1+1:]
        df[attrib].iloc[i] = df[attrib].iloc[i][:pos2] + c1 + df[attrib].iloc[i][pos2+1:]

    return df

# Replace one character with a random character at random position
def replace_one_character(df, attrib, idx_of_samples) :
    for i in idx_of_samples:
        pos = rand.randrange(len(df[attrib].iloc[i]))
        if attrib == 'exactDate': # Number digits only
            new_char = rand.choice(string.digits)
        else:
            new_char = rand.choice(string.ascii_lowercase)

        # Replace character
        df[attrib].iloc[i] = df[attrib].iloc[i][:pos] + new_char + df[attrib].iloc[i][pos+1:]

    return df

# Add one character with a random character at random position
def add_one_character(df, attrib, idx_of_samples) :
    for i in idx_of_samples:
        pos = rand.randrange(len(df[attrib].iloc[i]))
        new_char = rand.choice(string.ascii_letters.lower())

        # Replace character
        df[attrib].iloc[i] = df[attrib].iloc[i][:pos] + new_char + df[attrib].iloc[i][pos:]

    return df

# Function to modify all person attributes
def modify_character_string (df, attrib, modification_ratio, delete, switch, replace, add) :
    # Find new sample
    sample_idx = df[df[attrib].apply(lambda x : len(x)>3)].sample(frac=modification_ratio).index
    for i in range(delete):
        remove_one_character(df, attrib, sample_idx)
        print(f'In {len(sample_idx)} samples one character of attribute {attrib} removed.')

    # Find another, a different sample
    sample_idx = df[df[attrib].apply(lambda x : len(x)>3)].sample(frac=modification_ratio).index
    for i in range(switch):
        switch_two_characters(df, attrib, sample_idx)
        print(f'In {len(sample_idx)} samples two characters of attribute {attrib} switched.')

    # Find another, a different sample
    sample_idx = df[df[attrib].apply(lambda x : len(x)>3)].sample(frac=modification_ratio).index
    for i in range(replace):
        replace_one_character(df, attrib, sample_idx)
        print(f'In {len(sample_idx)} samples one character of attribute {attrib} replaced.')

    # Find another, a different sample
    sample_idx = df[df[attrib].apply(lambda x : len(x)>3)].sample(frac=modification_ratio).index
    for i in range(add):
        add_one_character(df, attrib, sample_idx)
        print(f'In {len(sample_idx)} samples one character of attribute {attrib} added.')

    return df

def remove_one_side_of_attribute_pair (df, attribute_list, modification_ratio) :
    for a in attribute_list:
        sample_idx = df[df[a].apply(lambda x : len(x)>0)].sample(frac=modification_ratio/10).index
        for i in sample_idx:
            df[a].iat[i] = ''

    return df
