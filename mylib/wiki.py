import wikipedia as wiki

#build a function to get the summary of a wikipedia page
def get_summary(topic):
    """
    This function returns the summary of a wikipedia page
    :param topic: the topic of the wikipedia page
    """
    return wiki.summary(topic)

#build a function to search the wikipedia page for a match
def search_wiki(topic):
    """
    This function searches the wikipedia page for a match
    :param topic: the topic of the wikipedia page
    """
    return wiki.search(topic)

#build a function to return the wikipedia page
def get_page(topic):
    """
    This function returns the wikipedia page
    :param topic: the topic of the wikipedia page
    """
    return wiki.page(topic)





