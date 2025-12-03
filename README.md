# Movie Critic Rating Prediction
MSDS – Machine Learning & Data Science Project

This project builds a predictive model that estimates a movie’s critic rating using pre-release information such as genre, runtime, and MPAA rating. 
The project includes data extraction from PostgreSQL, data cleaning, exploratory data analysis, feature engineering, and linear regression modeling.


## 1. Project Structure

Basic layout:

```arduino
movie-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env               # not included (ignored)
│
├── data/
│ └── movies_raw.csv
│
├── notebooks/
│ └── project.ipynb    # Full analysis, EDA, feature engineering, modeling
```


## 2. Data Source
The raw data was obtained from the **Northwestern MLDS PostgreSQL server**, inside the database:

```cpp
everything2025.public.movies
```

Data was extracted using the Python library **psycopg** through a secure `.env` file for database credentials.

## 3. Key Steps in the Project
### 1. Data Cleaning & EDA
- Converted release dates, fixed erroneous years (e.g., 20xx → 19xx)
- Visualized yearly theatrical releases
- Identified *popular* movies using audience review counts
- Examined MPAA rating distributions
- Created pair plots to explore runtime, genre, and rating relationships
  
### 2. Feature Engineering
Created new predictive features, including:
- `kid_friendly` (1 if rating is G/PG)
- Genre dummy variables (multi-label exploding)
- `genre_count` (number of genres per film)
- `runtime_ratio` (runtime divided by decade average)
- `decade` and `movie_age` features
- `runtime_sq` quadratic term

### 3. Modeling
Six linear regression models were trained:
1. **Model 1:** runtime_in_minutes  
2. **Model 2:** runtime_in_minutes + kid_friendly  
3. **Model 3:** runtime + kid_friendly + genre dummies  
4. **Model 4:** Model 3 + genre_count  
5. **Model 5:** Model 4 + runtime_ratio  
6. **Model 6:** Model 5 + runtime_sq  

### 4. Model Evaluation
Each model was evaluated using:
- **R²** (variance explained)
- **MAE** (mean absolute error)
- **RMSE** (root mean squared error)

| Model   | R²       | MAE       | RMSE      |
| ------- | -------- | --------- | --------- |
| Model 1 | 0.001376 | 24.375345 | 28.319368 |
| Model 2 | 0.001037 | 24.413898 | 28.324169 |
| Model 3 | 0.154660 | 21.999101 | 26.055424 |
| Model 4 | 0.154660 | 21.999101 | 26.055424 |
| Model 5 | 0.149498 | 22.115487 | 26.134861 |
| Model 6 | 0.153889 | 22.032113 | 26.067301 |

**Model 3 performed the best**, showing that genre is the strongest predictor of critic ratings.

Insights include:
- **Genre** is the most impactful predictor of critic ratings.
- Adding `genre_count`, `runtime_ratio`, or quadratic terms produced **minimal marginal improvement**, suggesting linear models may struggle with the limited feature set.

