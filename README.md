# QuestionHub

Platform where people can get request data using APIs.

## Badges

[![Build Status](https://travis-ci.org/JamesnThuo/QuestionHub.svg?branch=test-travis)](https://travis-ci.org/JamesnThuo/QuestionHub) | [![Coverage Status](https://coveralls.io/repos/github/JamesnThuo/QuestionHub/badge.svg?branch=travis)](https://coveralls.io/github/JamesnThuo/QuestionHub?branch=travis) | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Required Features
    - Users can create an account and log in.
    - Users can post questions.
    - Users can delete the questions they post
    - Users can post answers
    - Users can view the datasets.
    - Users can download a dataset.
    - Users can upvote or downvote an answer.
    - Users can comment on an answer.
    - Users can fetch all questions he/she has ever asked on the platform
    - Users can search for questions on the platform
    - Users can view questions with the most answers.


### Endpoints

#### Users Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/signup` | Add a user
GET | `/api/v1/auth/users` | Lists all users
GET | `/api/v1/auth/users/{user_id}` | Retrieve a user
POST | `/api/v1/auth/login` | Login a user

#### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions
GET | `/api/v1/questions/?q={search_string}` | Search a questions
GET | `/api/v1/questions/{question_id}` | Retrieve a question
PUT | `/api/v1/questions/{question_id}` | Edit a question of a logged in user
DELETE | `/api/v1/questions/{question_id}` | Delete a request of a logged in user

#### Answers Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/{question_id}/answers` | Add an answer
GET | `/api/v1/questions/answers` | Lists all answers
GET | `/api/v1/questions/answers/{answerID}` | Retrieve an answer
PUT | `/api/v1/questions/{question_id}/answer/{answerID}` | Edit an answer
DELETE | `/api/v1/questions/{question_id}/answer/{answerID}` | Delete an answer
POST | `/api/v1/questions/answers/vote/{answer_id}` | Upvote/DownVote an answer
POST | `/api/v1/questions/answers/comment/{answer_id}` | Comment on an answer

## Author
James Thuo
