import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from config import MAX_ITERATIONS, SYSTEM_PROMPT


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    i = 0
    while i < MAX_ITERATIONS:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=SYSTEM_PROMPT
                ),
            )

            if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print(
                    "Response tokens:", response.usage_metadata.candidates_token_count
                )

            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)

            if not response.function_calls:
                print(response.text)
                break

            function_responses = []
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose)
                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")
                if verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )
                function_responses.append(function_call_result.parts[0])

            function_messages = types.Content(role="user", parts=(function_responses))
            messages.append(function_messages)

            if not function_responses:
                raise Exception("no function responses generated, exiting.")
        except Exception as e:
            return f"Error: {e}"
        i += 1


if __name__ == "__main__":
    main()
