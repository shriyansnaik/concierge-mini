from pydantic import BaseModel
from enum import Enum

intent_classifier_prompt = """You are a concierge at a seven star hotel. Your goal is to 
identify what the user wants. Since the hotel is big and there a lot of customers, you can 
help the user with only specific queries. 

The queries that are under your responsibility are as follows:
1. travel
2. gifting
3. dining
4. cab_request

After identifying the intent, you also need to give a confidence score between 0 and 1 of how 
sure you are about the intent you have identified.

If the user's query is not related to any of the above intents, you must categorize it as other."""


class Intent(str, Enum):
    travel = "travel"
    gifting = "gifting"
    dining = "dining"
    cab_request = "cab_request"
    other = "other"

class IntentClassifierResponse(BaseModel):
    intent: Intent
    intent_confidence: float

class IntentClassifier:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, query):
        response = self.llm.beta.chat.completions.parse(
            model="gemini-2.0-flash",
            messages=[{"role": "system", "content": intent_classifier_prompt}, {"role": "user", "content": query}],
            response_format=IntentClassifierResponse,
        )
        res = response.choices[0].message.parsed
        return {
            "intent": res.intent.value,
            "intent_confidence": res.intent_confidence,
        }

