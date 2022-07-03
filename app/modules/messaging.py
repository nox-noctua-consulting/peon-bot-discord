import json
import random
from . import project_path

responses = json.load(open(f"{project_path}/config/documents/quotes.json"))
messages = json.load(open(f"{project_path}/config/documents/messages.json"))

def quote(group="hello"):
    return random.choice(responses[group])

def errorMessage(type="undefined",command="undefined"): # Add error header
    errorString = f"*\'{quote('nok')}\'*\n"
    errorString += f"*{messages['type'][type]}*\n" # Add error type
    errorString += f"```yaml\n{messages['sample'][command]}\n```" # Add help sample
    errorString += f"* \*Optional (required if there are multple servers, on different systems, with the same server name)\n$Optional (if you wish to set an auto-stop)*" # Add help sample
    return errorString