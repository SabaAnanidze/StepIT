class User:
    def __init__(self, username):
        self.username = username
        self.posts = []      
        self.friends = set() 

    def add_friend(self, other_user: 'User'):
        self.friends.add(other_user)
        other_user.friends.add(self)

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def comment_on_post(self, post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
        return comment

    def like_post(self, post):
        post.add_like(self)

    def like_comment(self, comment):
        comment.add_like(self)


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author     
        self.comments = []       
        self.likes = []          

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author     
        self.likes = []          

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)



Saba = User("Saba")
Achi = User("Achi")

Saba.add_friend(Achi)


post1 = Saba.create_post("This is my first post!")

comment1 = Achi.comment_on_post(post1, "Nice post, Saba!")

Saba.like_comment(comment1)

post2 = Saba.create_post("This is my second post!")

Achi.like_post(post2)

#using for loop for printing infor because infos are values of objects

print(f"{Saba.username}'s friends:", [f.username for f in Saba.friends])
print(f"{Achi.username}'s friends:", [f.username for f in Achi.friends])
print(f"Post1 content: {post1.content}")
print("Post1 comments:", [(c.author.username, c.content) for c in post1.comments])
print("Likes on comment1:", [u.username for u in comment1.likes])
print(f"Post2 likes:", [u.username for u in post2.likes])
