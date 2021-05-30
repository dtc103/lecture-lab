"""
pip imports:
fastapi
srt
python_dotenv
openai
uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pytube import YouTube
import srt
from datetime import timedelta
from dotenv import load_dotenv
import os
import openai
import re
import json

def openai_login():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    openai.organization = "org-0J10zZn9lypKaSBUA7vnDW6D"
    openai.api_key = API_KEY

openai_login()

#cache layout = {video_id: captions}
cached_captions = {}

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#####################################################################

@app.get("/")
async def root():
    return {"message": "msg"}

@app.get("/summarize")
async def summarize(video_id: str = ""):
    captions = get_caption_datastructure(video_id)
    if captions is None:
        print("Captions are None")

        #redirect to error page or something
        return ""

    print("Captions are not None")


    text = get_full_caption_text(captions)
    print(text)

    #prevent too long caption text
    if len(text.split()) > 750:
        return ""

    prompt = create_summarize_prompt(text)

    summary = query_gpt3(prompt=prompt)

    return {"message": summary}

    

@app.get("/flashcards")
async def flashcards(video_id: str = ""):
    captions = get_caption_datastructure(video_id)
    if captions is None:
        return ""
    
    text = get_full_caption_text(captions)

    if len(text.split()) > 750:
        return ""

    flashcard_prompt = create_flashcard_prompt(text)

    answer = query_gpt3(prompt=flashcard_prompt)

    fin_answer = parse_flashcard_answer(answer)

    return {"message": fin_answer}


@app.get("/questions")
async def questions(video_id: str = "", question: str = ""):
    captions = get_caption_datastructure(video_id)
    
    if captions is None:
        return ""
    
    text = get_full_caption_text(captions)

    #prevent too long caption text
    if len(text.split()) > 750:
        return ""

    question_prompt = create_question_prompt(text, question)

    answer = query_gpt3(prompt=question_prompt)

    return {"message": answer}

#####################################################################

def in_cache(video_id: str):
    if video_id in cached_captions:
        return True
    else:
        return False

#add english captions to the cache
def add_en_to_cache(video_id: str):
    source = YouTube(f'https://www.youtube.com/watch?v={video_id}')

    if 'en' in source.captions:
        en_caption = source.captions['en']
        if en_caption is not None:
            cached_captions[video_id] = list(srt.parse(en_caption.generate_srt_captions()))
            return True

    if 'a.en' in source.captions:
        auto_en_caption = source.captions['a.en']
        print(auto_en_caption)
        if auto_en_caption is not None:
            cached_captions[video_id] = list(srt.parse(auto_en_caption.generate_srt_captions()))
            return True

    return False

def get_caption_datastructure(video_id: str):
    if in_cache(video_id):
        return cached_captions[video_id]
    else:
        if add_en_to_cache(video_id):
            print(video_id, "was successfully added to the cache")
            return cached_captions[video_id]
        else:
            return None

def get_full_caption_text(captions):
    full_text = ""
    for sub in captions:
        full_text += f"{sub.content} "  
    return full_text

def create_summarize_prompt(text):
    prompt = "Generate a five sentence summary of the following transcript of a video to help understand its content.\n\n---"

    prompt += text
    prompt += "\n---\n"
    prompt += "Summary (five sentences):"

    return prompt

def create_question_prompt(text, question):
    prompt = "Answer questions about the following text in one sentence.\n---\n"
    prompt += text
    prompt += "\n---\n"
    prompt += "Question:"
    prompt += question
    prompt += "\nAnswer:"
    
    return prompt

def create_flashcard_prompt(text):
    prompt = "Generate flashcards (question and answer) about the following transcript of a medical video to help remember its contents.\n---\n"
    prompt += text
    prompt += "\n---\n"
    prompt += "Flashcard 1) Question:"

    return prompt

def parse_flashcard_answer(flashcard_answer):
    flashcards = []

    for match in re.findall(r"(.*question:)?(.+\?\s*)\n?answer:(.*)\n?", flashcard_answer, re.IGNORECASE | re.MULTILINE):
        flashcard = {}
        flashcard["question"] = str(match[1].rstrip().lstrip())
        flashcard["answer"] = str(match[2].rstrip().lstrip())

        flashcards.append(flashcard)

    json_string = json.dumps(flashcards)

    return json_string

def query_gpt3(engine="davinci-instruct-beta", prompt=None):
    completion = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=250, temperature=0.35, top_p=1, frequency_penalty=0.1)
    print(completion)
    return completion.choices[0].text

def get_all_openai_engines():
    print(openai.Engines.list())


"""
source = YouTube(f'https://www.youtube.com/watch?v=NhZJjQ9f17E')
auto_en_caption = source.captions['a.en']
parsed = srt.parse(auto_en_caption.generate_srt_captions())

print(auto_en_caption)
"""