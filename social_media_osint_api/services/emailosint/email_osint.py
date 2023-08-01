from holehe.core import *

from social_media_osint_api.services.emailosint.ask import Ask
from social_media_osint_api.services.emailosint.baidu import Baidu
from social_media_osint_api.services.emailosint.bing import Bing
from social_media_osint_api.services.emailosint.breached_directory import BreachedDirectory
from social_media_osint_api.services.emailosint.dogpile import Dogpile
from social_media_osint_api.services.emailosint.emailrep import EmailRepIo
from social_media_osint_api.services.emailosint.google import Google
from social_media_osint_api.services.emailosint.holehe import Holehe
from social_media_osint_api.services.emailosint.leak_lookup import LeakLookUp
from social_media_osint_api.services.emailosint.pgp import PGP
from social_media_osint_api.services.emailosint.yahoo import Yahoo


def search_email(email: str):
    engine_list = [Google(), PGP(), Yahoo(), BreachedDirectory(), EmailRepIo(), LeakLookUp(), Ask(), Baidu(),
                   Bing(), Dogpile(), Holehe()]
    engine_dict = dict(
        (type(x).__name__, trio.run(x.search, email) if type(x).__name__ == 'Holehe' else x.search(email)) for x in
        engine_list)

    # remove empty results
    filtered_dict = {k: v for k, v in engine_dict.items() if v is not None and v != []}

    breached_results_dict = {item['sources'][0].lower(): item for item in list(filtered_dict['BreachedDirectory']['result'])}
    leak_lookup_results_dict = {k: {} for k, v in filtered_dict['LeakLookUp']['message'].items() if v is not None and v == []}

    modified_results = {"basic_email_reputation": filtered_dict['EmailRepIo'],
                        "leaks": {**leak_lookup_results_dict, ** {key: val  for key, val in breached_results_dict.items()}},
                        "social_media_registrations": [account for account in filtered_dict['Holehe'] if
                                                       account['exists']]
                        }
    # result = EmailOsintResult(email=email, results=engine_dict)
    # result.save()
    return {"email": email, "results": modified_results}
