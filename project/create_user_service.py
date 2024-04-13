import bcrypt
import prisma
import prisma.models
from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    """
    Response model indicating the result of the user registration operation.
    """

    success: bool
    user_id: str
    message: str


async def create_user(email: str, password: str, username: str) -> CreateUserResponse:
    """
    Endpoint for user registration.

    This function registers a new user in the system by creating a new prisma.models.User record in the database.
    The function hashes the user's password for secure storage and verifies that the email address provided
    has not already been used to register an account.

    Args:
    email (str): prisma.models.User's email address for account registration.
    password (str): prisma.models.User's password for account security. This will be hashed and not stored in plain text.
    username (str): prisma.models.User's chosen username for their profile.

    Returns:
    CreateUserResponse: Response model indicating the result of the user registration operation.
    """
    existing_user = await prisma.models.User.prisma().find_unique(
        where={"email": email}
    )
    if existing_user is not None:
        return CreateUserResponse(
            success=False, user_id="", message="Email already in use."
        )
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    try:
        created_user = await prisma.models.User.prisma().create(
            data={"email": email, "password": hashed_password, "username": username}
        )
        return CreateUserResponse(
            success=True,
            user_id=created_user.id,
            message="prisma.models.User created successfully.",
        )
    except Exception as e:
        return CreateUserResponse(
            success=False, user_id="", message=f"Failed to create user: {str(e)}"
        )
