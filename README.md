![credit_risk1](https://github.com/njgeorge000158/Credit-Risk-Classification-with-Logistic-Regression-Using-Scikit-Learn/assets/137228821/76c5a095-a7e3-47be-b161-d95e602b739c)

----

# **Credit Risk Classification Using Scikit Learn**

## **Overview of the Analysis**

The purpose of this analysis is to predict the creditworthiness of borrowers for a peer-to-peer lending services company. With a dataset containing the 75,036 healthy and 2,500 high-risk loans, I surveyed supervised machine learning models to find the one that most accurately predicts the credit loan risk for a consumer. Although the instructions only request the Logistic Regression model, due to the binary classification nature of the problem, I expanded the analysis to include Decision Tree, Support Vector Machine, K-Nearest Neighbor, and Gaussian Naive Bayes. These models will predict whether a loan is healthy or high-risk by analyzing the provided applicant information such as loan size, interest rate, borrower income, debt-to-income ratio, number of accounts, derogatory marks, and total debt. Furthermore, the high discrepancy between the numbers of healthy and high-risk loans convinced me to examine the effect of random and synthetic sampling: random undersampling, random oversampling, cluster centroids, synthetic minority oversampling (SMOTE), and synthetic minority oversampling with edited nearest neighbors (SMOTEEN).

To accomplish the analysis, I used the following process:

1. Created 36 optimized hyperparameter models (6 classifiers X 6 sampling methodologies) in the IPython Notebook, spam_detector_optimization.ipynb, and wrote them to files in the folder, resources.
2. Read the spam data into a dataframe in the IPython Notebook, spam_detector.ipynb.
3. Separated the data into features and labels, checked the labels value count, and split the features and labels variables into training and testing data sets.
4. Read the optimized hyperparameters from the files in the folder, resources, and fit the models by using these optimized parameters and the training data.
7. Evaluated the each model’s performance using the testing data to find the accuracy, precision, and recall scores in a confusion matrix.

Here is a comparison of the top three models:

<img width="458" alt="Screenshot 2024-04-30 at 9 56 42 AM" src="https://github.com/njgeorge000158/Credit-Risk-Classification-Using-Scikit-Learn/assets/137228821/59de5a4a-4579-4529-b468-d64ee3462d13">

<img width="459" alt="Screenshot 2024-04-30 at 9 57 42 AM" src="https://github.com/njgeorge000158/Credit-Risk-Classification-Using-Scikit-Learn/assets/137228821/3efb278e-c7a2-4289-b13b-c43ce7984c06">

<img width="453" alt="Screenshot 2024-04-30 at 9 58 33 AM" src="https://github.com/njgeorge000158/Credit-Risk-Classification-Using-Scikit-Learn/assets/137228821/2e2b5fec-e2e7-44f1-aa7b-725438d976c9">

The tabulation of the overall accuracy of all the models produced the following rankings:

![credit_risk_classification_colabTable972ModelPerformanceRankings](https://github.com/njgeorge000158/Credit-Risk-Classification-Using-Scikit-Learn/assets/137228821/51b28a26-a303-4aa3-a66f-8ca834fc5cae)

## **Summary**

Logistic Regression (Cluster Centroids) is the best model for predicting healthy loans with a small number of false positives and negatives leading to a precision score of 100%, a recall score of 99%, and an f1-score of 100%.  Nevertheless, this model less accurately predicts high-risk loans with a precision of 84%, a recall of 100%, and an f1-score of 95%. The balanced accuracy, 99%, is about the same as the actual accuracy, 99.52%, due to the sampling method.  In terms of accuracy, the Support Vector Machine closely matches the first model for predicting healthy loans and high-risk loans to a precision score of 100%, a recall score of 99%, and an f1-score of 100%. This model also less accurately predicts high-risk loans with a precision of 83%, a recall of 100%, and an f1-score of 95%. The balanced accuracy, 99%, is about the same as the actual accuracy, 99.51%, without any sampling.

Although there is a narrow field of models for binary classification, the best model varies based on the nature, composition, and extent of the data. The most notable observation from these results is the varying effects that different models and oversampling methods can have on the predictive accuracy from a data set.

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
