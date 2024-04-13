from typing import Optional

import prisma
import prisma.models
from pydantic import BaseModel


class UserLoginResponse(BaseModel):
    """
    Model for the response returned after a user login attempt. This will include a success state and a session token if the authentication was successful.
    """

    success: bool
    token: str
    message: Optional[str] = None


async def user_login(email: str, password: str) -> UserLoginResponse:
    """
    Endpoint for user authentication.

    Args:
        email (str): The email address of the user trying to log in. It will be used to locate the user in the database.
        password (str): The password of the user trying to log in. It will be used along with the email to authenticate the user.

    Returns:
        UserLoginResponse: Model for the response returned after a user login attempt. This will include a success state and a session token if the authentication was successful.
    """
    user = await prisma.models.User.prisma().find_unique(where={"email": email})
    if user is None:
        return UserLoginResponse(
            success=False, token="", message="User does not exist."
        )
    if password == user.password:
        token = "secure_generated_token_for_demo_purpose"
        return UserLoginResponse(success=True, token=token, message="Login successful.")
    else:
        return UserLoginResponse(success=False, token="", message="Incorrect password.")
