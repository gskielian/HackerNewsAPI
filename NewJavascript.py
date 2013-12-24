#!/usr/bin/env python

from hn import HN
import re
import sys
from time import sleep
from subprocess import call
hn = HN()



#myre = '[fF]irefox'


myre = '[jJ][sS]'

myre2 = '[jJ]avascript'

# print top stories from homepage
while True:
  for story in hn.get_stories():
    if re.search(myre, story.title) or re.search(myre2, story.title):
        print(story.title)
        call(['say',story.title])
        var = raw_input("Continue?")
  sleep(60);

#print('[{0}] "{1}" by {2}'.format(story.points, story.title, story.submitter))

'''
# print 10 latest stories
for story in hn.get_stories(story_type='newest')[:10]:
    story.title
    print('*' * 50)
    print('')

# print the top 10 stories from /best page
for story in hn.get_stories(story_type='best')[:10]:
    print(story.title)
    print('*' * 50)
    print('')

'''

'''
# for each story on front page, print top comment
for story in hn.get_stories():
    print(story.title)
    comments = story.get_comments()
    print(comments[0] if len(comments) > 0 else None)
    print('*' * 10)
'''

'''
# for top 5 comments with nesting for top 5 stories
for story in hn.get_stories()[:5]:
    print(story.title)
    comments = story.get_comments()
    if len(comments) > 0:
        for comment in comments[:5]:
            print('\t' * (comment.level + 1) + comment.body[:min(30, len(comment.body))])
    print('*' * 10)
'''
