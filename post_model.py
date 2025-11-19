class Post:
    """
    The class that defines a post on the forum.
    "replies" is intended to be a list of Post objects.   
    """
    def __init__(self, id, title, author, messagetype, time, content, replies):
        self.id = id
        self.title = title
        self.author = author
        self.messagetype = messagetype
        self.time = time
        self.content = content
        self.replies = replies