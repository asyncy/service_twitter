from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from json import dumps
import requests
import threading
import sys


class Stream(threading.Thread):
    def __init__(self, auth, subscription):
        threading.Thread.__init__(self)
        stream = TwitterStream(auth=auth, block=True)
        self.stopped = False
        if subscription['data'].get('isTesting') is not None and subscription['data'].get('isTesting') != "" :
            self.testing = subscription['data'].get('isTesting')
        else:
            self.testing = False
        self.endpoint = subscription['endpoint']

        if subscription['data'].get('track'):
            self.iterator = stream.statuses.filter(
                track=subscription['data']['track'])
        else:
            self.iterator = stream.statuses.sample()

    def stop(self):
        self.stopped = True

    def run(self):
        for tweet in self.iterator:
            if self.stopped:
                raise StopIteration
            elif tweet is None:
                print('Stream: No output')
            elif tweet is Timeout:
                print('Stream: Timeout')
            elif tweet is HeartbeatTimeout:
                print('Stream: Heartbeat Timeout')
            elif tweet is Hangup:
                print('Stream: Hangup')
            elif tweet.get('text'):
                requests.post(
                    self.endpoint,
                    headers={'Content-Type': 'application/json'},
                    data=dumps({
                        'eventType': 'tweet',
                        'cloudEventsVersion': '0.1',
                        'contentType': 'application/vnd.omg.object+json',
                        'eventID': tweet['id'],
                        'data': tweet
                    })
                )
                if self.testing is True :
                    sys.exit()
            else:
                print(f'Stream: Other {str(tweet)}')
                if self.testing is True :
                    sys.exit()