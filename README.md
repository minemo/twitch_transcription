 # Twitch Transcriber

## FAQ:

### What is this?
A relatively basic setup for transcribing Livestreams on Twitch using [OpenAI's Whisper](https://github.com/openai/whisper) and [Streamlink](https://github.com/streamlink/streamlink).

### How do use it?
1. Install ffmpeg with `sudo apt install ffmpeg`, `choco install ffmpeg`...
2. Install Streamlink with `pip install streamlink`
3. Create a virtual environment
4. ```pip install -r requirements.txt```
5. ````python main.py <twitch channel>````

### Why?
Twitch doesn't have a built-in transcription feature, and I wanted to try out Whisper, so here we are. <br/>
Feel free to open a Push/Pull Request if you want to add something.

### How does it work?
I'm sure you can figure it out by reading the code for now. <br/>
_I'll add a more detailed explanation later, if this turns out to be useful._

