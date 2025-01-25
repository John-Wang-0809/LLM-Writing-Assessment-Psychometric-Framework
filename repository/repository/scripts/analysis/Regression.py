import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

def main():
    base_path = 'repository/data/processed'
    
    # Iterate through different datasets and versions
    for i in range(1, 4):  # 1-3
        for j in range(1, 5):  # 1-4
            file_path = os.path.join(base_path, f'Essay_Set_#{i}/machine_rater_data_{i}_{j}.csv')
            
            print(f"\nAnalyzing dataset {i}_{j}:")
            print("=" * 50)
            
            try:
                df = pd.read_csv(file_path, encoding='iso-8859-1')
            except Exception as e:
                print(f"Failed to read file: {e}")
                continue
            
            # For dataset 3, analyze by dimensions
            if i == 3:
                # Extract scores for 6 dimensions
                dimensions = ['Ideas_and_Content_Score', 'Organization_Score', 'Voice_Score', 
                            'Word_Choice_Score', 'Sentence_Fluency_Score', 'Conventions_Score']
                
                for dim in dimensions:
                    print(f"\nAnalyzing dimension: {dim}")
                    print("-" * 30)
                    
                    # Convert dimension data to wide format
                    df_wide = df.pivot(index='Essay_id', columns='Raters', values=dim)
                    
                    # Get all rater column names
                    rater_cols = df_wide.columns.tolist()
                    
                    # Perform regression analysis for each pair of raters
                    for k in range(len(rater_cols)-1):
                        for l in range(k+1, len(rater_cols)):
                            rater1 = rater_cols[k]
                            rater2 = rater_cols[l]
                            
                            # Prepare regression data
                            X = df_wide[[rater1]].values
                            y = df_wide[rater2].values
                            
                            # Build regression model
                            model = LinearRegression()
                            model.fit(X, y)
                            y_pred = model.predict(X)
                            
                            # Calculate regression metrics
                            slope = model.coef_[0]
                            intercept = model.intercept_
                            r_squared = r2_score(y, y_pred)
                            
                            # Output results
                            print(f"Regression analysis for Rater {rater1} vs Rater {rater2}:")
                            print(f"Slope: {slope:.4f}")
                            print(f"Intercept: {intercept:.4f}")
                            print(f"R²: {r_squared:.4f}")
                            print("-" * 50)
            
            # For datasets 1 and 2, analyze total scores directly
            else:
                # Convert data to wide format
                df_wide = df.pivot(index='Essay_id', columns='Raters', values='Scores')
                
                # Get all rater column names
                rater_cols = df_wide.columns.tolist()
                
                # Perform regression analysis for each pair of raters
                for k in range(len(rater_cols)-1):
                    for l in range(k+1, len(rater_cols)):
                        rater1 = rater_cols[k]
            # Get all rater column names
            rater_cols = df_wide.columns.tolist()
            
            # Perform regression analysis for each pair of raters
            for k in range(len(rater_cols)-1):
                for l in range(k+1, len(rater_cols)):
                    rater1 = rater_cols[k]
                    rater2 = rater_cols[l]
                    
                    # Prepare regression data
                    X = df_wide[[rater1]].values
                    y = df_wide[rater2].values
                    
                    # Build regression model
                    model = LinearRegression()
                    model.fit(X, y)
                    y_pred = model.predict(X)
                    
                    # Calculate regression metrics
                    slope = model.coef_[0]
                    intercept = model.intercept_
                    r_squared = r2_score(y, y_pred)
                    
                    # Output results
                    print(f"Regression analysis for Rater {rater1} vs Rater {rater2}:")
                    print(f"Slope: {slope:.4f}")
                    print(f"Intercept: {intercept:.4f}")
                    print(f"R²: {r_squared:.4f}")
                    print("-" * 50)

if __name__ == "__main__":
    main()
