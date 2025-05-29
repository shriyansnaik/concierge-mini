# concierge-mini

I have used the openai API client directly and wrote the entire code using python for better control. I have used Gemini-2.0-flash model for the workflow.

> NOTE: I have used structured outputs API which are currently enabled only by openai and gemini so please use either of those providers. You can make your Gemini API key here for free: https://aistudio.google.com/apikey

To setup the app, start by cloning the repo

```
git clone https://github.com/shriyansnaik/concierge-mini.git
cd concierge-mini
```

First make a python environment
```
python -m venv venv

# source venv/bin/activate (activate for mac/linux)
venv\Scripts\activate.bat (activate for windows)
```

Then install the requirements
```
pip install -r requirements.txt
```

Then create a .env file and add your Gemini key. The file should look like:
```
GEMINI_API_KEY=<gemini-key>
GEMINI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME="gemini-2.0-flash"
```
I have used gemini, but you can use any openai compatible base url.

Finally run the streamlit UI
```
streamlit run app.py
```

A few sample questions and their outputs have been saved in the `sample` folder.  
The same questions are also directly accessible from the left pane of the UI.  

For each intent category, I have set certain required fields:
```
required_fields = {
    "cab_request": ["destination", "price_range", "pickup_location"],
    "gifting": ["budget", "occasion"],
    "travel": ["number_of_members", "destination", "date"],
    "dining": ["number_of_members", "date", "time", "location", "cuisine"],
}
```
