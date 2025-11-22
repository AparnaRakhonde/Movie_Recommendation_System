# 🎬 Movie Recommendation System

## 👋 About the Project  

In a world with thousands of movie choices, users often struggle to find something they’ll enjoy watching next. Recommender systems help solve this by suggesting content based on a user’s preferences. This project aims to build a content-based movie recommender system that suggests movies similar to a selected one using metadata and text similarity.

This is a fun and interactive movie recommendation app built using **Python** and **Streamlit**. You choose a movie you like, and the app suggests 5 similar movies. It also shows you the posters for each movie, using data from the **TMDB API**.

---

## 📁 What’s Included  
- `app.py`: The main Streamlit app file  
- `movie_dict.pkl`: Contains movie information  
- `similarity.pkl`: Similarity scores between movies  
- `requirements.txt`: List of required Python libraries  

---

## 💡 How It Works  
1. You select a movie from the dropdown list  
2. The app uses cosine similarity to find similar movies  
3. It displays posters and titles of the top 5 recommended movies  

---

## 🔧 Getting Started

### ✅ Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/AparnaRakhonde/Movie_Recommendation.git
cd Movie_Recommendation

# Step 2: Install required libraries
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py
