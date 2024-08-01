# Movie Recommendation System

This repository contains a Movie Recommendation System built with Streamlit. The system recommends movies based on user input using machine learning models and a dataset of movies. The project utilizes Git Large File Storage (LFS) to handle large files such as model weights and datasets.

## Features
1. **Interactive UI:** Built with Streamlit for a responsive and user-friendly interface.
2. **Movie Recommendations:** Provides personalized movie recommendations based on selected movies.
3. **Data Handling:** Efficient handling of large datasets and models using Git LFS.

## Getting Started
To get a local copy up and running, follow these steps:


### Prerequisites: 
1. Python 3.x
2. pip (Python package installer)
3. Git LFS (Large File Storage)

### Installation: 
1. Clone the repository:
```bash
git clone https://github.com/rahulkumarmmmut/movie_recommendation_system.git
cd movie_recommendation_system
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. **Generate Model Files:**
The .pkl files in this project are specific to my model. You need to use the dataset to extract your own .pkl files, which you can generate by executing the last few steps in the model development part of the Jupyter notebook.
Run the model development steps in your local environment to generate movies.pkl, movie_dict.pkl, and similarity.pkl.
After generating those .pkl files, paste them in your project folder.

4. **Update API Key:**
Make sure to update your TMDB API key in the fetch_poster function in the app.py file.
5. Run the application:
```bash
streamlit run app.py
```

## Usage
1. Select a movie from the dropdown menu.
   ![image](https://github.com/user-attachments/assets/031cb416-b763-41af-b38b-99a96f2c4a1b)
3. Click on the "Recommend" button to get movie recommendations.
 ![image](https://github.com/user-attachments/assets/310d88ab-ffd0-4c77-8a4f-22e447cf15a3)
5. View the recommended movies along with their posters.
   ![image](https://github.com/user-attachments/assets/9343ccfb-69ec-4455-a25e-fa92ff063fb6)



## Data Processing and Model Development
### Data Processing
1. **Data Merging:** Combined tmdb_5000_movies.csv and tmdb_5000_credits.csv datasets.
2. **Feature Extraction:** Extracted genres, keywords, cast, and crew information.
3.  Used ast.literal_eval to parse stringified lists.
4. Extracted relevant features into lists of strings.

### Text Preprocessing:
1. Removed spaces in feature elements.
2. Combined features into a single tags column.
3. Converted text to lowercase.
4. Applied stemming using NLTK's PorterStemmer.

### Model Development
1. **Vectorization:** Converted text data to vectors using CountVectorizer with a max of 5000 features and English stop words.
2. **Similarity Calculation:** Computed cosine similarity between movie vectors to find similar movies.
3. **Recommendation Function:** Implemented a function to recommend the top 5 similar movies based on user input.

### Integration and Deployment
1. **Streamlit App:** Built an interactive web application using Streamlit.
Created UI components to select movies and display recommendations.
2. **TMDB API Integration:** Used TMDB API to fetch movie posters.
3. **Git LFS:** Employed Git Large File Storage to handle and version large files like similarity.pkl.
4. **Deployment:** Deployed the application on Vercel for easy access and user interaction.

## Technical Details
 Programming Languages: Python
### Libraries and Frameworks: 
1. Data Processing: Pandas, NumPy
2. Machine Learning: Scikit-learn, NLTK
3. Web Application: Streamlit

APIs: TMDB (The Movie Database) API

Version Control and Deployment: Git, GitHub, Git LFS, Vercel
