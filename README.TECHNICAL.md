# **Credit Risk Classification Using Scikit-Learn**

----

### **Installation:**

----

This project only requires running the Google Colab Notebook, crypto_clustering_colab.ipynb.

----

### **Usage:**

----

The Google Colab Notebook, credit_risk_classification_colab.ipynb, requires the following Python scripts with it in the same folder:

credit_risk_constants.py

logx.py

pandasx.py

timex.py

If the folders, logs and images, are not present, the Google Colab Notebook will create them.  The Google Colab Notebook, credit_risk_classification_colab.ipynb, needs the csv file, lending_data.csv, in the folder, resources, to execute. To place the Google Colab Notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, the notebook writes information to the log file in the folder, logs. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG and HTML files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

credit_risk_classification_colab.ipynb, credit_risk_constants.py, logx.py, pandasx.py, timex.py

#### Input files

lending_data.csv, dt_CLUSTER_CENTROIDS_grid_search_model.sav, dt_grid_search_model.sav, dt_OVERSAMPLED_grid_search_model.sav, dt_SMOTE_grid_search_model.sav, dt_SMOTEENN_grid_search_model.sav, dt_UNDERSAMPLED_grid_search_model.sav, knn_CLUSTER_CENTROIDS_grid_search_model.sav, knn_grid_search_model.sav, knn_OVERSAMPLED_grid_search_model.sav, knn_SMOTE_grid_search_model.sav, knn_SMOTEENN_grid_search_model.sav, knn_UNDERSAMPLED_grid_search_model.sav, lr_CLUSTER_CENTROIDS_grid_search_model.sav, lr_grid_search_model.sav, lr_OVERSAMPLED_grid_search_model.sav, lr_SMOTE_grid_search_model.sav, lr_SMOTEENN_grid_search_model.sav, lr_UNDERSAMPLED_grid_search_model.sav, rf_CLUSTER_CENTROIDS_grid_search_model.sav, rf_grid_search_model.sav, rf_OVERSAMPLED_grid_search_model.sav, rf_SMOTE_grid_search_model.sav, rf_SMOTEENN_grid_search_model.sav, rf_UNDERSAMPLED_grid_search_model.sav

#### Output files

dt_CLUSTER_CENTROIDS_model.sav, dt_model.sav, dt_OVERSAMPLED_model.sav, dt_SMOTE_model.sav, dt_SMOTEENN_model.sav, dt_UNDERSAMPLED_model.sav, gnb_CLUSTER_CENTROIDS_model.sav, gnb_model.sav, gnb_OVERSAMPLED_model.sav, gnb_SMOTE_model.sav, gnb_SMOTEENN_model.sav, gnb_UNDERSAMPLED_model.sav, knn_CLUSTER_CENTROIDS_model.sav, knn_model.sav, knn_OVERSAMPLED_model.sav, knn_SMOTE_model.sav, knn_SMOTEENN_model.sav, knn_UNDERSAMPLED_model.sav, lr_CLUSTER_CENTROIDS_model.sav, lr_model.sav, lr_OVERSAMPLED_model.sav, lr_SMOTE_model.sav, lr_SMOTEENN_model.sav, lr_UNDERSAMPLED_model.sav, rf_CLUSTER_CENTROIDS_model.sav, rf_model.sav, rf_OVERSAMPLED_model.sav, rf_SMOTE_model.sav, rf_SMOTEENN_model.sav, rf_UNDERSAMPLED_model.sav, svm_CLUSTER_CENTROIDS_model.sav, svm_model.sav, svm_OVERSAMPLED_model.sav, svm_SMOTE_model.sav, svm_SMOTEENN_model.sav, svm_UNDERSAMPLED_model.sav

#### SQL script

n/a

#### Software

Google Colab, Matplotlib, Numpy, Pandas, Python 3.11.5, scikit-learn

![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./credit_risk_classification_colab.ipynb](./credit_risk_classification_colab.ipynb)

|&rarr; [./credit_risk_constants.py](./credit_risk_constants.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable11LendingDataTable.png](./images/credit_risk_classification_colabTable11LendingDataTable.png)
  
  &emsp; |&rarr; [./images/credit_risk_classification_colabTable131CreditRiskTargetSeries.png](./images/credit_risk_classification_colabTable131CreditRiskTargetSeries.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable132CreditRiskFeaturesDataFrame.png](./images/credit_risk_classification_colabTable132CreditRiskFeaturesDataFrame.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable151CreditRiskScaledFeaturesTrainingData.png](./images/credit_risk_classification_colabTable151CreditRiskScaledFeaturesTrainingData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable152CreditRiskScaledFeaturesTestData.png](./images/credit_risk_classification_colabTable152CreditRiskScaledFeaturesTestData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable271ScaledFeaturesTrainingUndersampledData.png](./images/credit_risk_classification_colabTable271ScaledFeaturesTrainingUndersampledData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable272ScaledFeaturesTrainingOversampledData.png](./images/credit_risk_classification_colabTable272ScaledFeaturesTrainingOversampledData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable273ScaledFeaturesTrainingClusterCentroidsData.png](./images/credit_risk_classification_colabTable273ScaledFeaturesTrainingClusterCentroidsData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable274ScaledFeaturesTrainingSMOTEData.png](./images/credit_risk_classification_colabTable274ScaledFeaturesTrainingSMOTEData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable275ScaledFeaturesTrainingSMOTEENNData.png](./images/credit_risk_classification_colabTable275ScaledFeaturesTrainingSMOTEENNData.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable971ModelPerformanceMatrix.png](./images/credit_risk_classification_colabTable971ModelPerformanceMatrix.png)

  &emsp; |&rarr; [./images/credit_risk_classification_colabTable972ModelPerformanceRankings.png](./images/credit_risk_classification_colabTable972ModelPerformanceRankings.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable12LendingDataTable.png](./images/credit_risk_hyperparameters_optimization_colabTable12LendingDataTable.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable131LendingTargetSeries.png](./images/credit_risk_hyperparameters_optimization_colabTable131LendingTargetSeries.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable132LendingFeaturesDataFrame.png](./images/credit_risk_hyperparameters_optimization_colabTable132LendingFeaturesDataFrame.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable151LendingScaledFeaturesTrainingData.png](./images/credit_risk_hyperparameters_optimization_colabTable151LendingScaledFeaturesTrainingData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable152LendingScaledFeaturesTestData.png](./images/credit_risk_hyperparameters_optimization_colabTable152LendingScaledFeaturesTestData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable271ScaledFeaturesTrainingUndersampledData.png](./images/credit_risk_hyperparameters_optimization_colabTable271ScaledFeaturesTrainingUndersampledData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable272ScaledFeaturesTrainingOversampledData.png](./images/credit_risk_hyperparameters_optimization_colabTable272ScaledFeaturesTrainingOversampledData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable273ScaledFeaturesTrainingClusterCentroidsData.png](./images/credit_risk_hyperparameters_optimization_colabTable273ScaledFeaturesTrainingClusterCentroidsData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable274ScaledFeaturesTrainingSMOTEData.png](./images/credit_risk_hyperparameters_optimization_colabTable274ScaledFeaturesTrainingSMOTEData.png)

  &emsp; |&rarr; [./images/credit_risk_hyperparameters_optimization_colabTable275ScaledFeaturesTrainingSMOTEENNData.png](./images/credit_risk_hyperparameters_optimization_colabTable275ScaledFeaturesTrainingSMOTEENNData.png)

  &emsp; |&rarr; [./images/README.md](./images/README.md)
  
|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240429credit_risk_hyperparameters_optimization_colab_log.txt](./logs/20240429credit_risk_hyperparameters_optimization_colab_log.txt)

  &emsp; |&rarr; [./logs/20240430credit_risk_classification_colab_log.txt](./logs/20240430credit_risk_classification_colab_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./models/](./models/)

  &emsp; |&rarr; [./models/dt_CLUSTER_CENTROIDS_grid_search_model.sav](./models/dt_CLUSTER_CENTROIDS_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_CLUSTER_CENTROIDS_model.sav](./models/dt_CLUSTER_CENTROIDS_model.sav)

  &emsp; |&rarr; [./models/dt_grid_search_model.sav](./models/dt_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_model.sav](./models/dt_model.sav)

  &emsp; |&rarr; [./models/dt_OVERSAMPLED_grid_search_model.sav](./models/dt_OVERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_OVERSAMPLED_model.sav](./models/dt_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/dt_SMOTE_grid_search_model.sav](./models/dt_SMOTE_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_SMOTE_model.sav](./models/dt_SMOTE_model.sav)

  &emsp; |&rarr; [./models/dt_SMOTEENN_grid_search_model.sav](./models/dt_SMOTEENN_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_SMOTEENN_model.sav](./models/dt_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/dt_UNDERSAMPLED_grid_search_model.sav](./models/dt_UNDERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/dt_UNDERSAMPLED_model.sav](./models/dt_UNDERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/gnb_CLUSTER_CENTROIDS_model.sav](./models/gnb_CLUSTER_CENTROIDS_model.sav)

  &emsp; |&rarr; [./models/gnb_model.sav](./models/gnb_model.sav)

  &emsp; |&rarr; [./models/gnb_OVERSAMPLED_model.sav](./models/gnb_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/gnb_SMOTE_model.sav](./models/gnb_SMOTE_model.sav)

  &emsp; |&rarr; [./models/gnb_SMOTEENN_model.sav](./models/gnb_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/gnb_UNDERSAMPLED_model.sav](./models/gnb_UNDERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/knn_CLUSTER_CENTROIDS_grid_search_model.sav](./models/knn_CLUSTER_CENTROIDS_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_CLUSTER_CENTROIDSs_model.sav](./models/knn_CLUSTER_CENTROIDSs_model.sav)

  &emsp; |&rarr; [./models/knn_grid_search_model.sav](./models/knn_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_model.sav](./models/knn_model.sav)

  &emsp; |&rarr; [./models/knn_OVERSAMPLED_grid_search_model.sav](./models/knn_OVERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_OVERSAMPLED_model.sav](./models/knn_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/knn_SMOTE_grid_search_model.sav](./models/knn_SMOTE_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_SMOTE_model.sav](./models/knn_SMOTE_model.sav)

  &emsp; |&rarr; [./models/knn_SMOTEENN_grid_search_model.sav](./models/knn_SMOTEENN_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_SMOTEENN_model.sav](./models/knn_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/knn_UNDERSAMPLED_grid_search_model.sav](./models/knn_UNDERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/knn_UNDERSAMPLED_model.sav](./models/knn_UNDERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/lr_CLUSTER_CENTROIDS_grid_search_model.sav](./models/lr_CLUSTER_CENTROIDS_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_CLUSTER_CENTROIDS_model.sav](./models/lr_CLUSTER_CENTROIDS_model.sav)

  &emsp; |&rarr; [./models/lr_grid_search_model.sav](./models/lr_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_model.sav](./models/lr_model.sav)

  &emsp; |&rarr; [./models/lr_OVERSAMPLED_grid_search_model.sav](./models/lr_OVERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_OVERSAMPLED_model.sav](./models/lr_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/lr_SMOTE_grid_search_model.sav](./models/lr_SMOTE_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_SMOTE_model.sav](./models/lr_SMOTE_model.sav)

  &emsp; |&rarr; [./models/lr_SMOTEENN_grid_search_model.sav](./models/lr_SMOTEENN_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_SMOTEENN_model.sav](./models/lr_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/lr_UNDERSAMPLED_grid_search_model.sav](./models/lr_UNDERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/lr_UNDERSAMPLED_model.sav](./models/lr_UNDERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/README.md](./models/README.md)

  &emsp; |&rarr; [./models/rf_CLUSTER_CENTROIDS_grid_search_model.sav](./models/rf_CLUSTER_CENTROIDS_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_CLUSTER_CENTROIDS_model.sav](./models/rf_CLUSTER_CENTROIDS_model.sav)

  &emsp; |&rarr; [./models/rf_grid_search_model.sav](./models/rf_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_model.sav](./models/rf_model.sav)

  &emsp; |&rarr; [./models/rf_OVERSAMPLED_grid_search_model.sav](./models/rf_OVERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_OVERSAMPLED_model.sav](./models/rf_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/rf_SMOTE_grid_search_model.sav](./models/rf_SMOTE_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_SMOTE_model.sav](./models/rf_SMOTE_model.sav)

  &emsp; |&rarr; [./models/rf_SMOTEENN_grid_search_model.sav](./models/rf_SMOTEENN_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_SMOTEENN_model.sav](./models/rf_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/rf_UNDERSAMPLED_grid_search_model.sav](./models/rf_UNDERSAMPLED_grid_search_model.sav)

  &emsp; |&rarr; [./models/rf_UNDERSAMPLED_model.sav](./models/rf_UNDERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/svm_CLUSTER_CENTROIDS_model.sav](./models/svm_CLUSTER_CENTROIDS_model.sav)

  &emsp; |&rarr; [./models/svm_model.sav](./models/svm_model.sav)

  &emsp; |&rarr; [./models/svm_OVERSAMPLED_model.sav](./models/svm_OVERSAMPLED_model.sav)

  &emsp; |&rarr; [./models/svm_SMOTE_model.sav](./models/svm_SMOTE_model.sav)

  &emsp; |&rarr; [./models/svm_SMOTEENN_model.sav](./models/svm_SMOTEENN_model.sav)

  &emsp; |&rarr; [./models/svm_UNDERSAMPLED_model.sav](./models/svm_UNDERSAMPLED_model.sav)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/lending_data.csv](./resources/lending_data.csv)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Google Colab Documentation](https://cloud.google.com/colab/docs)

[imbalanced-learn documentation](https://imbalanced-learn.org/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

[scikit-learn Documentation](https://scikit-learn.org/stable/)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
