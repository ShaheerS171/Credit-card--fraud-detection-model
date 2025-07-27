# 🚨 Credit Card Fraud Detection using Machine Learning

This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The dataset is highly imbalanced, making it a challenging real-world problem. A complete ML pipeline has been implemented — from EDA and preprocessing to model evaluation and deployment.

---

## 📁 Dataset

- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Shape**: 284,807 rows × 31 columns
- **Target Column**: `Class` (0 = Legitimate, 1 = Fraud)

---

## ⚙️ Project Workflow

### 1. 📊 Exploratory Data Analysis (EDA)
- Checked for class imbalance.
- Visualized distributions of key features (like V17, V12, V14, etc.)
- Correlation heatmaps and pair plots.
- Identified outliers using boxplots.

### 2. 🧹 Preprocessing
- Scaled numeric columns where needed.
- Addressed missing/null values (if any).
- Selected top important features based on intuition and correlation.

### 3. 📉 Handling Imbalance
- Used **SMOTE (Synthetic Minority Oversampling Technique)** to handle class imbalance.
- Ensured stratified sampling for evaluation.

### 4. 🤖 Model Building
Trained and tested multiple classifiers:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM) ✅ *(Best Performer)*

### 5. ✅ Model Evaluation
- Evaluated using `StratifiedKFold` with `cross_val_predict`
- Metrics: **Accuracy, Precision, Recall, F1-Score**
- Final model tested on completely **unseen test data**

> Final model achieved excellent recall on minority class while maintaining overall accuracy.

---

## 🧠 Best Model: SVM (Support Vector Machine)
- SVM outperformed others in detecting frauds with high recall.
- Tuned hyperparameters manually for efficiency and generalization.
- Trained on SMOTE-balanced data.

---

## 🚀 Deployment with Streamlit
- Created an interactive **Streamlit app**.
- Users can manually input feature values for:
  - `V17`, `V12`, `V14`, `V16`, `V10`, `V11`, `V18`, `V9`, `V7`, `V4`
- Displays prediction result (Fraud or Legit).

> The trained SVM model and column metadata are stored as `.pkl` files using `joblib`.

---

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/fraud-detection-svm.git
   cd fraud-detection-svm
