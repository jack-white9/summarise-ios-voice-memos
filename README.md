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

## Example output

The following reflection was generated from only ~60 seconds of conversational audio input from a pre-service teacher.

```md
**Section 1: What happened?**

The pre-service teacher talked about the classroom management techniques used by their colleague, <redacted>. <redacted> employed strategies such as the "Okay in five, eyes on me, four, three, two, one" technique to grab the students' attention and bring about silence in the classroom. Additionally, <redacted> utilized call-and-response activities like the "knock knock" joke to engage the students in a fun and interactive way. The pre-service teacher also mentioned how <redacted> implemented a tactic of waiting in silence, using phrases like "I'm waiting," to encourage the students to settle down and focus.

**Section 2: So what?**

Effective classroom management is crucial for creating a conducive learning environment where students can engage and succeed academically. <redacted>'s use of various techniques shows her effort in maintaining a structured and disciplined classroom atmosphere. By employing strategies like countdowns, call-and-response activities, and silent waiting periods, <redacted> not only manages student behavior but also fosters student participation and cooperation. These techniques help in capturing students' attention, maintaining a sense of order, and promoting a positive classroom culture.

**Section 3: Now what?**

Reflecting on <redacted>'s classroom management techniques can inspire the pre-service teacher to explore various strategies and find what works best for their own classroom. They could experiment with countdowns, call-and-response activities, and silent waiting as ways to manage student behavior and create a focused learning environment. It's essential for the pre-service teacher to observe different approaches, adapt them to suit their teaching style, and continuously refine their classroom management skills to effectively engage students and enhance their learning experience. Moreover, they could seek further professional development or guidance on classroom management to deepen their understanding and proficiency in this critical aspect of teaching.
```
