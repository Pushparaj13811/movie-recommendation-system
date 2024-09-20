# Movie Recommendation System

This is a movie recommendation system built using **Streamlit**, **scikit-learn**, and **pandas**. The system allows users to select a movie from a dropdown list, and it recommends similar movies based on the provided movie's title using content-based filtering. 

## Features

- **Movie Selection**: Users can select a movie from a dropdown list.
- **Recommendations**: The system recommends 5 movies similar to the selected movie.
- **Poster Display**: Displays posters of the recommended movies.
  
## How It Works

The recommendation system uses a content-based filtering technique. It calculates the cosine similarity between movie features and provides a list of movies similar to the selected one.

## Data Used

The movie recommendation system was built using the **The Movide database dataset**, which contains metadata about movies such as titles, genres, and ratings. The dataset is publicly available and widely used for building movie recommendation systems.

The following files were used in creating this system:

1. **movies.pkl**: This file contains the metadata of the movies, including movie titles, genres, and other relevant information. The data was pre-processed and stored as a pandas DataFrame for easy access during recommendations.

2. **similarity.pkl**: This file contains the pre-computed cosine similarity matrix between the movies based on the content features (such as genres, cast, and crew). The matrix is used to calculate and recommend similar movies.

### Dataset Source

- **Movies Dataset**: The Movies dataset is available at [kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
  
The data was cleaned and processed to focus on the movie title and features relevant for content-based filtering.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pushparaj13811/movie-recommendation-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system/movie-recommender-system 
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install **Git Large File Storage (Git LFS)** to handle the large files (e.g., `similarity.pkl`):
   - On macOS:
     ```bash
     brew install git-lfs
     ```
   - On Ubuntu:
     ```bash
     sudo apt-get install git-lfs
     ```
   - On Windows:
     Download and install [Git LFS](https://git-lfs.github.com/).

5. Initialize Git LFS in your local repository:
   ```bash
   git lfs install
   ```

6. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

## Files in the Repository

- `app.py`: Main Python script to run the movie recommendation system.
- `movies.pkl`: A pickled file containing movie metadata such as titles.
- `similarity.pkl`: A pre-computed similarity matrix used for recommendations (handled by Git LFS).

## How to Use

1. Select a movie from the dropdown list on the Streamlit web interface.
2. Click the "Recommend" button to get a list of similar movies.
3. Movie recommendations along with posters will be displayed on the page.

## Git Large File Storage (Git LFS)

This repository uses **Git LFS** to handle large files such as `similarity.pkl`. Make sure to install and set up Git LFS by following the steps under **Installation**.

## API Integration

The application fetches movie posters dynamically using The Movie Database (TMDb) API. To enable this functionality:
1. Sign up for an API key at [The Movie Database](https://www.themoviedb.org/).
2. Replace `YOUR_API_KEY` in `app.py` with your API key.

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- scikit-learn
- Requests
