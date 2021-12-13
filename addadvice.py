import json
import requests
import django

class Advice:
    def __init__(self, text):
        """
        initializes the Advice class with the API url and the weather report
        args: self, text(str)
        returns: none
        """
        self.url = 'https://api.adviceslip.com'
        self.weather_report = text
    def addAdvice(self):
        """
        merges the advice from the api with the text argument
        args: self
        returnsL result(str)
        """
        try:
            advice = requests.get(f'{self.url}/advice')
            # print(f'{self.url}/advice')
            advice = advice.text
            # print(advice)
            advice = json.loads(advice)
            advice = advice['slip']['advice']
            result = f"Hello, \n \n{self.weather_report} \n \nAnd remember, \n\n{advice} "
            # print(result)
            return result
        except:
            return ('error, try again later')

