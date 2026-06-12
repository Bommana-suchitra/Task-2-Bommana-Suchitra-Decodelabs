from sklearn.datasets import load_iris
from src.evaluate import evaluate_model
from src.preprocess import preprocess_data
from src.train import train_model
from src.visualize import plot_confusion_matrix

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = preprocess_data(X, y)

model = train_model(X_train, y_train)
evaluate_model(
    model,
    X_test,
    y_test
)
plot_confusion_matrix(
    model,
    X_test,
    y_test
)



print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
print("Model trained successfully")