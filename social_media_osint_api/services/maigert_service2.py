# from maigret import maigret, types
import asyncio
import logging
import os

import maigret
from maigret import MaigretDatabase


async def search_username2(username):
    logger = logging.getLogger('maigret')
    logger.setLevel(logging.ERROR)

    module_path = os.path.dirname(maigret.__file__)
    json_path = os.path.join(module_path, 'resources', 'data.json')
    db = MaigretDatabase().load_from_path(json_path)
    get_top_sites_for_id = lambda x: db.ranked_sites_dict(
        top=500,
        names=["Facebook", "Twitter", "Instagram", "Youtube", "LinkedIn"])

    sites_to_check = get_top_sites_for_id("username")
    return await maigret.search(username, sites_to_check, logger)




