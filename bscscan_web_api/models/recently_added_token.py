# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional
from datetime import datetime

# Pip
from jsoncodable import JSONCodable

# Local
from .compiler import Compiler

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------- class: RecentlyAddedToken -------------------------------------------------- #

class RecentlyAddedToken(JSONCodable):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        address: str,
        name: str,
        compiler: Compiler,
        balance_bnb: Optional[float],
        txns: int,
        verified_date: str,
        audited: str,
        license: str
    ):
        self.address = address
        self.name = name
        self.compiler = compiler
        self.balance_bnb = balance_bnb or 0
        self.txns = txns

        self.verified_date = datetime.strptime(verified_date, '%m/%d/%Y')
        self.audited = audited
        self.license = license


        self.token_url = 'https://bscscan.com/token/{}'.format(address)
        self.contract_url = 'https://bscscan.com/address/{}'.format(address)

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    def age_days(self) -> int:
        return (datetime.now() - self.verified_date).days


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #




    # -------------------------------------------------- Private properties -------------------------------------------------- #




    # ---------------------------------------------------- Private methods --------------------------------------------------- #




# -------------------------------------------------------------------------------------------------------------------------------- #