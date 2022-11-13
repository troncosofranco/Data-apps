import trainmodel

def trainModel(df_cleaned):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import RepeatedStratifiedKFold
    from sklearn.model_selection import GridSearchCV

    target_label='Outcome'
    y= df_cleaned[target_label]
    X=df_cleaned.drop(target_label,axis=1)

    X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=0) #80% train, 20% tes
    
    #Define model and parameters
    model = RandomForestClassifier()
    n_estimators = [150]
    max_features = ['sqrt', 'log2']

    #Define grid search methodology
    grid = dict(n_estimators=n_estimators,max_features=max_features)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    grid_search = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, scoring='accuracy',error_score=0)

    return model