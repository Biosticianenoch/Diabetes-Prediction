
<div align="center">

# 🧪 Diabetes Disease Prediction  
### 📈 Machine Learning Classification for Health Diagnosis  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn) ![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

## 🎯 Objectives

- 🔍 Detect the presence of diabetes using health-related features.
- 📊 Clean, analyze, and visualize medical data.
- 🤖 Build ML models (KNN, Naive Bayes, SVM, Random Forest, Logistic Regression).
- ✅ Select the best model and save it for deployment.

---

## 📂 Dataset Overview

| Feature | Description |
|--------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | Serum insulin (2 hrs) |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Likelihood of diabetes based on family history |
| Age | Patient's age |
| Outcome | 0 = No diabetes, 1 = Diabetes |

---

## 🧼 Data Cleaning & Preprocessing

- ✅ Removed duplicates
- ⚠️ Replaced invalid 0-values with mean/median
- 📐 Scaled features using `QuantileTransformer`
- 📊 Balanced dataset (analysis shows imbalance favoring non-diabetics)

---

## 📊 Exploratory Data Analysis

### ✅ Count Plot
- Shows imbalance in outcome classes

### 📈 Histograms
- Most variables are skewed (except Glucose, BP)

### 📦 Boxplots
- Revealed significant outliers

### 🔥 Correlation Heatmap
```python
sns.heatmap(df.corr(), annot=True)
```

---

## ⚙️ Models Implemented

| Model | Accuracy | F1 Score | Precision | Recall |
|-------|----------|----------|-----------|--------|
| 🧪 Logistic Regression | 77.9% | 0.61 | 0.66 | 0.57 |
| 🌳 Random Forest | 81.8% | 0.70 | 0.71 | 0.68 |
| 📍 KNN | 81.8% | 0.69 | 0.72 | 0.66 |
| 💠 SVM (Best) | **83.8%** | **0.71** | **0.77** | **0.66** |
| 🧮 Naive Bayes | 77.2% | 0.59 | 0.66 | 0.53 |
| 🌲 Decision Tree | 79.2% | 0.56 | 0.77 | 0.45 |

---

## 🏆 Final Evaluation (SVM)

```yaml
Accuracy  : 83.76%
Precision : 77%
Recall    : 66%
F1 Score  : 71%
AUC       : Computed using roc_auc_score
```

📦 Model saved using `pickle`:
```python
pkl.dump(svm, open("diabetes_model.p", "wb"))
```

---

## 💡 Recommendations

- 👩‍⚕️ Focus on high-risk individuals with elevated glucose/BMI
- 🧪 Routine testing & early intervention
- 🚀 Future Steps:
  - Apply SMOTE to handle class imbalance
  - Add EHR or live data streams
  - Build a Streamlit or Flask web app

---

## 🙋‍♂️ Author

**Enock Bereka**  
📍 Kakamega, Kenya  
📧 your- [My Email](enochwafulah254@gmail.com)  
🔗 [LinkedIn Profile](https://linkedin.com/in/enockbereka)

---

> 🩺 *“Prediction is the first step to prevention. Data science makes it possible.”*

