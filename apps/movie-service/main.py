from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
import random

app = FastAPI(tile="KubeFlix", description="A FastAPI service for movie lovers", version="1.0")

# Dummy movie data
movies = [
    {"id": 1, "title": "The Matrix", "year": 1999, "genre": "Sci-Fi", "rating": 8.7},
    {"id": 2, "title": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.8},
    {"id": 3, "title": "The Godfather", "year": 1972, "genre": "Crime", "rating": 9.2},
    {"id": 4, "title": "Interstellar", "year": 2014, "genre": "Adventure", "rating": 8.6},
    {"id": 5, "title": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0},
    {"id": 6, "title": "Pulp Fiction", "year": 1994, "genre": "Crime", "rating": 8.9},
    {"id": 7, "title": "Fight Club", "year": 1999, "genre": "Drama", "rating": 8.8},
    {"id": 8, "title": "Forrest Gump", "year": 1994, "genre": "Drama", "rating": 8.8},
    {"id": 9, "title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "genre": "Fantasy", "rating": 8.8},
    {"id": 10, "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "rating": 9.3},
    {"id": 11, "title": "The Godfather Part II", "year": 1974, "genre": "Crime", "rating": 9.0},
    {"id": 12, "title": "The Lord of the Rings: The Return of the King", "year": 2003, "genre": "Fantasy", "rating": 8.9},
    {"id": 13, "title": "The Lord of the Rings: The Two Towers", "year": 2002, "genre": "Fantasy", "rating": 8.8},
    {"id": 14, "title": "The Empire Strikes Back", "year": 1980, "genre": "Sci-Fi", "rating": 8.7},
    {"id": 15, "title": "The Silence of the Lambs", "year": 1991, "genre": "Thriller", "rating": 8.6},
    {"id": 16, "title": "Se7en", "year": 1995, "genre": "Crime", "rating": 8.6},
    {"id": 17, "title": "The Green Mile", "year": 1999, "genre": "Drama", "rating": 8.6},
    {"id": 18, "title": "Gladiator", "year": 2000, "genre": "Action", "rating": 8.5},
    {"id": 19, "title": "The Prestige", "year": 2006, "genre": "Drama", "rating": 8.5},
    {"id": 20, "title": "The Departed", "year": 2006, "genre": "Crime", "rating": 8.5}
]


@app.get("/movies", tags=["Movies"])
def get_movies():
	return movies 


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Service!"}

@app.get("/movies/{movie_id}", tags=["Movies"])
def get_movie_by_id(movie_id: int):
     movie = next((m for m in movies if m["id"] == movie_id), None)
     if movie is None:
           raise HTTPException(status_code=404, detail="Movie not found!")
     return movie
     
@app.get("/search", tags=["Movies"])
def search_movies(title: str = Query(..., min_length=1, description="Title to search for")):
    results = [movie for movie in movies if title.lower() in movie["title"].lower()]
    return results if results else {"message": "No matching movies found."}

@app.get("/recommendations", tags=["Fun"])
def recommend_movie(count: int = 1):
    return random.sample(movies, min(count, len(movies)))

@app.get("/genres", tags=["Movies"])
def list_genres():
    genres = list({movie["genre"] for movie in movies})
    return {"available_genres": genres}

@app.get("/top-rated", tags=["Movies"])
def get_top_rated(limit: int = 3):
    top_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)[:limit]
    return top_movies

@app.post("/add-movie", tags=["Admin"])
def add_movie(title: str, year: int, genre: str, rating: float):
    new_id = max(movie["id"] for movie in movies) + 1
    new_movie = {"id": new_id, "title": title, "year": year, "genre": genre, "rating": rating}
    movies.append(new_movie)
    return {"message": "Movie added successfully!", "movie": new_movie}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)
