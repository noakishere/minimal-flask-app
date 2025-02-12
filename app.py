from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None
    
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "developer", "content": "You are a dream interpreter. You are a Jungian Dream Analysis machine and your framework is based on Carl Jung's analytical psychology and his theories of dreams. Imitate Carl Jung and only interpret the dream without anything else. Talk in mystery and some poetic tone."}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.2,
                        #   max_completion_tokens=50
            )
            result = response.choices[0].message.content

            image_prompt = "Make a stylized image based on this dream ${prompt}"

            image_response = openai.OpenAI().images.generate(
                model="dall-e-2",
                prompt=image_prompt,
                size="512x512",
                quality="standard",
                n=1,
            )
            image_url = image_response.data[0].url

        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing