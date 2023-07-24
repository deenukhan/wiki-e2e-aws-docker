"""
    This file is the main file of the application.
    We will be using FAST Api and mylib/wiki.py module to build a REST API.
"""

import uvicorn
import wikipedia as wiki
from fastapi import FastAPI
from pydantic import BaseModel

class Topic(BaseModel):
    """
    This class is used to validate the topic input
    """
    topic: str

# create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
def read_root():
    """
    This function returns the root path
    """
    return "Welcome to the wikipedia app"


@app.post("/summary")
def get_summary(topic: Topic):
    """
    This function returns the summary of a wikipedia page
    :param topic: the topic of the wikipedia page
    """
    return wiki.summary(topic.topic)

@app.post("/search")
def search_wiki(topic: Topic):
    """
    This function searches the wikipedia page for a match
    :param topic: the topic of the wikipedia page
    """
    return wiki.search(topic.topic)

@app.post("/page")
def get_page(topic: Topic):
    """
    This function returns the wikipedia page
    :param topic: the topic of the wikipedia page
    """
    return wiki.page(topic.topic).content


# @app.get("/summary/{topic}")
# def get_summary(topic):
#     """
#     This function returns the summary of a wikipedia page
#     :param topic: the topic of the wikipedia page
#     """
#     return wiki.summary(topic)


# @app.get("/search/{topic}")
# def search_wiki(topic):
#     """
#     This function searches the wikipedia page for a match
#     :param topic: the topic of the wikipedia page
#     """
#     return wiki.search(topic)


# @app.get("/page/{topic}")
# def get_page(topic):
#     """
#     This function returns the wikipedia page
#     :param topic: the topic of the wikipedia page
#     """
#     return wiki.page(topic)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
