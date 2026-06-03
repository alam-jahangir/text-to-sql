from google import genai
from google.genai import types

import constant
from config import Config

class GoogleGenai(Config):

    def __init__(self) -> None:
        # Call the parent class __init__ method
        super().__init__()
        self._client = None

    def get_client(self) -> genai.Client:

        if self._client is None:
            self._client = genai.Client(api_key=self.get_config_by_name("GEMINI_API_KEY"))

        return self._client

    def generate_sql(self, user_question: str) -> str:

        response = self.get_client().models.generate_content(
            model='gemini-2.5-flash',
            contents=constant.SYSTEM_PROMPT.format(user_question=user_question),
            config=types.GenerateContentConfig(
                temperature=0.0  # 0.0 guarantees deterministic, highly precise query logic
            )
        )

        return response.text.strip()
