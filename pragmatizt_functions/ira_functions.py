from sklearn.model_selection import train_test_split

def my_function():
    print('hello world')

def train_test_split(X, y):
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, train_size=0.75, test_size=0.25, random_state=42
        )

    print("X_train:", X_train.shape)
    print("X_val:", X_val.shape)
    print("y_train:", y_train.shape)
    print("y_val:", y_val.shape)

    return (X_train, X_val, y_train, y_val)
