import base64
import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        json_string = json.dumps(strs)
        encoded_identifier = base64.b64encode(json_string.encode()).decode()
        return encoded_identifier

    def decode(self, s: str) -> List[str]:
        decoded_json = base64.b64decode(s).decode()
        restored_list = json.loads(decoded_json)
        return restored_list
