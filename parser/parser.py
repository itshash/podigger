import feedparser
import re
import json

def get_episodes(feed):

    podcast = {}
    d = feedparser.parse(feed)
    no_tag = re.compile((r'(<!--.*?-->|<[^>]*>)'))

    podcast['title'] = d.feed.title
    podcast['items'] = []

    for entry in  d.entries:

        item = {}
        tags = []
        item['title'] = entry.title
        description = no_tag.sub('', entry.description)

        item['description'] = description

        for t in entry.tags:
            tags.append(t.term)

        item['tags'] = tags

        if entry.enclosures:
            item['enclosure'] = entry.enclosures[0].href

        podcast['items'].append(item)


    return json.dumps(podcast)