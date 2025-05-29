from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

class FollowUpQuestion(BaseModel):
    follow_up_questions: list[str]

follow_up_question_generator_prompt = """You are an expert conversationalist and asking to the point precise questions.

You are given a user query and a list of missing values. You need to generate a follow up for each of the missing value.

Your language should be casual and the question should be precise and to the point. 

When phrasing the question, use the name of the missing value in the question.

Generate follow ups ONLY for the missing values and nothing else."""

class FollowUpQuestionGenerator:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, query, missing_values):
        prompt = f"User query: {query}\nMissing values: {missing_values}"
        response = self.llm.beta.chat.completions.parse(
            model=os.getenv("MODEL_NAME"),
            messages=[{"role": "system", "content": follow_up_question_generator_prompt}, {"role": "user", "content": prompt}],
            response_format=FollowUpQuestion,
        )
        res = response.choices[0].message.parsed
        return res.follow_up_questions
