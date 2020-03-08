
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
