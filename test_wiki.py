"""
Let's write the pytest test cases for the wiki app.
"""

# Path: tests/test_wiki.py
import pytest
from mylib import wiki


# build a test function to test the get_summary function
def test_get_summary():
    """
    This function tests the get_summary function
    """
    topic = "Barack Obama"
    # get the summary of the wikipedia page
    summary = wiki.get_summary(topic)
    assert "Barack" in summary


# Build a test function to test the search_wiki function
def test_search_wiki():
    """
    This function tests the search_wiki function
    """
    topic = "Barack"
    # search the wikipedia page for a match
    search = wiki.search_wiki(topic)
    assert "Barack Obama" in search


# Build a test function to test the get_page function
def test_get_page():
    """
    This function tests the get_page function
    """
    topic = "Barack Obama"
    # get the wikipedia page
    page = wiki.get_page(topic)
    assert "Barack Obama" in page.title
    assert "Barack Hussein Obama II" in page.summary
    assert "Barack_Obama" in page.url
    assert page.pageid == "534366"
