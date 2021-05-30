# Lecture Lab

Lecture lab as a chrome extension, which can be used by medical students to understand lecture videos better.
This app is able to summarize videos, create flashcards according to the lectures content and to answer questions about them.

# Installation
- to be able to use the app, create a .env file inside the /backend/ folder.
  - inside this file add the following line: `API_KEY=sk...` wherer sk... represents your openai key.
- To be able to start the app u need the uvicorn server tools, which can be found on the following website: https://www.uvicorn.org
- start the app by opening a console in your /backend/ folder and type in `uvicorn main:app`. This will start a server at your localhost.
- Add the content from your /frontend/ folder into your chrome extension and you should be able to use the extension

# Remarks
- At the moment the app can only be used on youtube videos with available english subtitles
- the anki export is still causing troubles
