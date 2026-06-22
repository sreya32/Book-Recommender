import streamlit as st
import pickle
import numpy as np

# Load files
pivot = pickle.load(open("pivot.pkl", "rb"))
predicted_ratings = pickle.load(open("svd_predictions.pkl", "rb"))
book_names = pickle.load(open("book_names.pkl", "rb"))

st.title("📚 Book Recommendation System")

user_id = st.number_input(
    "Enter User ID",
    min_value=int(pivot.index.min()),
    max_value=int(pivot.index.max())
)

if st.button("Recommend Books"):

    if user_id in pivot.index:

        user_index = list(pivot.index).index(user_id)

        scores = predicted_ratings[user_index]

        recommended = np.argsort(scores)[::-1]

        st.subheader("Recommended Books")

        count = 0
        for i in recommended:
            book = book_names[i]

            if pivot.iloc[user_index, i] == 0:
                st.write(book)
                count += 1

            if count == 10:
                break

    else:
        st.error("User ID not found.")