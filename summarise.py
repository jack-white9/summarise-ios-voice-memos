from openai import OpenAI
from dotenv import load_dotenv
import os


class AI:
    def __init__(self):
        load_dotenv()
        self.openai_client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def transcribe(self, audio_path):
        audio_file = open(audio_path, "rb")
        response = self.openai_client.audio.transcriptions.create(
            model="whisper-1", file=audio_file
        )
        return response.text

    def summarise(self, transcript):
        prompt = """
            You're tasked with creating a meaningful reflection by summarizing the following voice transcription from an Australian pre-service teacher. Remember to structure your response into three separate sections:
            - **Section 1: "What happened?"**
            - **Section 2: "So what?"**
            - **Section 3: "Now what?"**
            Ensure your reflection aligns with the Victorian education domain.
        """

        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": transcript},
            ],
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    ai = AI()
    transcript = ai.transcribe("voice_memo.m4a")
    summary = ai.summarise(transcript)
    print(summary)
