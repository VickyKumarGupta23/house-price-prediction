# House Price Prediction

A machine learning project that predicts house prices using the California Housing dataset, built with Python, Scikit-learn, and Pandas.

## 📌 Project Overview
This project applies regression models to predict median house values based on features like median income, house age, average rooms, and location (latitude/longitude). It compares a baseline Linear Regression model against a Random Forest Regressor to improve prediction accuracy.

## 🛠️ Tech Stack
- Python 3.11
- Jupyter Notebook (via VS Code)
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn

## 📊 Dataset
California Housing dataset (built into Scikit-learn), containing ~20,000 records with features:
- MedInc (median income)
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude, Longitude
- MedHouseVal (target — median house value)

## 🔍 Workflow
1. **EDA** — explored data distribution, checked for missing values, visualized correlations
2. **Feature/Target Split** — separated input features (X) and target variable (y)
3. **Train-Test Split** — 80/20 split for training and testing
4. **Model Training** — trained Linear Regression and Random Forest Regressor
5. **Evaluation** — compared models using R², MAE, and RMSE

## 📈 Results
| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| Linear Regression | ~0.60 | - | - |
| Random Forest Regressor | **0.8046** | 0.3277 | 0.5060 |

Random Forest significantly outperformed Linear Regression, achieving ~80% R² accuracy.

## 📁 Folder Structure
house-price-prediction/

├── data/

├── notebooks/

│   └── 01_EDA.ipynb

├── outputs/

│   ├── plots/

│   └── house_price_model.pkl

├── requirements.txt

└── README.md
## ▶️ How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Open `notebooks/01_EDA.ipynb` in VS Code or Jupyter
4. Run all cells

## 🔮 Future Improvements
- Hyperparameter tuning (GridSearchCV)
- Try Gradient Boosting / XGBoost
- Add cross-validation
- Deploy as a web app (Flask/Streamlit)
## For Run the project locally 
- pip install streamlit
- new app.py file add to the main project 
- streamlit run app.py to run the project locally