# Importing required module
import json
import os
import sys
from argparse import Namespace
from pathlib import Path

sherlock_path = 'C:/Users/adds0/Git/sherlock/sherlock'
# Include this line if your script is not in the sherlock folder
sys.path.insert(0, sherlock_path)

import sherlock
import sites
import notify


def main():
    username = "harismahmood"
    args = Namespace()
    args.username = username
    args.site = None
    args.json = True
    args.csv = False
    args.site_list = None
    args.proxy = None
    args.timeout = None
    args.tor = False
    args.unique_tor = False
    args.print_found = False
    args.print_not_found = False
    args.print_unknown = False
    args.verbose = False
    args.rank = False
    args.folderoutput = None
    args.trace = False
    args.fancy = False
    args.no_color = False
    args.proxy_list = None
    args.proxy_file_type = None
    args.list_all = False
    args.update = False
    args.exclude = None

    data_folder = os.path.join(Path(sherlock_path, "resources"), "data.json")

    sites_info = sites.SitesInformation(data_folder)
    site_data_all = {site.name: site.information for site in sites_info}

    query_notify = notify.QueryNotifyPrint()
    results = sherlock.sherlock(username, site_data_all, query_notify, False)
    results = dict(filter(lambda elem: elem[1]['http_status'] == 200, results.items()))

    for site_name, site_data in results.items():
        site_data['username'] = site_data['status'].username
        site_data['site_name'] = site_data['status'].site_name
        site_data['status'] = site_data['status'].status.value

    # maigret.main()
    results_json = json.dumps(results)
    for site_name, site_data in results_json.items():
        if site_data['exists'] == "yes":
            print(f"{username} found on {site_name}: {site_data['url_user']}")
        elif site_data['exists'] == "no":
            print(f"{username} not found on {site_name}")
        else:
            print(f"Error checking {site_name}")


if __name__ == "__main__":
    main()
