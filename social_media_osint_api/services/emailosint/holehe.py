import argparse

from holehe.modules.transport.blablacar import *


# Holehe checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.
class Holehe():

    async def search(self, email: str, timeout: int = 10, csv: bool = False, no_password_recovery: bool = False,
                     no_color: bool = False, no_clear: bool = False, only_used: bool = False):
        args_dict = {'nopasswordrecovery': no_password_recovery, 'nocolor': no_color, 'noclear': no_clear,
                     'onlyused': only_used, 'csvoutput': csv}

        args = argparse.Namespace(**args_dict)

        ## code from here onwards
        check_update()
        credit()

        if not is_email(email):
            exit("[-] Please enter a target email ! \nExample : holehe email@example.com")

        # Import Modules
        modules = import_submodules("holehe.modules")
        websites = get_functions(modules, args)
        # Get timeout

        # Start time
        start_time = time.time()
        # Def the async client
        client = httpx.AsyncClient(timeout=timeout)
        # Launching the modules
        out = []
        instrument = TrioProgress(len(websites))
        trio.lowlevel.add_instrument(instrument)
        async with trio.open_nursery() as nursery:
            for website in websites:
                nursery.start_soon(launch_module, website, email, client, out)
        trio.lowlevel.remove_instrument(instrument)
        # Sort by modules names
        out = sorted(out, key=lambda i: i['name'])
        # Close the client
        await client.aclose()
        # Print the result
        print_result(out, args, email, start_time, websites)
        credit()
        # Export results
        export_csv(out, args, email)
        return out
