import Article 

class Author:
    all_authors = []

    def _init_(self, name):
        self.name = name
        self.authored_articles = []
        self._class_.all_authors.append(self)

    def _str_(self):
        return f"Author: {self.name}"

    @property
    def articles(self):
        return self.authored_articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.authored_articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self.authored_articles.append(new_article)

    @property
    def topic_areas(self):
        return list(set(article.magazine.category for article in self.authored_articles))