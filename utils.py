import json

# Functions for posts
def get_data(filename: str)-> list:
    """Create list of all data from a json file

    Arguments:
    filename -- path to a file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_posts_by_user(filename: str, user_name: str)-> list:
    """Create list of posts by specific user from a json file

    Arguments:
    filename -- path to a posts file
    username -- name of a user
    """
    posts = get_data(filename)
    posts_found = [post for post in posts if user_name in post['poster_name']]
    return posts_found

def get_post_by_id(filename: str, post_id: int)-> dict:
    """Get post with the specified id from a json file

    Arguments:
    filename -- path to a posts file
    post_id -- id of the post
    """
    posts = get_data(filename)
    post_found = posts[post_id - 1]
    return post_found

def get_posts_for_word(filename: str, searched_word: str)-> list:
    """Get all posts which contain specific word from a json file

    Arguments:
    filename -- path to a posts file
    searched_word -- id of the post
    """
    posts = get_data(filename)
    posts_found = [post for post in posts if searched_word.lower() in post['content']]
    return posts_found

# Functions for comments
def get_comments_by_post_id(filename: str, post_id: int)-> list:
    """Get all comments post which contain specific word from a json file

    Arguments:
    filename -- path to a comments file
    post_id -- id of the associated post
    """
    comments = get_data(filename)
    comments_found = [comment for comment in comments if comment['post_id'] == post_id]
    return comments_found


# Test functions
if __name__ == '__main__':
    # get_posts
    posts = get_data('data/data.json')
    print(posts)
    # get_posts_by_user
    posts = get_posts_by_user('data/data.json', 'larry')
    print(posts)
    # get_post_by_pk
    post = get_post_by_id('data/data.json', 2)
    print(post)
    # get_posts_for_word
    posts = get_posts_for_word('data/data.json', 'тарелка')
    print(posts)
    # get_comments_by_post_id
    comments = get_comments_by_post_id('data/comments.json', 1)
    print(comments)