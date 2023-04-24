import json
import subprocess
from pathlib import Path

from social_media_osint_api.models import OsintResult


def search_username_and_store(username, sites=None, user_agent=None, tags=None, json_file=None):
    maigret_args = [
        'maigret',
        username,
        '--html', '--pdf'
    ]
    if json_file:
        maigret_args.extend(['--json', json_file])
    if sites:
        maigret_args.extend(['--site', ','.join(sites)])
    if tags:
        maigret_args.extend(['--tags', ','.join(tags)])
    if user_agent:
        maigret_args.extend(['-a', user_agent])
    # osint_data = maigret_main(maigret_args)
    completed_process = subprocess.run(maigret_args, capture_output=True, text=True)
    if completed_process.returncode == 0:
        path = Path(__file__).parent.parent.parent
        file = (path / "reports/report_{}_{}.json".format(username, json_file)).resolve()
        f = open(file)
        osint_data = json.load(f)

    result = OsintResult(username=username, data=osint_data)
    result.save()

    return result
