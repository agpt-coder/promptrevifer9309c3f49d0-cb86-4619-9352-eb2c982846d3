import openai
from pydantic import BaseModel


class RefinePromptResponse(BaseModel):
    """
    This model holds the refined prompt returned from the API after processing with GPT-4.
    """

    refined_prompt: str


def refine_prompt(original_prompt: str) -> RefinePromptResponse:
    """
    Receives a user's prompt and returns a refined version using GPT-4.

    Args:
        original_prompt (str): The original prompt submitted by the user for refinement.

    Returns:
        RefinePromptResponse: This model holds the refined prompt returned from the API after processing with GPT-4.

    This function leverages OpenAI's GPT-4 (text-davinci-003 as of this writing) to refine a user-submitted prompt into a clearer and
    more specific version. It interacts with the OpenAI API using the provided prompt, applying advanced
    prompt engineering techniques. The refined prompt is then wrapped in a RefinePromptResponse object and returned,
    ready for further processing or display to the user.
    """
    openai.api_key = "your_openai_api_key_here"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Refine this prompt to be clearer and more specific. Original: {original_prompt}",
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    refined_prompt = (
        response.choices[0].text.strip() if response.choices else ""
    )  # TODO(autogpt): Cannot access member "choices" for type "Generator[Unknown | list[Unknown] | dict[Unknown, Unknown], None, None]"
    #     Member "choices" is unknown. reportAttributeAccessIssue
    return RefinePromptResponse(refined_prompt=refined_prompt)
