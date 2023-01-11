import subprocess
from io import BytesIO
import threading
import whisper
import time
import argparse


def pipe_stream_to_bytes(username: str, whispermodel: whisper.Whisper, text):
    """A function that streams a Twitch stream to a BytesIO object."""
    # Create a subprocess that pipes the stream to ffmpeg
    process = subprocess.Popen(
        f"streamlink --loglevel none --twitch-low-latency --twitch-disable-ad twitch.tv/{username} 360p -o - ",
        stdout=subprocess.PIPE)
    # Read the stream from the subprocess
    rectime = 15  # seconds
    sample_rate = 48000
    print("Skipping ads, may take a few seconds...")
    for b in iter(lambda: process.stdout.read(rectime * sample_rate), b''):
        audio = BytesIO(b)
        # save to temp file
        with open("temp.mp4", "wb") as f:
            f.write(audio.getvalue())
        # load temp file
        temp = whispermodel.transcribe("temp.mp4")
        if temp['text'] != "":
            text.append(temp['text'])


def log_text(alltext, n):
    # each n seconds, print the text
    while True:
        time.sleep(n)
        if len(alltext) > 0:
            print(alltext[-1])
            alltext.clear()


def main(argv):
    uname = argv.username
    print("Loading model...")
    model = whisper.load_model("base", 'cuda', in_memory=True)
    print("Done.")
    # Start the stream in a thread
    transcribed = []
    interval = 5
    print("Starting transcribing and streaming threads...")
    transcriber = threading.Thread(target=pipe_stream_to_bytes, args=(uname, model, transcribed))
    logger = threading.Thread(target=log_text, args=(transcribed, interval))
    transcriber.start()
    logger.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transcribe a Twitch stream semi-live.')
    parser.add_argument('--username', type=str, default='gamesdonequick', help='Twitch channel to transcribe')
    args = parser.parse_args()
    main(args)
