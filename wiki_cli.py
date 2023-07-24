"""
This is the command line tool which utilizes the functions in the mylib/wiki.py module.
"""

# Path: wiki_cli.py
import click
from mylib import wiki


@click.group()
def cli():
    """
    This is the command line tool which utilizes the functions in the mylib/wiki.py module.
    """


@cli.command("summary")
@click.argument("topic")
def get_summary(topic):
    """
    This function returns the summary of a wikipedia page
    :param topic: the topic of the wikipedia page

    example:
    $ python wiki_cli.py summary "Barack Obama"
    """
    # get the summary of the wikipedia page in colored output
    click.echo(click.style(wiki.get_summary(topic), fg="green"))


@cli.command("search")
@click.argument("topic")
def search_wiki(topic):
    """
    This function searches the wikipedia page for a match
    :param topic: the topic of the wikipedia page

    example:
    $ python wiki_cli.py search "Barack"
    """
    # search the wikipedia page for a match
    click.echo(click.style(str(wiki.search_wiki(topic)), fg="green"))


@cli.command("page")
@click.argument("topic")
def get_page(topic):
    """
    This function returns the wikipedia page
    :param topic: the topic of the wikipedia page

    example:
    $ python wiki_cli.py page "Barack Obama"
    """
    # get the wikipedia page
    click.echo(click.style(str(wiki.get_page(topic).content), fg="green"))


if __name__ == "__main__":
    cli()
