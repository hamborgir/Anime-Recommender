# Anime Recommender System

This project simulates a recommender system using cosine similarity on an anime dataset. The web application is built with Flask and allows users to search for an anime and receive recommendations based on the selected anime.

## Description

The Anime Recommender System uses cosine similarity to provide recommendations for anime titles. By using weighted similarity score between the titles, genres, and synopses of various animes, the system can suggest similar animes that users might enjoy. The system uses a preprocessed dataset, and the similarity matrix is computed and stored in `similarity_matrix.npy` to enhance the efficiency of the recommendation process.

## Data Source

The dataset used for this project is sourced from [Kaggle's MyAnimeList Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?select=anime-dataset-2023.csv). This dataset contains detailed information about various anime titles, including genres, synopses, ratings, and more.

## Installation

To install and run the Flask application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hamborgir/Anime-Recommender.git
   cd Anime-Recommender
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the similarity matrix:**

   Before running the Flask app, open the `cleaner.ipynb` notebook and run all cells. This will generate the `similarity_matrix.npy` file, which is necessary for the recommendation system to function.
   
   ```bash
   cd model
   jupyter notebook cleaner.ipynb
   ```
6. **Run the Flask application:**

   ```bash
   cd..
   flask --app app.py run
   ```
   Runner also included in the code, so the `app.py` can just be run directly.
   ```bash
   cd..
   python app.py
   ```

7. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to use the Anime Recommender System.

## Usage

The application provides the following functionalities:

- **Search for Anime:** Users can search for an anime by typing in the search bar. The search results will display up to 10 matching titles, which are case-insensitive.
- **Anime Details:** Upon selecting an anime from the search results, detailed information about the anime is displayed, including the synopsis, genres, score, type, studios, rating, and favorites.
- **Recommendations:** The system generates and displays up to 10 recommended animes based on the cosine similarity calculated between the selected anime and others in the dataset.
- **Responsive Design:** The interface is built using Bootstrap and is fully responsive, ensuring a smooth user experience across different devices.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

---
