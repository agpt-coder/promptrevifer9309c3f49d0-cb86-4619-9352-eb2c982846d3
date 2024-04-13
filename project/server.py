import logging
from contextlib import asynccontextmanager

import project.create_user_service
import project.refine_prompt_service
import project.user_login_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="promptrevifer930",
    lifespan=lifespan,
    description="To create a single API endpoint for refining LLM prompts using GPT-4, we'll leverage the discussed tech stack: Python as the programming language, FastAPI for the API framework, PostgreSQL as the database, and Prisma as the ORM. This endpoint will accept a string as input, representing the LLM prompt provided by the user. It will then interact with GPT-4 through the OpenAI Python package to refine this prompt, employing advanced prompt engineering techniques based on best practices for prompt refinement. The refined prompt, generated as a result of GPT-4's processing, will be returned to the user.\n\nImplementation steps include setting up a FastAPI project, integrating the OpenAI package for Python, and creating an endpoint to receive the user's prompt and return the refined version. The system message 'You are a prompt refiner. Use advanced prompt engineering techniques to refine the user's prompt.' will guide the AI's interaction with the user's prompt to ensure the outcome adheres to the goals of clarity, specificity, and enhanced potential effectiveness of the prompt in eliciting desired responses from GPT-4.",
)


@app.post("/user/login", response_model=project.user_login_service.UserLoginResponse)
async def api_post_user_login(
    email: str, password: str
) -> project.user_login_service.UserLoginResponse | Response:
    """
    Endpoint for user authentication.
    """
    try:
        res = await project.user_login_service.user_login(email, password)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post(
    "/user/register", response_model=project.create_user_service.CreateUserResponse
)
async def api_post_create_user(
    email: str, password: str, username: str
) -> project.create_user_service.CreateUserResponse | Response:
    """
    Endpoint for user registration.
    """
    try:
        res = await project.create_user_service.create_user(email, password, username)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post(
    "/prompts/refine", response_model=project.refine_prompt_service.RefinePromptResponse
)
async def api_post_refine_prompt(
    original_prompt: str,
) -> project.refine_prompt_service.RefinePromptResponse | Response:
    """
    Receives a user's prompt and returns a refined version using GPT-4.
    """
    try:
        res = project.refine_prompt_service.refine_prompt(original_prompt)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
