# _Twitter_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

Do Twitter stuff in a microservice.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Follow
```coffee
>>> twitter follow handle:'screenName' user:'userID' follow:'true'
```
##### Unfollow
```coffee
>>> twitter unfollow handle:'screenName' user:'userID'
```
##### Followers
```coffee
>>> twitter followers handle:'screenName' user:'userID' cursor:'2' count:'50'
```
##### Retweet
```coffee
>>> twitter retweet tweet:'tweetID'
```
##### Tweet
```coffee
>>> twitter tweet status:'status'
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Follow
```shell
$ omg run follow -a handle=<SCREEN_NAME> -a user=<USER_ID> -a follow=<TRUE/FALSE> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```
##### Unfollow
```shell
$ omg run unfollow -a handle=<SCREEN_NAME> -a user=<USER_ID> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```
##### Followers
```shell
$ omg run followers -a handle=<SCREEN_NAME> -a user=<USER_ID> -a cursor=<RANGE_OF_PAGE> -a count=<MAX_USER_RANGE_PER_PAGE> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```
##### Retweet
```shell
$ omg run retweet -a tweet=<TWEET_ID> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```
##### Tweet
```shell
$ omg run tweet -a status=<STATUS> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```
##### Stream
```shell
$ omg subscribe stream tweet -a track=<STRING/PHRASES_LIST_TO_TRACK> -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> -e ACCESS_TOKEN=<ACCESS_TOKEN> -e ACCESS_TOKEN_SECRET=<ACCESS_TOKEN_SECRET>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/twitter/blob/master/LICENSE).
