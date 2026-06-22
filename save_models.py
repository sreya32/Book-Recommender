import pickle

pickle.dump(pivot, open("pivot.pkl", "wb"))
pickle.dump(predicted_ratings, open("svd_predictions.pkl", "wb"))
pickle.dump(list(pivot.columns), open("book_names.pkl", "wb"))

print("Files created!")