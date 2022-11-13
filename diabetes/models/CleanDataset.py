def cleanDataset(df):
    #Import libraries
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import seaborn as sns 
    import warnings #avoid warning flash
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import QuantileTransformer
    warnings.filterwarnings('ignore')


    df.drop(['ID', 'No_Pation'], axis=1, inplace=True)
    df=df.drop_duplicates()

    df = df.rename({"CLASS": "Outcome"}, axis=1)

    #The strings of output show different format
    df.loc[df['Outcome'] == 'Y ', 'Outcome'] = 'Y'
    df.loc[df['Outcome'] == 'N ', 'Outcome'] = 'N'
    df.loc[df['Gender'] == 'f', 'Gender'] = 'F'
    df = df.drop(df[df['Outcome'] == 'P'].index)
    
    #Transform categorial to numeric data
    encoder = LabelEncoder()

    # apply on df
    df['Outcome'] = encoder.fit_transform(df['Outcome'])
    df['Gender']= encoder.fit_transform(df['Gender'])

    #Quantile transformation
    column_names = list(df.columns)

    x=df
    quantile  = QuantileTransformer()
    X = quantile.fit_transform(x)

    df_quantile=quantile.transform(X)
    df_quantile=pd.DataFrame(X)
    df_quantile.columns = column_names
    
    #feature selection
    df_cleaned = df_quantile.drop(['LDL', 'HDL','Cr', 'Urea','Gender'], axis=1)
    
    return df_cleaned