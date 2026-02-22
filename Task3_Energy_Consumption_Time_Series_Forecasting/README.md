# Task 3: Household Energy Consumption Time Series Forecasting

## 🎯 Task Objective
The primary objective of this task is to forecast short-term household energy usage by leveraging historical time-based patterns. This involves preparing a time-series dataset, creating temporal features, training multiple forecasting models, and evaluating their effectiveness in predicting future energy consumption.

## 🛠️ Approach
1. **Data Preprocessing and Resampling:**
   * Loaded the `Household Power Consumption` dataset and cleaned missing or invalid values (`?`).
   * Parsed the `Date` and `Time` columns to create a proper Datetime index.
   * Resampled the minute-level target variable (`Global_active_power`) into **hourly averages**. Doing this mitigates noise and helps models capture underlying short-term trends much more effectively.

2. **Feature Engineering:**
   * Extracted specific time-based features from the Datetime index, including **Hour of Day**, **Day of Week**, **Month**, and a binary **Is Weekend** indicator.
   * These features are crucial because they help machine learning models (like XGBoost) understand cyclical, repeating human behavioral patterns that govern power usage.

3. **Model Implementation and Comparison:**
   * Divided the chronological data into a training set and a hold-out test set (e.g., forecasting the last 7 days / 168 hours).
   * Trained three distinct forecasting methodologies to present a comprehensive comparison:
      * **ARIMA**: A traditional statistical model utilizing sequential autoregression and moving averages. 
      * **Prophet**: A flexible forecasting procedure by Meta, designed to handle multiple macro seasonalities automatically (daily, weekly).
      * **XGBoost**: A powerful decision-tree ensemble algorithm that learns non-linear relationships using our engineered temporal features.

4. **Evaluation and Visualization:**
   * Measured and compared predictive accuracy on the unseen test dataset utilizing robust regressional metrics such as **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.
   * Visualized the actual vs. forecasted energy usage using `matplotlib` to investigate how well each model traced daily consumption peaks and troughs.

## 📊 Results and Findings
* **XGBoost** proved to be the most accurate model for this environment, achieving the lowest Mean Absolute Error (MAE: ~**0.015**). It successfully identified complex relationships by leveraging the engineered features (recognizing that energy usage surges depend heavily on the specific hour and whether people are home on weekends).
* **ARIMA** functioned as a solid statistical baseline, performing reasonably well (MAE: ~**0.79**). It successfully predicted continuous sequential dependencies but can struggle to capture dynamic volatility compared to tree ensembles.
* **Prophet** exhibited slightly higher overall error (MAE: ~**0.736**), but nonetheless demonstrated clear strengths in gracefully and transparently modeling the periodic daily and weekly distributions.

* **Overall Conclusion:** The visualizations confirmed that all models matched the general cyclical trends, but XGBoost mapped the sudden dynamic spikes in daytime/evening usage most accurately. This validates the importance of direct temporal feature generation in time-series forecasting.
