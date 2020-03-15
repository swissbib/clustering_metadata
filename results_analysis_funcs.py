import matplotlib.pyplot as plt

def get_confusion_matrix_indices (y_t, y_pre) :
    # False predicted uniques
    false_pred_uniques = (y_t != y_pre) & (y_t==1)
    # False predicted duplicates
    false_pred_duplicates = (y_t != y_pre) & (y_t==0)
    # Correct predicted uniques
    true_pred_uniques = (y_t == y_pre) & (y_t==0)
    # Correct predicted duplicates
    true_pred_duplicates = (y_t == y_pre) & (y_t==1)

    return true_pred_uniques, true_pred_duplicates, false_pred_uniques, false_pred_duplicates

# Plotting function for Grid Search results : training data
def plot_accuracy (param_dict, scores, accuracy_data) :
    if accuracy_data[-3:] == '_tr':
        colors = {'gini' : 'orange', 'entropy' : 'brown'}
        mfc_colors = {'gini' : 'pink', 'entropy' : 'black'}
        label_end = 'train'
    else :
        colors = {'gini' : 'green', 'entropy' : 'blue'}
        mfc_colors = {'gini' : 'yellow', 'entropy' : 'red'}
        label_end = 'validation'

    for i in param_dict['criterion']:
        # Data plot
        plt.plot([acc['max_depth'] for acc in scores if acc['criterion'] == i][:-1], [acc[accuracy_data] for acc in scores if acc['criterion'] == i][:-1], c=colors[i], marker='o', mfc=mfc_colors[i], mec=colors[i],
                 label=f'measure = {i}, {label_end}')
    plt.xlabel('tree depth')

    return plt
