from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    cm = confusion_matrix(
        y_test,
        predictions
    )
   

    print("\nAccuracy:", accuracy)
    print("\nF1 Score:", f1)
    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions
        )
    )
    with open("outputs/results.txt", "w") as file:
      file.write(f"Accuracy: {accuracy}\n")
      file.write(f"F1 Score: {f1}\n")