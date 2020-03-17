from sklearn.model_selection import ParameterGrid
import numpy as np
from sklearn.model_selection import train_test_split

# Generate ParameterGrid object and print its parameters
def generate_parameter_grid (param_dict) :
    # Generate parameter grid object
    pg = ParameterGrid(param_dict)

    # Print number of combinations
    print('The grid parameters are ...')
    for params in param_dict :
        print(f'{params} {param_dict[params]}')
    print(f' => Number of combinations : {len(pg)}')

    return pg

def fit_model_measure_scores (model, param_dict, X_tr, y_tr, X_te, y_te) :
    # Set parameters
    model.set_params(**param_dict)
    print('Fitting with parameters', param_dict)

    # Fit classifier
    model.fit(X_tr, y_tr)

    # Save accuracy on train set and validation set : models have only .score() function ...
    #  ... and no .accuracy_score() function, which is callable with the sklearn.metrics library.
    #  They return the same result, though.
    param_dict['accuracy_tr'] = model.score(X_tr, y_tr)
    param_dict['accuracy_val'] = model.score(X_te, y_te)
    if (1-model.score(X_tr, y_tr)) == 0:
        # If model reaches 100% accuracy on train data set
        param_dict['log_accuracy_tr'] = -np.inf
    else:
        param_dict['log_accuracy_tr'] = -np.log(1-model.score(X_tr, y_tr))
    param_dict['log_accuracy_val'] = -np.log(1-model.score(X_te, y_te))

    print(' => validation score {:.3f}%'.format(100*param_dict['accuracy_val']))

    # For saving results
    return param_dict

def get_best_parameters (scores, parameter_dictionary) :
    idx_best = [acc['accuracy_val'] for acc in scores].index(
        max([acc['accuracy_val'] for acc in scores]))

    print('The parameters for the best model are ...')
    param_dict = {}
    for pkey in parameter_dictionary:
        param_dict[pkey] = scores[idx_best][pkey]
        print(f'{pkey} = {param_dict[pkey]}')

    return param_dict

def split_feature_target (df, mode) :
    # Transform DataFrame data into numpy array.
    X = df.drop(columns=['duplicates']).values
    y = df.duplicates.values
    full_idx = np.arange(len(y))
    test_sizes = 0.2

    X_train, X_te, y_train, y_te, idx_train, idx_te = train_test_split(X, y, full_idx, stratify=y, test_size=test_sizes, random_state=0)

    if mode == 'train_validation_test' :
        # Split once more to have validation set.
        X_tr, X_val, y_tr, y_val, idx_tr, idx_val = train_test_split(X_train, y_train, idx_train, stratify=y_train, test_size=test_sizes, random_state=0)

        return X_tr, X_val, X_te, y_tr, y_val, y_te, idx_tr, idx_val, idx_te
    elif mode == 'train_test' :

        return X_train, None, X_te, y_train, None, y_te, idx_train, None, idx_te
    else :
        print('Unknown split requirement.')

    return None
