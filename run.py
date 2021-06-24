from pprint import pprint as pp
from ranking_api.db import renew_tables, get_session
from ranking_api.model import *

renew_tables()

session = get_session()

pp(session.query(Tournament).all())
