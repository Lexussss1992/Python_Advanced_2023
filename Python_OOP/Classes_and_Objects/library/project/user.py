class User:
    def __init__(self, use_id: int, username: str):
        self.user_id = use_id
        self.username = username
        self.books = []

    def info(self):
        return ", ".join(i for i in self.books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {', '.join(i for i in self.books)}"
