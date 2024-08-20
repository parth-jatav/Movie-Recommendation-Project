# 🎬 Movie Recommendation System

<img src = "deploy.png">

**[Live Demo: movie-recommendation-all.streamlit.app](https://movie-recommendation-all.streamlit.app/)**  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommendation-all.streamlit.app/)  

Your go-to tool for finding your next favorite movie!

## 🚀 Overview

The **Movie Recommendation System** is a content-based machine learning project that suggests movies similar to a selected movie. Built with Python and Streamlit, this project offers a sleek and interactive web app to explore movie recommendations.

![Movie Popcorn](https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif)

## 🏗️ Project Structure

- **📊 Data Collection**: 
  - Datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` from Kaggle.
  - Data includes genres, keywords, cast, crew, and more!

- **🛠️ Data Preprocessing**:
  - Merged datasets and selected relevant columns.
  - Handled missing values, duplicates, and converted data into usable formats.
  - Created a `tags` column combining genres, cast, crew, and keywords.

- **🤖 Model Creation**:
  - Used `CountVectorizer` for vectorizing tags and calculated cosine similarity.
  - Pickle files save the model and data for quick access.

- **🌐 Website Development**:
  - Built with Streamlit to deliver an interactive experience.
  - Displays recommended movies with posters fetched from TMDB API.

- **🚀 Deployment**: 
  - The app is deployed and ready for you to explore!

![Web App Demo](https://media.giphy.com/media/l3vQXTnTzT7kq7g1i/giphy.gif)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parth-jatav/movie-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## 🎥 Usage

1. Select a movie from the dropdown menu.
2. Click the "Get Recommendations" button.
3. View the recommended movies along with their posters.

![Movie Posters](https://media.giphy.com/media/26FL1soZ3STRDSLGU/giphy.gif)

## 📂 Dataset

- **Source**: Datasets are sourced from Kaggle:
  - [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## 🎯 Features

- **Content-Based Filtering**: Recommends movies based on metadata similarity.
- **Interactive UI**: Built with Streamlit for a smooth user experience.
- **Dynamic Posters**: Fetches movie posters from the TMDB API.

![Interactive UI](https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif)

## 🛠️ Libraries Used

- **Pandas** 🐼
- **NumPy** 🔢
- **NLTK** 🧠
- **Scikit-learn** 📈
- **Streamlit** 🌐
- **Requests** 🌍
- **Pickle** 🥒

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or bug reports.

![Coding](https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- Thanks to [TMDB](https://www.themoviedb.org/) for the movie data.
- Kudos to Kaggle for hosting the datasets.

![Thank You](https://media.giphy.com/media/l4FGGafcOHmrlQxGk/giphy.gif)
