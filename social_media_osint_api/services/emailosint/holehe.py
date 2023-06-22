import trio
from holehe.modules.crowfunding.buymeacoffee import *
from holehe.modules.forum.cracked_to import *
from holehe.modules.mails.google import google
from holehe.modules.mails.protonmail import protonmail
from holehe.modules.mails.yahoo import yahoo
from holehe.modules.music.spotify import *
from holehe.modules.porn.pornhub import *
from holehe.modules.porn.redtube import *
from holehe.modules.porn.xvideos import *
from holehe.modules.programing.github import *
from holehe.modules.shopping.amazon import *
from holehe.modules.shopping.ebay import *
from holehe.modules.social_media.discord import *
from holehe.modules.social_media.instagram import *
from holehe.modules.social_media.pinterest import pinterest
from holehe.modules.social_media.snapchat import *
from holehe.modules.social_media.tumblr import tumblr
from holehe.modules.social_media.twitter import *
from holehe.modules.transport.blablacar import *

from social_media_osint_api.services.emailosint.email_request import EmailRequest


# Holehe checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.
# Only a handful of modules with holehe have been used, see https://github.com/megadose/holehe
class Holehe(EmailRequest):

    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in Holehe...'.format(email))
        try:
            list_acc = []

            # Ecommerce
            async def acc_amazon():
                out = []
                client = httpx.AsyncClient()
                await amazon(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_ebay():
                out = []
                client = httpx.AsyncClient()
                await ebay(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # Social Media
            async def acc_snapchat():
                out = []
                client = httpx.AsyncClient()
                await snapchat(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_pinterest():
                out = []
                client = httpx.AsyncClient()
                await pinterest(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_tumblr():
                out = []
                client = httpx.AsyncClient()
                await tumblr(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_discord():
                out = []
                client = httpx.AsyncClient()
                await discord(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_instagram():
                out = []
                client = httpx.AsyncClient()
                await instagram(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_twitter():
                out = []
                client = httpx.AsyncClient()
                await twitter(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # crowfunding
            async def acc_buymeacoffee():
                out = []
                client = httpx.AsyncClient()
                await buymeacoffee(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # transport
            async def acc_blablacar():
                out = []
                client = httpx.AsyncClient()
                await blablacar(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_cracked_to():
                out = []
                client = httpx.AsyncClient()
                await cracked_to(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # programing
            async def acc_github():
                out = []
                client = httpx.AsyncClient()
                await github(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # music
            async def acc_spotify():
                out = []
                client = httpx.AsyncClient()
                await spotify(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # Email
            async def acc_google():
                out = []
                client = httpx.AsyncClient()
                await google(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_yahoo():
                out = []
                client = httpx.AsyncClient()
                await yahoo(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_protonmail():
                out = []
                client = httpx.AsyncClient()
                await protonmail(email, client, out)
                list_acc.append(out)
                await client.aclose()

            # X-Rated Sites
            async def acc_redtube():
                out = []
                client = httpx.AsyncClient()
                await redtube(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_pornhub():
                out = []
                client = httpx.AsyncClient()
                await pornhub(email, client, out)
                list_acc.append(out)
                await client.aclose()

            async def acc_xvideos():
                out = []
                client = httpx.AsyncClient()
                await xvideos(email, client, out)
                list_acc.append(out)
                await client.aclose()

            trio.run(acc_amazon)
            trio.run(acc_ebay)
            trio.run(acc_blablacar)
            trio.run(acc_buymeacoffee)
            trio.run(acc_cracked_to)
            trio.run(acc_github)
            trio.run(acc_snapchat)
            trio.run(acc_discord)
            trio.run(acc_tumblr())
            trio.run(acc_instagram)
            trio.run(acc_pinterest)
            trio.run(acc_twitter)
            trio.run(acc_spotify)
            trio.run(acc_redtube)
            trio.run(acc_pornhub)
            trio.run(acc_xvideos)

            accounts_founds = []

            for i in list_acc:
                try:
                    if i[0]['exists']:
                        accounts_founds.append(i[0]['name'])
                except:
                    pass

            a = accounts_founds
            founds = str(a).replace('[', '').replace(']', '').replace("'", "").replace(', ', '\n- ').upper()

            print("- " + founds)

        except:
            return None
