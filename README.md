# summarise-ios-voice-memos

Creates reflection summaries from iOS voice memos using OpenAI Whisper and OpenAI GPT 3.5.

## Getting started

### Installation

1. Add OpenAI API key

```sh
export OPENAI_API_KEY=<key>
```

2. Add M4A recordings from iOS Voice Memos

```sh
# directory must be called "recordings"
mkdir recordings/
```

3. Install dependencies

```sh
python3 -m venv .venv/ && \
source .venv/bin/activate && \
pip install -r requirements.txt
```

### Running the app

Run `main.py` to print voice memo summaries to the console.

```sh
python3 main.py
```
