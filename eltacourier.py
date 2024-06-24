import requests
import json
import shared

class EltaCourier:
    def __init__(self, getaway :str="https://www.elta-courier.gr"):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        self.config = { 
            "getaway": getaway if getaway and isinstance(getaway, str) else None,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
            }  
        }
        if hasattr(self, "rss") and self.rss and isinstance(self.rss, requests.Session) and \
        hasattr(self, "config") and self.config and isinstance(self.config, dict) and \
        "headers" in self.config and self.config["headers"] and isinstance(self.config["headers"], dict):
            self.rss.headers.update(self.config["headers"])
    def track(self, number :(list,str)=None):
        if hasattr(self, "config") and self.config and isinstance(self.config, dict) and \
        "getaway" in self.config and self.config["getaway"] and isinstance(self.config["getaway"], str) and \
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
            data = json.loads(
                s=self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                ).content
            )
            return data["result"] if "result" in data and data["result"] else None