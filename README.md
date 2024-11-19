# **Behavioral Analysis of User Phone Usage Metrics (ML)**

Created in Google Colab.
**Dataset Source**: [Kaggle - Mobile Device Usage and User Behavior Dataset](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)

### **Overview**
This project conducts a behavioral analysis on user phone usage metrics. The objective is to identify correlations between various phone usage metrics and user behavior.

### **Dataset Summary**
- **Sample Size**: 700 entries (n = 700)

- **Features**:
  - **User ID**: Unique identifier for each user.<br>
  - **Device Model**: Model of the user's smartphone.<br>
  - **Operating System**: OS of the device (iOS or Android).<br>
  - **App Usage Time**: Daily time spent on mobile applications, measured in minutes.<br>
  - **Screen On Time**: Average hours per day the screen is active.<br>
  - **Battery Drain**: Daily battery consumption in mAh.<br>
  - **Number of Apps Installed**: Total apps available on the device.<br>
  - **Data Usage**: Daily mobile data consumption in megabytes.<br>
  - **Age**: Age of the user.<br>
  - **Gender**: Gender of the user (Male or Female).<br>
  - **User Behavior Class**: Classification of user behavior based on usage patterns from Light (1) to Extreme (5) usage.

### **Analysis and Models**
1. **Logistic Regression Model**:
   - Predicts **Battery Drain (mAh/day)**.
   - Trained using **App Usage Time (min/day)**, **Screen On Time (hours/day)**, and **Data Usage (MB/day)**.

2. **Linear Regression Model**:
   - Developed as a comparison to the logistic regression model for predicting battery drain and examining model performance.
