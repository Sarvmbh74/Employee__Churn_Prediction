# Deployment link
https://employeechurnprediction-w6rdzewlcgmgmyhdfhjgwm.streamlit.app/

# 🧠 Employee Churn Prediction App

This is a **Streamlit web application** that predicts whether an employee is likely to **stay** or **leave** the company based on input features such as satisfaction level, number of projects, and more.

---

## 🚀 Features

- Predict employee churn using a trained `RandomForestClassifier` pipeline
- Clean and interactive UI with Streamlit sliders and dropdowns
- Input preprocessing is handled inside the pipeline (scaling + encoding)
- Displays result as **Yes (Leave)** or **No (Stay)** with prediction probability

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas / NumPy
- Pickle (for model serialization)

---

## 📂 Project Structure

employee_churn_prediction/
│
├── app.py # Streamlit frontend code
├── churn_pipeline.pkl # Trained and saved ML pipeline
├── requirements.txt # Dependencies
├── README.md # You're reading it!
└── data/ # (Optional) Raw data files for training


---

## ✅ How to Run Locally

1. **Clone the repo or download the files:**

```bash
git clone https://github.com/yourusername/employee_churn_prediction.git
cd employee_churn_prediction

| Feature                 | Type     | Description                        |
| ----------------------- | -------- | ---------------------------------- |
| satisfaction\_level     | Float    | Employee satisfaction (0.0 to 1.0) |
| last\_evaluation        | Float    | Last evaluation score (0.0 to 1.0) |
| number\_project         | Integer  | Number of projects worked on       |
| average\_montly\_hours  | Integer  | Monthly average working hours      |
| time\_spend\_company    | Integer  | Years spent in the company         |
| Work\_accident          | 0 or 1   | Whether they had a work accident   |
| promotion\_last\_5years | 0 or 1   | Whether they got promoted          |
| departments             | Category | Department (sales, IT, etc.)       |
| salary                  | Category | Salary level (low, medium, high)   |

