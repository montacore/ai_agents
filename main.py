import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
def generate_content(client, messages):
    res = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    return res
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # now you can access args.user_prompt

    load_dotenv()
    try: 
        api_key = os.environ.get("OPENROUTER_API_KEY")
    except:
        if api_key == None:
            raise RuntimeError("OPENROUTER_API_KEY environment variable was not found...")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages = [
        {"role": "user", "content": args.user_prompt},
    ]
    response = generate_content(client, messages)

    if response.usage != None:
        prompt_tokens = response.usage.prompt_tokens
        response_tokens = response.usage.completion_tokens 
    else:
        raise RuntimeError("Potentially failed API request, please try again")
    # print(response)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
