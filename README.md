---
date: 2024-04-13T08:38:38.405080
author: AutoGPT <info@agpt.co>
---

# promptrevifer930

To create a single API endpoint for refining LLM prompts using GPT-4, we'll leverage the discussed tech stack: Python as the programming language, FastAPI for the API framework, PostgreSQL as the database, and Prisma as the ORM. This endpoint will accept a string as input, representing the LLM prompt provided by the user. It will then interact with GPT-4 through the OpenAI Python package to refine this prompt, employing advanced prompt engineering techniques based on best practices for prompt refinement. The refined prompt, generated as a result of GPT-4's processing, will be returned to the user.

Implementation steps include setting up a FastAPI project, integrating the OpenAI package for Python, and creating an endpoint to receive the user's prompt and return the refined version. The system message 'You are a prompt refiner. Use advanced prompt engineering techniques to refine the user's prompt.' will guide the AI's interaction with the user's prompt to ensure the outcome adheres to the goals of clarity, specificity, and enhanced potential effectiveness of the prompt in eliciting desired responses from GPT-4.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'promptrevifer930'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
