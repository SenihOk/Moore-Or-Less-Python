import os

class Codes:
    def __init__(self):
        """
        initializes the variables for the twitter API tokens
        args: none
        returns: none
        """
        self.api_key  = ""
        self.api_key_scrt  = ""
        self.bearer_tkn  = ""
        self.access_tkn  = ""
        self.access_tkn_scrt = ""
        
    def assignValues(self):
        """
        assigns tokens to the token variables
        args: none
        return: none
        """
        self.api_key = (os.environ['API_KEY'])
        self.api_key_scrt = (os.environ['API_KEY_SECRET'])
        self.bearer_tkn = (os.environ['BEARER_TOKEN'])
        self.access_tkn = (os.environ['ACCESS_TOKEN'])
        self.access_tkn_scrt = (os.environ['ACCESS_TOKEN_SECRET'])
        return {"api_key": self.api_key, "api_key_scrt": self.api_key_scrt, "access_tkn": self.access_tkn, "access_tkn_scrt" : self.access_tkn_scrt}
