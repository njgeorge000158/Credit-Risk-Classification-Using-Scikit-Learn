#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  credit_risk_constants.py
 #
 #  File Description:
 #      This Python script, credit_risk_constants.py, contains generic Python constants
 #      for tasks in the Google Colab Notebooks, credit_risk_colab.ipynb and
 #      credit_risk_optimization_colab.ipynb.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  11/27/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'credit_risk_constants.py'


# In[3]:


CONSTANT_INPUT_FILE_PATH = './gdrive/MyDrive/credit_risk_classification/resources/lending_data.csv'


CONSTANT_ML_RANDOM_STATE_1 = 21

CONSTANT_ML_RANDOM_STATE_2 = 9

CONSTANT_ML_LR_MAX_ITERATIONS = 10000000

CONSTANT_ML_RF_N_ESTIMATORS = 200

CONSTANT_ML_SVM_PROBABILITY = True

CONSTANT_ML_KNN_LEAF_SIZE = 2


# In[4]:


CONSTANT_LR_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_grid_search_model.sav'

CONSTANT_LR_UNDERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_undersampled_grid_search_model.sav'

CONSTANT_LR_OVERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_oversampled_grid_search_model.sav'

CONSTANT_LR_cluster_cluster_centroids_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_cluster_cluster_centroids_grid_search_model.sav'

CONSTANT_LR_SMOTE_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_SMOTE_grid_search_model.sav'

CONSTANT_LR_SMOTEENN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_SMOTEENN_grid_search_model.sav'


CONSTANT_DT_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_grid_search_model.sav'

CONSTANT_DT_UNDERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_undersampled_grid_search_model.sav'

CONSTANT_DT_OVERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_oversampled_grid_search_model.sav'

CONSTANT_DT_cluster_cluster_centroids_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_cluster_cluster_centroids_grid_search_model.sav'

CONSTANT_DT_SMOTE_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_SMOTE_grid_search_model.sav'

CONSTANT_DT_SMOTEENN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_SMOTEENN_grid_search_model.sav'


CONSTANT_RF_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_grid_search_model.sav'

CONSTANT_RF_UNDERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_undersampled_grid_search_model.sav'

CONSTANT_RF_OVERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_oversampled_grid_search_model.sav'

CONSTANT_RF_cluster_cluster_centroids_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_cluster_cluster_centroids_grid_search_model.sav'

CONSTANT_RF_SMOTE_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_SMOTE_grid_search_model.sav'

CONSTANT_RF_SMOTEENN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_SMOTEENN_grid_search_model.sav'


CONSTANT_SVM_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_grid_search_model.sav'

CONSTANT_SVM_UNDERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_undersampled_grid_search_model.sav'

CONSTANT_SVM_OVERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_oversampled_grid_search_model.sav'

CONSTANT_SVM_cluster_cluster_centroids_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_cluster_cluster_centroids_grid_search_model.sav'

CONSTANT_SVM_SMOTE_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_SMOTE_grid_search_model.sav'

CONSTANT_SVM_SMOTEENN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_SMOTEENN_grid_search_model.sav'


CONSTANT_KNN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_grid_search_model.sav'

CONSTANT_KNN_UNDERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_undersampled_grid_search_model.sav'

CONSTANT_KNN_OVERSAMPLED_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_oversampled_grid_search_model.sav'

CONSTANT_KNN_cluster_cluster_centroids_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_cluster_cluster_centroids_grid_search_model.sav'

CONSTANT_KNN_SMOTE_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_SMOTE_grid_search_model.sav'

CONSTANT_KNN_SMOTEENN_GRID_SEARCH_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_SMOTEENN_grid_search_model.sav'


# In[5]:


CONSTANT_LR_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_model.sav'

CONSTANT_LR_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_undersampled_model.sav'

CONSTANT_LR_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_oversampled_model.sav'

CONSTANT_LR_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_cluster_centroids_model.sav'

CONSTANT_LR_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_SMOTE_model.sav'

CONSTANT_LR_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/lr_SMOTEENN_model.sav'


CONSTANT_DT_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_model.sav'

CONSTANT_DT_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_undersampled_model.sav'

CONSTANT_DT_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_oversampled_model.sav'

CONSTANT_DT_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_cluster_centroids_model.sav'

CONSTANT_DT_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_SMOTE_model.sav'

CONSTANT_DT_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/dt_SMOTEENN_model.sav'


CONSTANT_RF_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_model.sav'

CONSTANT_RF_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_undersampled_model.sav'

CONSTANT_RF_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_oversampled_model.sav'

CONSTANT_RF_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_cluster_centroids_model.sav'

CONSTANT_RF_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_SMOTE_model.sav'

CONSTANT_RF_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/rf_SMOTEENN_model.sav'


CONSTANT_SVM_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_model.sav'

CONSTANT_SVM_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_undersampled_model.sav'

CONSTANT_SVM_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_oversampled_model.sav'

CONSTANT_SVM_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_cluster_centroids_model.sav'

CONSTANT_SVM_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_SMOTE_model.sav'

CONSTANT_SVM_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/svm_SMOTEENN_model.sav'


CONSTANT_KNN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_model.sav'

CONSTANT_KNN_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_undersampled_model.sav'

CONSTANT_KNN_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_oversampled_model.sav'

CONSTANT_KNN_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_cluster_centroids_model.sav'

CONSTANT_KNN_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_SMOTE_model.sav'

CONSTANT_KNN_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/knn_SMOTEENN_model.sav'


CONSTANT_GNB_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_model.sav'

CONSTANT_GNB_UNDERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_undersampled_model.sav'

CONSTANT_GNB_OVERSAMPLED_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_oversampled_model.sav'

CONSTANT_GNB_CENTROIDS_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_cluster_centroids_model.sav'

CONSTANT_GNB_SMOTE_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_SMOTE_model.sav'

CONSTANT_GNB_SMOTEENN_MODEL_FILE_PATH \
    = './gdrive/MyDrive/credit_risk_classification/resources/gnb_SMOTEENN_model.sav'


# In[ ]:




