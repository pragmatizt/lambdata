from sklearn.model_selection import train_test_split

def my_function():
    print('hello world')

def ira_split_version(X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.5, test_size=0.5, random_state=42)

    print("X_train:", X_train.shape)
    print("X_val:", X_val.shape)
    print("y_train:", y_train.shape)
    print("y_val:", y_val.shape)

    return (X_train, X_val, y_train, y_val)

def find_nulls(df):
    f_nulls = df.isnull().sum()

    return f_nulls
