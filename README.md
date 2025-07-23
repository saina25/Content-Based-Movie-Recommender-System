# 🎬 Movie Recommender System

This is a **content-based movie recommendation system** built using **Python**, **pandas**, **scikit-learn**, and **Streamlit**. It uses metadata such as genres, cast, crew, and keywords from the **TMDB 5000 Movie Dataset** to suggest movies similar to the one you select.

## 🚀 Features

* Recommends top 5 similar movies based on a selected title
* Uses NLP and cosine similarity for content-based filtering
* Clean, interactive interface built using Streamlit
* Efficient caching for fast load times

## 📁 Dataset

This app uses the following CSV files from the TMDB 5000 dataset:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

You can download the dataset from Kaggle:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 🛠️ How It Works

1. **Data Preprocessing**

   * Merges movie and credit datasets on the `title` column
   * Extracts genres, keywords, top 3 cast members, and the director
   * Cleans the text and combines all relevant metadata into a `tags` column

2. **Vectorization**

   * Converts the tags column into a vector using `CountVectorizer`
   * Limits to 5000 most frequent terms and removes English stop words

3. **Similarity Calculation**

   * Computes **cosine similarity** between movie vectors

4. **Recommendation**

   * Given a movie title, finds its vector and returns the top 5 most similar movies

## 📦 Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender-streamlit.git
cd movie-recommender-streamlit
```

### Install the required libraries:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
streamlit
pandas
scikit-learn
```

## ▶️ Run the App

```bash
streamlit run app.py
```

Make sure `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` are in the same directory as `app.py`.

## 🖥️ UI Preview

* Dropdown to select your favorite movie
* Button to generate recommendations
* Display of top 5 similar movies with emoji-enhanced UI

## 📌 Example

If you select **Inception**, the app might recommend:

```
👉 The Dark Knight  
👉 Interstellar  
👉 The Prestige  
👉 Batman Begins  
👉 Memento  
```

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
