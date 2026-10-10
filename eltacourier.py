import requests
import json
import shared

class EltaCourier:
    def __init__(self, getaway :str="https://www.elta-courier.gr"):
        self.rss = requests.Session()
        self.config = { 
            "getaway": getaway if getaway and isinstance(getaway, str) else None,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
            }  
        }
        self.rss.headers.update(self.config["headers"])
    def close(self):
        if self.rss != None:
            self.rss.close()
    def __enter__(self):
        return self
    def __exit__(**args):
        self.close()
        return True
    @property
    def validate(self):
        return hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        self.config.get("headers", None) != None and isinstance(self.config.get("headers", None), str)
    def request(self, config :dict=None):
        if data == None or isinstance(data, dict) == False:
            return
        return self.rss.request(
            **config
        )
    def requestJson(self, config :dict=None):
        if config == None or isinstance(config, dict) == False:
            return
        req = self.request(
            config=config
        )
        if req.headers.get("Content-Type", None) == None or isinstance(req.headers.get("Content-Type", None), str) == False or req.headers.get("Content-Type") != "applicaton/json":
            return
        return json.loads(
            s=req.content
        )
    def track(self, number :(list,str)=None):
        if self.validate and \
        number and (isinstance(number, str) or isinstance(number, list) and len(number) > 0):
            if isinstance(number, list):
                number = "\n".join(number)
            config = {
                "method": "post",
                "url": f'{self.config["getaway"]}/track.php',
                "data": {
                    "number": number
                }
            }
            data = self.requestJson(
                config=config
            )
            if data == None or isinstance(data, dict) == False:
                return
            return data.get("result", None)