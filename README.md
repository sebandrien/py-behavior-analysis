# A Behavior Analysis of User Usage Metrics (ML)
Data set sourced from: https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset
A behavioral analysis of a dataset of multiple user phone usage metrics.

Goal is to establish correlations between usage metrics and user behavior.
The dataset consists of a sample size of 700 entries, n = 700.

The data was organized in the following ways:
User ID: Unique identifier for each user.
Device Model: Model of the user's smartphone.
Operating System: The OS of the device (iOS or Android).
App Usage Time: Daily time spent on mobile applications, measured in minutes.
Screen On Time: Average hours per day the screen is active.
Battery Drain: Daily battery consumption in mAh.
Number of Apps Installed: Total apps available on the device.
Data Usage: Daily mobile data consumption in megabytes.
Age: Age of the user.
Gender: Gender of the user (Male or Female).
User Behavior Class: Classification of user behavior based on usage patterns Light (1) - Extreme (5) usage.

A logisitc regression model is used to predict 'Battery Drain (mAh/day)' by training the model on 'App Usage Time (min/day)', 'Screen On Time (hours/day)', 'Data Usage (MB/day)'.

A linear regression model is also used to compare the results to the logistic regression model.
