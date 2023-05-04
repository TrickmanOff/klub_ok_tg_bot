import os
import re
from dataclasses import dataclass
from typing import Dict

ARTICLE_FILENAME_PATTERN = '^article.*\.md$'


@dataclass
class Article():
    title: str
    content: str


def import_articles() -> Dict[str, Article]:
    articles: Dict[str, Article] = {}
    articles_dirpath = os.path.join(os.path.dirname(__file__), 'articles')
    for filename in os.listdir(articles_dirpath):
        if re.match(ARTICLE_FILENAME_PATTERN, filename):
            with open(os.path.join(articles_dirpath, filename), 'r') as file:
                title = file.readline()
                file.readline()
                content = ''.join(file.readlines())
            articles[os.path.basename(filename)] = Article(title, content)

    return articles


articles = import_articles()
