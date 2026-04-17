from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

## loading the enveroment veribles
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

## Initializing a client

Client = genai.Client(api_key=api_key)

def note_generator(images) :
    pil_images = [Image.open(img) for img in images]
    prompt = """
    Summarize the pictures in note format at max 100 words,
      make sure to add neccessary markdwon to differentiate the sections 
    """

    response = Client.models.generate_content(
    model= "gemini-3-flash-preview",
    contents=[pil_images,prompt]
    )

    return response.text

def quiz_generator(images,difficulty) :
    pil_images = [Image.open(img) for img in images]
    prompt = f"""
  Generate 3 Quizzes based on {difficulty}. 
  Must be make sure to add markdown for differantiate optios or quiz.
  Also add the answer sheet in the last.
    """

    response = Client.models.generate_content(
    model= "gemini-3-flash-preview",
    contents=[pil_images,prompt]
    )

    return response.text