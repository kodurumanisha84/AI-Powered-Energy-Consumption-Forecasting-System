# ⚡ AI-Powered Energy Consumption Forecasting System

## 📌 Overview

This project is an **AI-based Energy Consumption Forecasting System** that predicts future electricity usage using Machine Learning.

It simulates a real-world industry scenario where organizations use historical energy data to **forecast future demand, reduce costs, and optimize energy usage**.

---

## 🎯 Problem Statement

Energy consumption is increasing rapidly across industries like:

* Smart Cities
* Manufacturing Plants
* Data Centers
* Electricity Boards

Without forecasting, organizations face:

* ❌ Energy wastage
* ❌ High electricity bills
* ❌ Poor resource planning

---

## 💡 Solution

This project uses **Machine Learning (Random Forest Regressor)** to:

* Analyze historical energy usage
* Learn patterns from time-series data
* Predict future energy consumption

---

## 🏭 Industry Relevance

This system can be used in:

* ⚡ Power distribution companies → demand forecasting
* 🏙️ Smart cities → optimize electricity usage
* 🏭 Factories → schedule machines efficiently
* 🖥️ Data centers → reduce power + cooling costs
* 🌞 Renewable energy → optimize energy supply

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📂 Project Structure

```
AI-Energy-Forecasting/
│
├── data/              # Dataset
├── src/               # Source code (optional)
├── models/            # Saved models
├── outputs/           # Prediction outputs
├── images/            # Screenshots for README         
│
├── generate_dataset.py
├── main.py
├── requirements.txt
├── README.md
```

---

## 📊 Dataset

* Time-series energy consumption data
* Generated using simulation (realistic pattern)
* Contains:

  * Date
  * Energy usage

---

## ⚙️ Features

* ✅ Dataset generation (simulation)
* ✅ Data preprocessing
* ✅ Feature engineering (day, month, lag values)
* ✅ Machine Learning model training
* ✅ Energy consumption forecasting
* ✅ Model evaluation (RMSE, R²)
* ✅ Visualization (Actual vs Predicted graph)

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/kodurumanisha84/AI-Energy-Consumption-Forecasting.git
cd AI-Energy-Consumption-Forecasting
```

### 2. Create Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Generate Dataset

```bash
python generate_dataset.py
```

### Step 2: Run Model

```bash
python main.py
```

---

## 📈 Output

### 🔹 Model Performance

* RMSE (Root Mean Square Error)
* R² Score

### 🔹 Visualization

* Actual vs Predicted Energy Consumption

---


## 🧠 How It Works

1. Generate or load energy dataset
2. Preprocess and clean data
3. Create time-based features
4. Train Random Forest model
5. Predict future energy consumption
6. Evaluate model performance
7. Visualize results

---

## 🔮 Future Improvements

* Add weather data (temperature, humidity)
* Use advanced models (ARIMA, LSTM)
* Deploy using Streamlit dashboard
* Real-time forecasting system

---

## 📚 Learning Outcomes

* Time Series Forecasting
* Machine Learning Pipeline
* Feature Engineering
* Model Evaluation
* Real-world project development
* GitHub project structuring

---

## 🙌 Author

**Koduru Manisha**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
