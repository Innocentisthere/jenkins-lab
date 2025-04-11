import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def download_data():
    df = pd.read_csv('https://raw.githubusercontent.com/Innocentisthere/jenkins-lab/refs/heads/main/insurance.csv', delimiter = ',')
    df.to_csv("insurance.csv", index = False)
    return df

def clear_data(path2df):
    df = pd.read_csv(path2df)
    
    cat_columns = df.select_dtypes(include=object)
    num_columns = df.select_dtypes(exclude=object)

    # OneHotEncoding
    for col in cat_columns:
        to_add = pd.get_dummies(df[col], drop_first=True, dtype=float)
        df = pd.concat((df, to_add), axis=1)
        df = df.drop([col], axis=1)
    
    df.to_csv('df_clear.csv')
    return True

download_data()
clear_data("insurance.csv")