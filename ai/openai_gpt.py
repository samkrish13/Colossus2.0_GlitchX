
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(prompt, model="gpt-3.5-turbo"):
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message["content"]

    except Exception as e:
        print(f"Error in GPT response: {e}")
        return "Sorry, I had trouble generating a response. Please try again."
