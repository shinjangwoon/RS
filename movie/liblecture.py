from IPython.display import display, HTML
import numpy as np
import math
import pandas as pd


def displaymovies(movies, movieIds, rating=[]):

    html = ""

    for i, movieId in enumerate(movieIds):
        movie = movies[movies["movieId"] == movieId].iloc[0]

        html += f"""
            <div style="display:inline-block;min-width:150px;max-width:150px; vertical-align:top">
                <img src='{movie.imgurl}' width=120> <br/>
                <span>{movie.title}</span> <br/>
                {f"<span>{rating[i]}</span> <br/>" if len(rating) > 0 else ""}
                <ul>{"".join([f"<li>{genre}</li>" for genre in movie.genres.split('|')])}</ul>
            </div>
        
        """

    display(HTML(html))


def getMAE(real, pred):
    errors = real - pred
    return errors.abs().mean()


def getRMSE(real, pred):
    errors = real - pred
    return math.sqrt(errors.pow(2).mean())
