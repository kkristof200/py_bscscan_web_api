# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, List

# Pip
from requests import Response
from noraise import noraise

# Local
from bs4 import BeautifulSoup
from .models import RecentlyAddedToken, Compiler, Token

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: Parser -------------------------------------------------------- #

class Parser:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self
    ):
        return


    # --------------------------------------------------- Public properties -------------------------------------------------- #




    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    @classmethod
    @noraise()
    def parse_recently_added_tokens(
        cls,
        response: Optional[Response]
    ) -> Optional[List[RecentlyAddedToken]]:
        soup = cls.__get_bs(response)

        if not soup:
            return None
        
        return [t for t in
            [
                cls.__parse_recently_added_token(tr)
                for tr in soup.find('tbody').find_all('tr')
            ]
            if t
        ]
    
    @classmethod
    @noraise()
    def parse_token(
        cls,
        address: str,
        response: Optional[Response]
    ) -> Optional[RecentlyAddedToken]:
        soup = cls.__get_bs(response)

        if not soup:
            return None

        holders_text = soup.find('div', id='ContentPlaceHolder1_tr_tokenHolders').find('div', class_='mr-3').text

        return Token(
            address=address,
            holders=int(''.join(filter(str.isdigit, holders_text)) or '0'),
            transfers=int(''.join(filter(str.isdigit, soup.find('div', id='ContentPlaceHolder1_trNoOfTxns').find('span', id='totaltxns').text)) or '0')
        )


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    @staticmethod
    @noraise()
    def __parse_recently_added_token(tr: BeautifulSoup) -> Optional[RecentlyAddedToken]:
        tds = tr.find_all('td')
        compiler_issues_element = tds[3].find('span')
        
        @noraise(print_exc=False, default_return_value=0.0)
        def get_bnb_balance(element) -> float:
            return float(element.text.split(' ')[0])


        return RecentlyAddedToken(
            address=tds[0].find('a')['title'],
            name=tds[1].text,
            compiler=Compiler(
                name=tds[2].text,
                version=tds[3].text,
                issues_message=compiler_issues_element['title'] if compiler_issues_element else None
            ),
            balance_bnb=get_bnb_balance(tds[4]),
            txns=int(tds[5].text),
            verified_date=tds[7].text,
            audited=tds[8].text,
            license=tds[9].text
        )

    @staticmethod
    @noraise()
    def __get_bs(response: Optional[Response]) -> Optional[BeautifulSoup]:
        return BeautifulSoup(response.content, 'lxml')


# -------------------------------------------------------------------------------------------------------------------------------- #