from parser import json_parser
from dotenv import load_dotenv
import os
load_dotenv()

required_fields = {
    "cab_request": ["destination", "price_range", "pickup_location"],
    "gifting": ["budget", "occasion"],
    "travel": ["number_of_members", "destination", "date"],
    "dining": ["number_of_members", "date", "time", "location", "cuisine"],
}

intent_description = {
    "cab_request": "booking a cab",
    "gifting": "buying a gift",
    "travel": "booking a trip",
    "dining": "making a dining reservation",
}

def create_extraction_prompt(intent):
    extraction_prompt = f"""You are an expert at extracting information from user's query.

Given a user's query, extract the key entities from the user's query pertaining to booking a cab.

Required Fields in user's query:
{"\n".join([f"{i+1}. {entity}" for i, entity in enumerate(required_fields[intent])])}

If the user has provided any additional information that is relevant to {intent_description[intent]}, you must extract it as well with appropriate key.

You must respond in below format with appropriate keys.

{{
  "key_entities": {{
    {",\n".join([f"{entity}: value" for entity in required_fields[intent]])}
    # other keys entities found in the query
  }},
}}

Place empty strings/lists temporarily for required values that are not found.
"""
    return extraction_prompt

class Extractor:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, query, intent):
        extraction_prompt = create_extraction_prompt(intent)
        response = self.llm.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=[{"role": "system", "content": extraction_prompt}, {"role": "user", "content": query}],
        )
        res = response.choices[0].message.content
        parsed_res = json_parser(res)

        missing_required_fields = []
        for field in required_fields[intent]:
            if field not in parsed_res['key_entities'].keys():
                missing_required_fields.append(field)
            elif parsed_res['key_entities'][field] == "":
                missing_required_fields.append(field)

        return parsed_res, missing_required_fields
