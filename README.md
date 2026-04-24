# 🎬 Movie Recommendation System

This project is a Content-Based Movie Recommendation System built using Machine Learning and NLP techniques. It recommends movies similar to a given movie based on genres, keywords, cast, and overview.

---

## 🚀 Features

- Recommend top 5 similar movies  
- Uses movie metadata (genre, keywords, cast, director)  
- Fast similarity-based recommendations  
- Beginner-friendly implementation  

---

## 🧠 Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- CountVectorizer (NLP)  
- Cosine Similarity  

---

## ⚙️ How It Works

1. Load movie and credits datasets  
2. Merge datasets based on title  
3. Extract important features (genres, keywords, cast, crew, overview)  
4. Combine features into a single text column  
5. Convert text into vectors using CountVectorizer  
6. Compute similarity using cosine similarity  
7. Recommend top 5 similar movies  

---

## 📂 Project Structure

movie_recommender_clean/
- main.py  
- movies.csv  
- credits.csv  

---

## ▶️ How to Run

1. Install required libraries:  
pip install pandas scikit-learn  

2. Run the project:  
python main.py  

3. Enter a movie name:  
Avatar  

---

## 🎯 Example

Input: Avatar  

Output:  
Recommended movies:  
John Carter  
Guardians of the Galaxy  
...  

---

## 💡 Future Improvements

- Add Streamlit UI  
- Show movie posters using API  
- Deploy as web application  
- Add collaborative filtering  

---

## 📌 Author

kalyani  

---

## ⭐ Note

This is an intermediate-level project demonstrating NLP techniques, feature engineering, and similarity-based recommendation systems.

---

⭐ If you like this project, give it a star!

