# Jungian Dream Interpreter Web App

## Overview

This project is a Flask-based web application that interprets dreams using Carl Jung's analytical psychology. The app uses OpenAI's GPT-4 model to provide a dream analysis based on Jungian ideas. It also uses DALL-E-2 to generate a stylized image that reflects the user's dream description. The aim is to offer both a textual and visual representation of the dream using a Jungian framework.

## Implementation Details

The application is built with Flask and uses two OpenAI models. When a user submits a dream description, the app performs the following steps:

1. **Input Handling**: The dream description is received from a web form.
2. **Jungian Dream Analysis**: A prompt is created to instruct GPT-4 to act as a Jungian dream interpreter. The prompt directs the model to analyze the dream using themes like archetypes and symbolism, as seen in Jung's work.
3. **Text Generation**: GPT-4 processes the prompt and returns a dream interpretation in a style that mimics Jung.
4. **Image Generation**: The app also creates a prompt for DALL-E-2 based on the dream description. The image generated aims to visually represent the key elements of the dream.
5. **Rendering Results**: The text and image are then displayed on the webpage for the user.

The OpenAI API key is stored in an environment file (`.env`) and loaded securely using the `dotenv` package. The application is hosted on Render, which ensures it is accessible and runs smoothly in a production environment.

## User Guide

1. **Access the App**: Open your web browser and navigate to the app's URL on Render.
2. **Submit a Dream**: Enter your dream description in the provided text field.
3. **Start Analysis**: Click the submit button to initiate the dream interpretation and image generation.
4. **View Results**: The page will display a Jungian interpretation of your dream along with a generated image.
5. **Error Handling**: If an error occurs (e.g., issues with the API), an error message will be shown on the screen.

## Hosting on your own machine

1. **Clone this repository**
2. **.env**: Create .env file and put your OPENAI key
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. **Run app.py**: Go to the repository's directory and run:
   ```
   python app.py
   ```
4. **Go to browser**: localhost/5000

## Reflection and Future Improvements

This project provided insight into using AI for psychological analysis. Creating a prompt that follows Jungian ideas required careful thought to maintain a clear and focused interpretation of dreams. The project shows that AI can be a useful tool to connect abstract psychological theories with practical applications.

Future improvements include:

- Refining the prompt to produce more detailed and accurate interpretations.
- Adding options for users to save their interpretations and images.
- Enhancing error handling to provide more useful feedback when issues occur.
- Experimenting with different models or settings to improve the variety and depth of the analyses.
