import os
import praw
import time



class PatrickBot(object):
    '''
    No! This is Patrick!
    '''

    def __init__(self):
        self.r         = praw.Reddit(user_agent = 'shitty_patrick_bot')
        self.logged_in = False
        self.subreddits = ["benpringle", "starcraftcirclejerk"]

    def login(self):
        '''
        Returns True  if login was successful
        Returns False if an exception was thrown
        '''
        try:
            self.r.login('shitty_patrick_bot', os.environ['patrick_p'])
            self.logged_in = True
            return True

        except:
            return False


    def is_flagged_comment(self, comment):
        '''take in a comment, determine if its valid, return true'''
        comment = comment.lower().strip()
        if comment.startswith("is this"):
            return True
        else:
            return False
    

    def parse_comments(self, subreddit):
        subreddit = self.r.get_subreddit(subreddit)
        for submission in subreddit.get_new(limit = 25):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            for comment in flat_comments:
                text = comment.body
                if self.is_flagged_comment(text):
                    print (text)
                    print(dir(comment))
        return True

    def run(self):
        self.login()
        while True:
            for subreddit in self.subreddits:
               self.parse_comments(subreddit)
            time.sleep(15 * 60 * 60)

if __name__ == '__main__':

    bot = PatrickBot().run()





