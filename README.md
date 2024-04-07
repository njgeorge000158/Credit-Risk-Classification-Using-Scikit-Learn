![credit_risk1](https://github.com/njgeorge000158/Credit-Risk-Classification-with-Logistic-Regression-Using-Scikit-Learn/assets/137228821/76c5a095-a7e3-47be-b161-d95e602b739c)

----

# **Credit Risk Classification with Logistic Regression using Scikit-learn**

## **Overview of the Analysis**

The purpose of this analysis is to evaluate the performance of two supervised machine learning models for predicting consumer loan credit risk. These Logistic Regression models use a data set of historical activity from a peer-to-peer lending services company to identify the creditworthiness of borrowers. Specifically, the models predict whether a loan is healthy or high-risk by analyzing the provided applicant information such as loan size, interest rate, borrower income, debt-to-income ratio, number of accounts, derogatory marks, and total debt.  Moreover, although the data set is comprehensive, there is significantly more information about healthy loans than high-risk loans (75,036 records vs. 2,500 records). With this in mind, the second model compensates for this inconsistency.

To accomplish the analysis, the machine learning process includes the following steps:

1. Separate the data into a features variable, X, and a labels variable, y.
2. Check the labels value count.
3. Further split the features and labels variables into training and testing data sets.
4. Fit a Logistic Regression model by using the training data.
5. Evaluate the model’s performance using the testing data to find the accuracy, precision, and recall scores.
8. Resample the data using the Scikit-learn function, RandomOverSampler, to address the labels's value count imbalance.
9. Check the labels value count again.
10. Create and fit another Logistic Regression model with the resampled data.
11. Evaluate the performance of the second model using the same metrics.

## **Results**

### **Machine Learning Model 1: Logistic Regression with Original Data**
* Overall Accuracy: 96.0%
* Balanced Accuracy: 99%
* Precision (Health Loans): 100%
* Precision (High-risk Loans): 87%
* Recall (Healthy Loans): 100%
* Recall (High-risk Loans): 92%

<img width="588" alt="credit_risk2" src="https://github.com/njgeorge000158/Credit-Risk-Classification-with-Logistic-Regression-Using-Scikit-Learn/assets/137228821/f97b7ce0-ad91-48c1-b8fb-17e3c1e87288">

### **Machine Learning Model 2: Logistic Regression with Resampled Data**
* Overall Accuracy: 99.5%
* Balanced Accuracy: 99%
* Precision (Health Loans): 100%
* Precision (High-risk Loans): 87%
* Recall (Healthy Loans): 99%
* Recall (High-risk Loans): 100%

<img width="571" alt="credit_risk3" src="https://github.com/njgeorge000158/Credit-Risk-Classification-with-Logistic-Regression-Using-Scikit-Learn/assets/137228821/c6b485ae-b5a0-4967-bfe1-31fc129704b5">

## **Summary**

The first Logistic Regression model does an excellent job predicting healthy loans with a small number of false positives and negatives leading to a precision score of 100%, a recall score of 100%, and an f1-score of 100%.  Nevertheless, this model less accurately predicts high-risk loans with a precision of 87%, a recall of 92%, and an f1-score of 90%. The balanced accuracy, 99%, is higher than the actual accuracy, 96%, because of the significant difference in labels's value counts. The first model's potential for an increase in accuracy and the comparatively inadequate performance in predicting high-risk loans vs. health loans are concerning. Thus, the first model warrants further optimization either by closing the value count gap with additional data or random oversampling: the second model uses the latter to solve this problem.

In terms of accuracy, the second Logistic Regression model with random oversampling matches the first model for predicting healthy loans and outperforms it for high-risk loans. For instance, the number of accepted healthy loans falls (18,642 to 18,632); the number of rejected high-risk loans expands (604 to 650); the number of false positives increases slightly (89 to 99); and the number of false negatives significantly drops (49 to 3). Moreover, using random oversampling to generate additional synthetic samples for the minority label class eliminates the labels's value count discrepancy leading to, among other things, the balanced accuracy score matching the overall accuracy score, 99%. For healthy loans, both models have 100% precision, 99% recall, and 100% f1-scores; for high-risk loans, although the precision, 87%, remains the same, the recall, 92%, increases by 8% to 100%, and the f1-score, 90%, increases by 3% to 93%. Consequently, using random oversampling with the Logistic Regression model maintains its identification of healthy loans while improving its identification of high-risk loans.

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
