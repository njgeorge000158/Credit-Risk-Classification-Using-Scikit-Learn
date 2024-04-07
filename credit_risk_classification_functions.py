#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  credit_risk_classification_functions.py
 #
 #  File Description:
 #      This Python script, credit_risk_classification_functions.py, contains generic 
 #      Python functions for completing common tasks in the Credit Risk Analysis.
 #      Here is the list:
 #
 #      ModelPerformanceEvaluatorFunction
 #      
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  11/27/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import log_subroutines

import pandas as pd

from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'credit_risk_classification_functions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_model_performance_evaluation
 #
 #  Function Description:
 #      This function evaluates the logistic regression model and returns 
 #      a confusion matrix matrix.
 #
 #
 #  Return Type: float, dataframe, string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          y_test_series
 #                          The parameter is test data used for evaluation.
 #  nparray
 #          predictions_nparray
 #                          The parameter is the predictions used for evaluation.
 #  boolean
 #          original_flag_boolean
 #                          The parameter indicates the type of data (original vs. 
 #                          random oversampling)
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/27/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_model_performance_evaluation \
        (y_test_series, 
         predictions_nparray, 
         original_flag_boolean = True):

    try:
        
        if original_flag_boolean == True:
        
            data_type_string ='Original'
    
        else:
        
            data_type_string = 'Random Oversampling'
        
        
        confusion_matrix_nparray = confusion_matrix(y_test_series, predictions_nparray)

        
        index_string_list = ['Actual Healthy', 'Actual High-Risk']
    
        column_string_list = ['Predicted Healthy', 'Predicted High-Risk']
        
        target_names_string_list = ['healthy', 'high risk']
        

        accuracy_score_float = balanced_accuracy_score(y_test_series, predictions_nparray)

        
        confusion_matrix_dataframe \
            = pd.DataFrame \
                (confusion_matrix_nparray,
                 index = index_string_list,
                 columns = column_string_list)

        classification_report_string \
            = classification_report \
                (y_test_series, 
                 predictions_nparray, 
                 target_names = target_names_string_list)
    
    
        log_subroutines.print_and_log_text \
            ('\033[1m' + f'LOGISTIC REGRESSION MODEL ({data_type_string})\n' + '\033[0m\n'
             + '1) '
             + '\033[1m' + 'Accuracy Score: ' + '\033[0m'
             + f'{round(accuracy_score_float * 100, 1)}%\n\n'
             + '2) '
             + '\033[1m' + 'Confusion Matrix:\n' + '\033[0m\n'
             + f'{confusion_matrix_dataframe}\n\n'
             + f'3) '
             + '\033[1m' + 'Classification Report:\n' + '\033[0m\n'
             + f'{classification_report_string}\n')
    
    
        return accuracy_score_float, confusion_matrix_dataframe, classification_report_string
    
    except:
        
        log_subroutines.print_and_log_text \
            ('The function, return_model_performance_evaluation, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + 'was unable to return a confusion matrix.')
    
        return None


# In[ ]:




