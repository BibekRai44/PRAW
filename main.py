import praw
from datetime import datetime,timezone

client_id='7x63b4H0_0d2W5DKK61TSA'
client_secret='NFoNppi9lNNZZgGuyiZpdvpVAc5_5A'
user_agent="Scraper 1.0 by u/Bibek44 "

subreddit_name='Nepal'

start_date = datetime(2023, 3, 17, 0, 0, 0, tzinfo=timezone.utc)
end_date = datetime(2023, 3, 18, 0, 0, 0, tzinfo=timezone.utc)

user_agent="Scraper 1.0 by u/Bibek44 "

def top_post_stats(subreddit_name, time_filter):
    reddit = praw.Reddit(client_id='7x63b4H0_0d2W5DKK61TSA',
                        client_secret='NFoNppi9lNNZZgGuyiZpdvpVAc5_5A',
                        user_agent=user_agent)

    top_by_upvotes = None
    for submission in reddit.subreddit(subreddit_name).top(limit=1):
        if submission.score > 0:
            top_by_upvotes = submission
            break

    if top_by_upvotes is not None:
        print('Top post by upvotes: "{}" with {} upvotes ({})'.format(top_by_upvotes.title, top_by_upvotes.score,top_by_upvotes.permalink))
    else:
        print('No posts found that meet the search criteria.')

    top_by_comments = None
    for submission in reddit.subreddit(subreddit_name).top(time_filter='day', limit=1):
        if submission.num_comments > 0:
            top_by_comments = submission
            break

    if top_by_upvotes is not None:
        print('Top post by comments: "{}" with {} comments ({})'.format(top_by_comments.title, top_by_comments.num_comments,top_by_comments.permalink))
    else:
        print('No posts found that meet the search criteria.')

    with open('top_posts.html', 'w') as f:
        f.write('<html>\n<head>\n<title>Top Posts on r/{}</title>\n</head>\n<body>\n'.format(subreddit_name))
        if top_by_upvotes is not None:
            f.write('<p>Top post by upvotes: <a href="{}">{}</a> with {} upvotes</p>\n'.format(top_by_upvotes.permalink, top_by_upvotes.title, top_by_upvotes.score))
        if top_by_comments is not None:
            f.write('<p>Top post by comments: <a href="{}">{}</a> with {} comments</p>\n'.format(top_by_comments.permalink, top_by_comments.title, top_by_comments.num_comments))
        f.write('</body>\n</html>')

top_post_stats('Nepal', time_filter='day')
