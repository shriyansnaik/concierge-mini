from parser import json_parser

required_fields = {
    "cab request": ["destination", "price_range", "pickup_location"],
    "gifting": ["budget", "occasion"],
    "travel": ["number_of_members", "destination", "date"],
    "dining": ["number_of_members", "date", "time", "location", "cuisine"],
}

intent_description = {
    "cab request": "booking a cab",
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

If the user has not provided required fields, you must ask follow up questions to get the values of the required fields. 
If the provided information for a required field is ambiguous, you must ask follow up questions to get the specific information. For example, for a required field of date, the user might have said coming summer. In this case, you must ask for the specific date.
When asking the follow up questions, you must use the required fields name in your question.

You must not ask follow up questions if the required fields are provided.

You must respond in below format with appropriate keys.

{{
  "key_entities": {{
    {",\n".join([f"{entity}: value" for entity in required_fields[intent]])}
    "any_other_keys": value
  }},
  "follow_up_questions": list  # only include follow up questions for required fields
}}

Place empty strings/lists temporarily for values not found.

In case the key entities have all the required fields, you must return empty list in follow_up_questions
    """
    return extraction_prompt

class Extractor:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, query, intent):
        extraction_prompt = create_extraction_prompt(intent)
        response = self.llm.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "system", "content": extraction_prompt}, {"role": "user", "content": query}],
        )
        res = response.choices[0].message.content
        return json_parser(res)
