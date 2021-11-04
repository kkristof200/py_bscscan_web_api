# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Dict, List

# Pip
from ksimpleapi import Api

# Local
from ._parser import Parser
from .models import RecentlyAddedToken, Token

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: Bscscan -------------------------------------------------------- #

class BSCScan(Api):

    # ------------------------------------------------------- Overrides ------------------------------------------------------ #

    @classmethod
    def extra_headers(cls) -> Optional[Dict[str, any]]:
        return {
            'Host': 'bscscan.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def get_token(
        self,
        address: str
    ) -> Optional[Token]:
        return Parser.parse_token(
            self._get(f'https://bscscan.com/token/{address}')
        )

    def get_recently_added_tokens(self) -> List[RecentlyAddedToken]:
        tokens = []

        for i in range(5):
            _tokens = Parser.parse_recently_added_tokens(
                self._get('https://bscscan.com/contractsVerified/{}/ps=100'.format(i+1))
            )

            if _tokens:
                tokens.extend(_tokens)

        return tokens


    # -------------------------------------------------- Private properties -------------------------------------------------- #

    @property
    def _parser(self) -> Parser:
        if '__parser' in dir(self):
            self.__parser = Parser()

        return self.__parser


# -------------------------------------------------------------------------------------------------------------------------------- #