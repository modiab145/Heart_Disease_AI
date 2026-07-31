# Heart Disease Risk Prediction — Capstone Project

End-to-end machine learning project predicting heart disease risk from clinical,
lifestyle, and wearable-device data (NTI Final Project).

## Status: Phase 1 of 5 complete
- [x] **Phase 1** — Project structure, Business Understanding, Data Understanding, EDA
- [ ] Phase 2 — Data Cleaning, Feature Engineering, Feature Selection
- [ ] Phase 3 — Modeling, Hyperparameter Tuning, Ensemble Learning
- [ ] Phase 4 — Evaluation, Error Analysis, Explainability (SHAP/LIME)
- [ ] Phase 5 — Streamlit App, Final Report, Documentation

## Project Structure
```
heart_disease_project/
├── data/
│   ├── raw/            # original CSV
│   └── processed/      # cleaned/engineered data (Phase 2)
├── notebooks/
│   ├── 01_business_and_data_understanding.ipynb
│   └── 02_eda.ipynb
├── src/                # reusable pipeline code (Phase 2+)
├── models/             # saved trained models (Phase 3+)
├── reports/            # final report (Phase 5)
├── streamlit/          # deployed app (Phase 5)
├── images/             # exported EDA charts
└── requirements.txt
```

## Dataset
`heart_disease_risk_2026.csv` — 9,000 patients, 27 columns (clinical measurements,
lifestyle factors, wearable data). Target: `has_heart_disease` (binary, ~30% positive).

## Key Findings So Far (see notebooks for full detail)
- Mild class imbalance (70/30) → use stratified splits, prioritize Recall/F1/ROC-AUC over Accuracy.
- Strongest predictors: `max_heart_rate_achieved`, `st_depression`, `age`, `exercise_induced_angina`.
- No missing values; lipid panel features (cholesterol/LDL/triglycerides) are collinear.

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_business_and_data_understanding.ipynb
```
