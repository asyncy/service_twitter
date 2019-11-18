# _Twitter_ Open Microservice

> Twitter as a microservice

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org)
[![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices)
[![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md)
[![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard
originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the
events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open
Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from
within this project's root directory:

#### Actions

##### follow

> Follow an user

##### Action Arguments

| Argument Name       | Type      | Required | Default | Description                               |
| :------------------ | :-------- | :------- | :------ | :---------------------------------------- |
| handle              | `string`  | `false`  | None    | The screen name of the user to follow.    |
| user                | `int`     | `false`  | None    | The ID of the user to follow.             |
| follow              | `boolean` | `false`  | None    | Enable notifications for the target user. |
| CONSUMER_KEY        | `string`  | `true`   | None    | No description provided.                  |
| CONSUMER_SECRET     | `string`  | `true`   | None    | No description provided.                  |
| ACCESS_TOKEN        | `string`  | `true`   | None    | No description provided.                  |
| ACCESS_TOKEN_SECRET | `string`  | `true`   | None    | No description provided.                  |

```shell
oms run follow \
    -a handle='*****' \
    -a user='*****' \
    -a follow='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

##### unfollow

> Unfollow an user

##### Action Arguments

| Argument Name       | Type     | Required | Default | Description                              |
| :------------------ | :------- | :------- | :------ | :--------------------------------------- |
| handle              | `string` | `false`  | None    | The screen name of the user to unfollow. |
| user                | `int`    | `false`  | None    | The ID of the user to unfollow.          |
| CONSUMER_KEY        | `string` | `true`   | None    | No description provided.                 |
| CONSUMER_SECRET     | `string` | `true`   | None    | No description provided.                 |
| ACCESS_TOKEN        | `string` | `true`   | None    | No description provided.                 |
| ACCESS_TOKEN_SECRET | `string` | `true`   | None    | No description provided.                 |

```shell
oms run unfollow \
    -a handle='*****' \
    -a user='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

##### followers

> Returns a cursored collection of user objects for users following the specified user.

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced
change and eventual consistency issues. Results are given in groups of 20 users and multiple “pages” of results can be
navigated through using the `next_cursor` value in subsequent requests.

##### Action Arguments

| Argument Name       | Type      | Required | Default | Description                                                                                                                                |
| :------------------ | :-------- | :------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| handle              | `string`  | `false`  | None    | The screen name of the user for whom to return results.                                                                                    |
| user                | `int`     | `false`  | None    | The ID of the user for whom to return results.                                                                                             |
| cursor              | `int`     | `false`  | None    | Causes the results to be broken into pages. If no cursor is provided, a value of -1 will be assumed, which is the first “page.”            |
| count               | `int`     | `false`  | None    | The number of users to return per page, up to a maximum of 200. Defaults to 20.                                                            |
| skip_status         | `boolean` | `false`  | None    | When set to either true, statuses will not be included in the returned user objects. If set to any other value, statuses will be included. |
| CONSUMER_KEY        | `string`  | `true`   | None    | No description provided.                                                                                                                   |
| CONSUMER_SECRET     | `string`  | `true`   | None    | No description provided.                                                                                                                   |
| ACCESS_TOKEN        | `string`  | `true`   | None    | No description provided.                                                                                                                   |
| ACCESS_TOKEN_SECRET | `string`  | `true`   | None    | No description provided.                                                                                                                   |

```shell
oms run followers \
    -a handle='*****' \
    -a user='*****' \
    -a cursor='*****' \
    -a count='*****' \
    -a skip_status='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

##### retweet

> Retweet a tweet

##### Action Arguments

| Argument Name       | Type     | Required | Default | Description              |
| :------------------ | :------- | :------- | :------ | :----------------------- |
| tweet               | `string` | `true`   | None    | No description provided. |
| CONSUMER_KEY        | `string` | `true`   | None    | No description provided. |
| CONSUMER_SECRET     | `string` | `true`   | None    | No description provided. |
| ACCESS_TOKEN        | `string` | `true`   | None    | No description provided. |
| ACCESS_TOKEN_SECRET | `string` | `true`   | None    | No description provided. |

```shell
oms run retweet \
    -a tweet='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

##### tweet

> Tweet a message

##### Action Arguments

| Argument Name       | Type     | Required | Default | Description              |
| :------------------ | :------- | :------- | :------ | :----------------------- |
| status              | `string` | `true`   | None    | No description provided. |
| CONSUMER_KEY        | `string` | `true`   | None    | No description provided. |
| CONSUMER_SECRET     | `string` | `true`   | None    | No description provided. |
| ACCESS_TOKEN        | `string` | `true`   | None    | No description provided. |
| ACCESS_TOKEN_SECRET | `string` | `true`   | None    | No description provided. |

```shell
oms run tweet \
    -a status='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

##### tweet

> Stream tweets

##### Action Arguments

| Argument Name       | Type     | Required | Default | Description                                                                                                                                    |
| :------------------ | :------- | :------- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| track               | `any`    | `false`  | None    | A single string or list of phrases to track. https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters#track |
| CONSUMER_KEY        | `string` | `true`   | None    | No description provided.                                                                                                                       |
| CONSUMER_SECRET     | `string` | `true`   | None    | No description provided.                                                                                                                       |
| ACCESS_TOKEN        | `string` | `true`   | None    | No description provided.                                                                                                                       |
| ACCESS_TOKEN_SECRET | `string` | `true`   | None    | No description provided.                                                                                                                       |

```shell
oms subscribe tweet \
    -a track='*****' \
    -e CONSUMER_KEY=$CONSUMER_KEY \
    -e CONSUMER_SECRET=$CONSUMER_SECRET \
    -e ACCESS_TOKEN=$ACCESS_TOKEN \
    -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the
Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit twitter on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/twitter)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md).
Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

- [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build
  microservices.
- [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of
  languages.
- [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node,
  Python, Scala, Java, Clojure.
- [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
- [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
