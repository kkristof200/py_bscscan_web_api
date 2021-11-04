# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional
from datetime import datetime

# Pip
from jsoncodable import JSONCodable

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: Token --------------------------------------------------------- #

class Token(JSONCodable):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        address: str,
        holders: int,
        transfers: int
    ):
        self.address = address
        self.holders = holders
        self.transfers = transfers

        self.url_holders  = f'https://bscscan.com/token/{address}#balances'
        self.url_token    = f'https://bscscan.com/token/{address}'
        self.url_contract = f'https://bscscan.com/address/{address}'
        self.url_src_code = f'https://bscscan.com/address/{address}#code'


# -------------------------------------------------------------------------------------------------------------------------------- #