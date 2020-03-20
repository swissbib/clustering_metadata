"""General functions for saving performance results of the models"""
import os
import pickle as pk
import pandas as pd
import numpy as np
import nbformat
from sklearn.dummy import DummyClassifier
import sklearn.metrics as me

# Restore results so far
def restore_dict_results (path, load_file) :
    with open(os.path.join(path, load_file), 'rb') as handle:
        results_dict = pk.load(handle)

    return results_dict

# Save full DataFrame into pickle file
def save_dict_results (results_dict, path_goldstandard, dump_file) :
    # Binary intermediary metadata file
    with open(os.path.join(path_goldstandard, dump_file), 'wb') as df_output_file:
        pk.dump(results_dict, df_output_file)

    return None

# Save notebook on disc
def save_notebook_results (notebook, path_results, dict_dump_file_name) :
    # Build notebook file name first
    notebook_name = dict_dump_file_name['notebook_name'][:-6]
    for k in dict_dump_file_name.keys():
        if k != 'notebook_name':
            notebook_name = notebook_name + '_' + k + str(dict_dump_file_name[k])
    # File suffix still
    notebook_name = notebook_name + '.ipynb'

    # Notebook to file
    with open(os.path.join(path_results, notebook_name), 'wt') as f:
        nbformat.write(notebook, f)

    return None

# Determine name of model
def get_model_name (model) :
    if model.__class__.__name__ == 'Sequential' :
        return 'Neural Network'
    else :
        return model.__class__.__name__

# Generate DataFrame of model scores
def generate_model_score_df (model, X, y, y_pred, suffix) :
    df = pd.DataFrame.from_dict({
        'model': get_model_name(model)+suffix,
        # The model.score() is the same as model's .accuracy_score()
#        'test_score' : [model.score(X, y) if get_model_name(model) != 'Neural Network' else me.accuracy_score(y, y_pred)],
        'auc' : [100*me.roc_auc_score(y, y_pred)],
        'accuracy' : [100*me.accuracy_score(y, y_pred)],
        'precision' : [100*me.precision_score(y, y_pred)],
        'recall' : [100*me.recall_score(y, y_pred)],
        # The model.score() is the same as model's .accuracy_score()
#        'test_score_log' : [-np.log(1-model.score(X, y)) if get_model_name(model) != 'Neural Network' else -np.log(1-me.accuracy_score(y, y_pred))],
        'auc_log' : [-np.log(1-me.roc_auc_score(y, y_pred))],
        'accuracy_log' : [-np.log(1-me.accuracy_score(y, y_pred))],
        'precision_log' : [-np.log(1-me.precision_score(y, y_pred))],
        'recall_log' : [-np.log(1-me.recall_score(y, y_pred))]
    })

    return df

# Store wrongly predicted rows
def add_wrong_predictions(path, model, coma_quadrant, df, suffix='') :
    filename = 'wrong_predictions.pkl'

    if os.path.exists(os.path.join(path, filename)) :
        wrong_predictions = restore_dict_results(path, filename)
        if get_model_name(model)+suffix not in wrong_predictions.keys() :
            # Initialize empty dictionary
            wrong_predictions[get_model_name(model)+suffix] = {}
        wrong_predictions[get_model_name(model)+suffix][coma_quadrant] = df
    else :
        wrong_predictions = {get_model_name(model)+suffix : {coma_quadrant : df}}

    return save_dict_results(wrong_predictions, path, filename)

# Store results of model
def add_result_to_results (path, validation_scores, model, X, y, y_pred, suffix='') :
    filename = 'results.pkl'

    if isinstance(model, DummyClassifier) :
        # Baseline as first model
        results_dictionary = {'results_best_model' : pd.DataFrame(), 'results_model_scores' : {}}
    else :
        # Restore results so far
        results_dictionary = restore_dict_results(path, filename)

    # Add results of model
    results_dictionary['results_best_model'] = results_dictionary['results_best_model'].append(generate_model_score_df(model, X, y, y_pred, suffix), sort=False)
    results_dictionary['results_model_scores'][get_model_name(model)+suffix] = pd.DataFrame(validation_scores)

    return save_dict_results(results_dictionary, path, filename)
