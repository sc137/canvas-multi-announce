# Create an Announcement across Multiple Canvas Courses

Add your canvas URL and API Key to `create_multi_announcement.py`.

Run from the cli with your announcement file as the argument.

`$ ./create_multi_announcement.py test.md`

## Delay your post

The post time format is: YYYY-MM-DDTHH:MM:SSZ

You can enter the time to post manually. Note the literal T and Z characters.

All timestamps are UTC (add 7 or 8 hours for Los Angeles).

## Requirements

- Python 3
- pip3 canvasapi
- pip3 markdown

## Project Links

- [UCFOPEN CanvasAPI Github](https://github.com/ucfopen/canvasapi)
- [CanvasAPI Documentation](https://canvasapi.readthedocs.io/en/stable/getting-started.html)
- [Canvas LMS API Documentation](https://canvas.instructure.com/doc/api/index.html)