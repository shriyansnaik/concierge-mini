def json_parser(text):
    import re
    import json

    # Find the JSON content in the text
    match = re.search(r'```json\s*\n(.*?)\n```', text, re.DOTALL)
    if match:
        json_content = match.group(1)
        data = json.loads(json_content)
        return data
    else:
        return {}

