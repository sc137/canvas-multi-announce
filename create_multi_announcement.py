#!/usr/bin/env python3
# create_multi_announcement.py
# sable cantus
# create a discussion post from a mardown file
# post to multiple CRNs

import sys
try:
    from canvasapi import Canvas
except ImportError as e:
    print("Please install the canvasapi module.")
    sys.exit()
try:
    import markdown
except ImportError as e:
    print("Please install the markdown module.")
    sys.exit()

# Enter the course numbers
# COURSE_NUMBERS = [
                    # '111111', # Course 1
                    # '111112', # Course 2
                    # '111113'  # Course 3
                    # ]


# Use a Sandbox for testing
COURSE_NUMBERS = [ '121331' ]

# Canvas API URL
# This will be the URL used to access your institutions canvas account
# e.g. https://<collegename>.instructure.com
API_URL = "https://<<collegename>>.instructure.com"

# Canvas API key
# Generate an api key in canvas <<canvas url>>/profile/settings
# Click New Access token and name it something you recognize
API_KEY = "<<canvas api key>>"

# Initiate the new Canvas object
canvas = Canvas(API_URL, API_KEY)

# Open the announcement file
if len(sys.argv) > 1:
    file_name = str(sys.argv[1])
    print('Selected file: {}'.format(file_name))
    title = input("Subject: ")
else:
    print("Please specify the announcement file.")
    print("usage: ./create_multi_announcement.py <filename>")
    sys.exit()

# set the time to post for a delayed message
print("post time format is: YYYY-MM-DDTHH:MM:SSZ")
print("literal characters T and Z")
print("All timestamps are UTC (add 7 or 8 hours)") 
delayed_post = input("Please enter the time to post (or blank to send now): ")

for COURSE_NUM in COURSE_NUMBERS:
    course = canvas.get_course(COURSE_NUM)
    print()
    print("Selected course: \n", course.name)
    print()

    # read in the message from a markdown file
    with open(file_name, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    message = markdown.markdown(text, extensions=['sane_lists'])

    post = course.create_discussion_topic(
        title=title,
        message=message,
        discussion_type='threaded',
        is_announcement=True,
        delayed_post_at=delayed_post
    )
    print('Created: ', post)
    print(post.url)
