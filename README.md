## Installation

- Clone the project

  ```
  git clone https://github.com/nicolas-landel/pick-your-date.git
  ```

- Pull the project:

  ```console
  git pull git@github.com:nicolas-landel/pick-your-date.git
  ```

- Create `.env` from `.env.example`:

  ```console
  cp .env.example .env
  ```

- Build Docker image and start it:

  ```console
  docker-compose up --build
  ```

- Migrations

  ```
  docker-compose exec questionnaire-grpc ./manage.py migrate
  ```