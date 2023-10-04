import os

class Blog:
    def __init__(self):
        self.posts = []
        self.post_directory = "blog_posts"
        os.makedirs(self.post_directory, exist_ok=True)

    def create_post(self, title, content):
        post = {"title": title, "content": content}
        self.posts.append(post)
        self.save_post_to_file(title, content)

    def save_post_to_file(self, title, content):
        post_filename = os.path.join(self.post_directory, f"{title}.txt")
        with open(post_filename, "w") as file:
            file.write(content)

    def read_posts(self):
        for index, post in enumerate(self.posts):
            print(f"Post {index + 1}:")
            print(f"Title: {post['title']}")
            print(f"Content: {post['content']}")

    def update_post(self, index, title, content):
        if 1 <= index <= len(self.posts):
            post = {"title": title, "content": content}
            self.posts[index - 1] = post
            self.save_post_to_file(title, content)
        else:
            print("Invalid post index.")

    def delete_post(self, index):
        if 1 <= index <= len(self.posts):
            post = self.posts.pop(index - 1)
            post_title = post['title']
            self.delete_post_file(post_title)
        else:
            print("Invalid post index.")

    def delete_post_file(self, title):
        post_filename = os.path.join(self.post_directory, f"{title}.txt")
        if os.path.exists(post_filename):
            os.remove(post_filename)

def main():
    blog = Blog()

    while True:
        print("Options:")
        print("1. Create a new post")
        print("2. Read all posts")
        print("3. Update a post")
        print("4. Delete a post")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title: ")
            content = input("Enter the content: ")
            blog.create_post(title, content)
            print("Post created!")
        elif choice == "2":
            blog.read_posts()
        elif choice == "3":
            index = int(input("Enter the post index to update: "))
            title = input("Enter the new title: ")
            content = input("Enter the new content: ")
            blog.update_post(index, title, content)
            print("Post updated!")
        elif choice == "4":
            index = int(input("Enter the post index to delete: "))
            blog.delete_post(index)
            print("Post deleted!")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

