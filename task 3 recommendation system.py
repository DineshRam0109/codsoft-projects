import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
ratings_path = 'C:\\Users\\dines\\OneDrive\\Documents\\codsoft\\ratings.csv'
movies_path = 'C:\\Users\\dines\\OneDrive\\Documents\\codsoft\\movies.csv'

ratings = pd.read_csv(ratings_path)
movies = pd.read_csv(movies_path)

# Check if the data is loaded correctly
print("Ratings DataFrame:")
print(ratings.head())
print("\nMovies DataFrame:")
print(movies.head())

# Merge ratings and movie titles
movie_data = pd.merge(ratings, movies, on='movie_id')
print("\nMerged DataFrame:")
print(movie_data.head())

# Create User-Item Matrix
user_movie_matrix = movie_data.pivot_table(index='user_id', columns='title', values='rating')
print("\nUser-Movie Matrix:")
print(user_movie_matrix)

# Fill NaN with 0 for similarity calculation
user_movie_matrix_filled = user_movie_matrix.fillna(0)

# Calculate Movie Similarity
movie_similarity = cosine_similarity(user_movie_matrix_filled.T)
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Update User Rating Function
def update_user_rating(user_id, movie_title, new_rating):
    global user_movie_matrix, ratings, movies
    
    # Get the movie_id corresponding to the movie_title
    movie_id = movies[movies['title'] == movie_title]['movie_id'].values[0]
    
    # Update the user_movie_matrix
    user_movie_matrix.loc[user_id, movie_title] = new_rating
    
    # Check if the combination of user_id and movie_id already exists in the ratings DataFrame
    condition = (ratings['user_id'] == user_id) & (ratings['movie_id'] == movie_id)
    
    if condition.any():
        # Update the existing rating
        ratings.loc[condition, 'rating'] = new_rating
    else:
        # Add a new entry if the combination does not exist
        new_rating_entry = pd.DataFrame({'user_id': [user_id], 'movie_id': [movie_id], 'rating': [new_rating]})
        ratings = pd.concat([ratings, new_rating_entry], ignore_index=True)


# Recommendation Function
def recommend_movies(movie_title, user_id, user_movie_matrix, movie_similarity):
    user_ratings = user_movie_matrix.loc[user_id].dropna()

    # Check if the movie_title exists in the similarity index
    if movie_title not in movie_similarity.index:
        print(f"Movie '{movie_title}' not found in similarity index.")
        return pd.Series()  # Return an empty Series if the movie is not found

    similar_scores = movie_similarity[movie_title]
    similar_movies = similar_scores.drop(movie_title).dropna()

    # Ensure we only use movies the user has rated
    similar_movies = similar_movies[similar_movies.index.isin(user_ratings.index)]
    
    if similar_movies.empty:
        print("No similar movies found that the user has rated.")
        return pd.Series()  # Return an empty Series if no similar movies are found

    # Calculate collaborative recommendations
    collaborative_recommendations = user_ratings[similar_movies.index].dot(similar_movies) / similar_movies.sum()

    # Content-based filtering (placeholder for demonstration)
    content_recommendations = pd.Series(user_ratings.mean(), index=[movie_title])  # Make sure this is a Series

    # Combine recommendations
    recommendations = (collaborative_recommendations + content_recommendations) / 2
    
    # Ensure recommendations is a Series
    if isinstance(recommendations, pd.Series):
        recommendations = recommendations.sort_values(ascending=False)
    else:
        print("Error: Recommendations calculation did not return a Series.")
        return pd.Series()  # Return an empty Series if something went wrong
    
    return recommendations.head(5)


# Example Usage
user_id = 1
movie_title = 'The Matrix'

# Get initial recommendations
recommendations = recommend_movies(movie_title, user_id, user_movie_matrix, movie_similarity_df)
print(f"\nRecommendations for User {user_id} based on '{movie_title}':\n{recommendations}\n")

# Update user rating and get new recommendations
update_user_rating(user_id, 'Inception', 5)
new_recommendations = recommend_movies(movie_title, user_id, user_movie_matrix, movie_similarity_df)
print(f"Updated Recommendations for User {user_id} based on '{movie_title}':\n{new_recommendations}")
