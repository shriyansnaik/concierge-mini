from duckduckgo_search import DDGS
from pydantic import BaseModel

search_query_generator_prompt = """You are an expert at web search. Given a user query, 
you need to generate a search query that will give the most relevant results to find solution 
for user's query. The search query should be a single concise sentence. This search query will 
be entered into a search engine so structure it in a search query way.

For example:
User query: I want to buy an iPhone 15 Pro Max for my friend's birthday.
Search query: buy iPhone 15 Pro Max 

User Query: Need flight from Delhi to Mumbai on 1st June because I need to attend my sister's wedding.
Search query: flights from Delhi to Mumbai on 1st June

User Query: I want how to know how to make a newyork cheesecake.
Search query: newyork cheesecake recipe

You MUST respond with a single search query and no additional text.
"""


class Internet:
    def __init__(self, llm):
        self.llm = llm

    def generate_search_query(self, query):
        response = self.llm.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "system", "content": search_query_generator_prompt}, {"role": "user", "content": query}],
        )
        return response.choices[0].message.content

    def __call__(self, query):
        search_query = self.generate_search_query(query)
        results = DDGS().text(search_query, max_results=5)
        return results
