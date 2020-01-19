"""General functions for saving performance results of the models"""
import os
import pandas as pd
import numpy as np
from sklearn.dummy import DummyClassifier
import sklearn.metrics as me

# Restore results so far
def restore_results (path_goldstandard) :
    df = pd.read_pickle(os.path.join(path_goldstandard, 'results.pkl'), compression=None)
    return df

# Add result of this section
def add_result_to_results (path_goldstandard, model, X, y, y_pred) :
    if not isinstance(model, DummyClassifier) :
        df = restore_results(path_goldstandard)
    else :
        df = pd.DataFrame()

    df = df.append(pd.DataFrame.from_dict({
        'model': [model.__class__.__name__ if model.__class__.__name__ != 'Sequential' else 'Neural Network'],
        'test_score' : [model.score(X, y) if model.__class__.__name__ != 'Sequential' else 0.0],
        'auc' : [100*me.roc_auc_score(y, y_pred)],
        'accuracy' : [100*me.accuracy_score(y, y_pred)],
        'precision' : [100*me.precision_score(y, y_pred)],
        'recall' : [100*me.recall_score(y, y_pred)],
        'test_score_log' : [np.log(1-model.score(X, y)) if model.__class__.__name__ != 'Sequential' else 0.0],
        'auc_log' : [np.log(1-me.roc_auc_score(y, y_pred))],
        'accuracy_log' : [np.log(1-me.accuracy_score(y, y_pred))],
        'precision_log' : [np.log(1-me.precision_score(y, y_pred))],
        'recall_log' : [np.log(1-me.recall_score(y, y_pred))]
    }), sort=False)

    save_results(df, path_goldstandard)

    return

# Save full DataFrame into pickle file
def save_results (df, path_goldstandard) :
    df.to_pickle(os.path.join(path_goldstandard, 'results.pkl'), compression=None)
    return
