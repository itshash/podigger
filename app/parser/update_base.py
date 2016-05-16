from sqlalchemy import exists
import json
from . parser import get_episodes
from app.api.models import Tag, Episode, Podcast, db


class EpisodeUpdater(object):

    def __init__(self, feeds):
        self.feeds = feeds
        self.episodes = {}

    def populate(self):

        for link in self.feeds:

            pod = Podcast.query.filter_by(feed=link).first()
            podcast = json.loads(get_episodes(link[0]))

            for item in podcast['items']:
                episode = {}
                tag_list = []

                episode['podcast'] = podcast['title']
                episode['title'] = item['title']
                episode['link'] = item['link']
                episode['description'] = item['description']
                episode['published'] = item['published']

                if 'tags' in item:
                    episode['tags'] = item['tags']

                    for tag in episode['tags']:
                        tag_exists = db.session.query(exists().where(Tag.name == tag)).first()

                        if not tag_exists:
                            t = Tag(name=tag)
                            db.session.add(t)
                            tag_list.append(t)

                if 'enclosure' in item:
                    episode['enclosure'] = item['enclosure']
                else:
                    episode['enclosure'] = None

                episode_exists = db.session.query(Episode).filter_by(link=episode['link']).first()

                if not episode_exists:
                    ep = Episode(
                        title=episode['title'],
                        link=episode['link'],
                        description=episode['description'],
                        published=episode['published'],
                        enclosure=episode['enclosure'],
                        podcast_id=pod.id,
                        data_json=episode
                    )

                    if tag_list:
                        ep.tags.append(tag_list)

                    db.session.add(ep)
                    db.session.commit()
