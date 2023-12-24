import discord
import aiohttp
import asyncio
import platform
from pystyle import Colors, Center
import time
import os
import re

class Utilities:
    def log(self, log_type: str, message: str, should_print: bool = True):
        options = {
            "info": f"{Colors.gray}[{Colors.blue}!{Colors.gray}]{Colors.reset}",
            "warn": f"{Colors.gray}[{Colors.yellow}?{Colors.gray}]{Colors.reset}",
            "success": f"{Colors.gray}[{Colors.green}+{Colors.gray}]{Colors.reset}",
            "error": f"{Colors.gray}[{Colors.red}-{Colors.gray}]{Colors.reset}",
        }
        
        if log_type not in options:
            raise ValueError("Invalid type for logging.")
        output = f"{options[log_type]} {Colors.gray}[{Colors.reset}{time.strftime('%H:%M:%S')}{Colors.gray}]{Colors.reset}: {message}"
        if should_print:
            print(output)
            return
        else:
            return output
    
    def clear(self, message: str = None):
        system = platform.system()
        if system in ["Linux", "Darwin"]:  # Unix/Linux/MacOS
            os.system('clear')
        elif system == "Windows":
            os.system('cls')
        else:
            raise RuntimeError(f"Clearing the screen is not supported on {system}.")
        
        if message:
            print(message)
        return
    
    def menu(self, *args):

        text = ""
        for i, arg in enumerate(args):
            if i != len(args) - 1:
                text += f"{Colors.gray}[{Colors.green}{i + 1}{Colors.gray}]{Colors.reset}: {arg}\n"
            else:
                text += f"\n{Colors.gray}[{Colors.red}0{Colors.gray}]{Colors.reset}: {arg}"
        
        text = text.strip()
        return text, list(args)
    
class WHT:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    
    async def send(self, **kwargs):
        try:
            async with aiohttp.ClientSession() as session:
                webhook: discord.Webhook = discord.Webhook.from_url(self.webhook_url, session=session)
                await webhook.send(**kwargs)
            return True, None
        except Exception as e:
            return False, e
        
    async def validate(self, webhook_url: str = None):
        webhook_url = webhook_url or self.webhook_url

        if not re.compile(r'^https://(?:ptb\.|canary\.)?discord\.com/api/webhooks/').match(webhook_url):
            return False
        
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(webhook_url) as response:
                    await session.close()
                    return True if response.status == 200 else False
            except Exception:
                return False
            
    async def delete(self, webhook_url: str = None):
        webhook_url = webhook_url or self.webhook_url
     
        async with aiohttp.ClientSession() as session:
            try:
                async with session.delete(webhook_url) as response:
                    await session.close()
                return True, None
            except Exception as e:
                return False, e
            
    async def get(self, webhook_url: str = None):
        webhook_url = webhook_url or self.webhook_url
     
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(webhook_url) as response:
                    await session.close()
                    return await response.json()
            except Exception as e:
                return None

    async def update(self, new_data: dict, webhook_url: str = None):
        webhook_url = webhook_url or self.webhook_url

        async with aiohttp.ClientSession() as session:
            try:
                async with session.patch(webhook_url, json=new_data) as response:
                    await session.close()
                return True, None
            except Exception as e:
                return False, e
    
async def main():
    util = Utilities()
    
    util.clear(util.log("info", "Loading...", False))
    ### Loading shit will go here ###
    util.clear()
    
    while True:
        # util.clear()
        webhook = WHT(input(util.log("info", "Enter your webhook url: ", False)))
        if webhook.webhook_url != "bypass":
            if not await webhook.validate():
                util.log("error", "The webhook you provided is invalid.")
                continue
            

        while True:
            util.clear()
            menu, options = util.menu("Send Message", "Spam Message", "Delete Webhook", "Webhook Information", "Change Webhook Information", "Logout")
            print(Center.Center(menu, 50) + "\n "*3)
            
            try: option = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50)))
            except ValueError: option = "Invalid Placeholder"
            
            if option not in range(len(options)):
                util.clear()
                print(Center.Center(menu, 50) + "\n "*3)
    
                print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                time.sleep(2.5)
            
            if option == 1:
                while True:
                    util.clear()
                    menu, options = util.menu("Regular Message", "Embeded Message", "Go Back")
                    print(Center.Center(menu, 50) + "\n "*3)
                    
                    try: option = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50)))
                    except ValueError: option = "Invalid Placeholder"
                    
                    if option not in range(len(options)):
                        util.clear()
                        print(Center.Center(menu, 50) + "\n "*3)
            
                        print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                        time.sleep(2.5)
                    
                    if option == 1:
                        response, e = await webhook.send(content=input(util.log("info", "Message Content: ", False)))
                        if response:
                            util.log("success", "Successfully sent message.")
                        else:
                            util.log("error", f"An error has occured: {e}.")
                    
                    elif option == 2:
                        embed = discord.Embed()
                        embed.title = input(util.log("info", "Embed Title: ", False))
                        embed.description = input(util.log("info", "Embed Description: ", False))
                        content = input(util.log("info", "Message Content: ", False))
                        
                        response, e = await webhook.send(embed=embed, content=content)
                        if response:
                            util.log("success", "Successfully sent message.")
                        else:
                            util.log("error", f"An error has occured: {e}.")

                    elif option == 0:
                        break
                    
                    print("\n")
                    input(util.log("info", "Press enter to continue...", False))
            elif option == 2:
                while True:
                    util.clear()
                    menu, options = util.menu("Regular Message", "Embeded Message", "Go Back")
                    print(Center.Center(menu, 50) + "\n "*3)
                    
                    try: option = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50)))
                    except ValueError: option = "Invalid Placeholder"
                    
                    if option not in range(len(options)):
                        util.clear()
                        print(Center.Center(menu, 50) + "\n "*3)
            
                        print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                        time.sleep(2.5)
                    
                    if option == 1:
                        while True:
                            try: 
                                iterations = int(input(util.log("info", "Number of messages to send: ", False)))
                                break
                            except: pass
                        
                        content = input(util.log("info", "Message Content: ", False)) 
                        success = 0
                        for i in range(iterations):
                            response, e = await webhook.send(content=content)
                            if response:
                                success += 1
                                util.log("success", "Successfully sent message.")
                            else:
                                util.log("error", f"An error has occured: {e}.")
                        
                        util.log("info", f"Finished sending {iterations} messages. ({success} message{'s' if success > 1 else None} succeeded, {iterations - success} message{'s' if success > 1 else None} failed)")
                        input(util.log("info", "Press enter to continue...", False))
                        continue
                        
                    elif option == 2:
                        while True:
                            try: 
                                iterations = int(input(util.log("info", "Number of messages to send: ", False)))
                                break
                            except: pass
                            
                        embed = discord.Embed()
                        embed.title = input(util.log("info", "Embed Title: ", False))
                        embed.description = input(util.log("info", "Embed Description: ", False))
                        content = input(util.log("info", "Message Content: ", False))
                        
                        success = 0
                        for i in range(iterations):
                            response, e = await webhook.send(content=content, embed=embed)
                            if response:
                                success += 1
                                util.log("success", "Successfully sent message.")
                            else:
                                util.log("error", f"An error has occured: {e}.")
                        
                        util.log("info", f"Finished sending {iterations} messages. ({success} message{'s' if success > 1 else None} succeeded, {iterations - success} message{'s' if success > 1 else None} failed)")
                        input(util.log("info", "Press enter to continue...", False))
                        continue
                    
                    elif option == 0:
                        break
            
            elif option == 3:
                response, e = await webhook.delete()
                if response:
                    util.log("success", "Successfully deleted webhook.")
                else:
                    util.log("error", f"An error has occured: {e}.")

                input(util.log("info", "Press enter to continue...", False))
                continue
            
            elif option == 4:
                data = await webhook.get()
                print("\n"*3)
                wtype = data["type"]
                if wtype == 1:
                    wtypestr = "Incoming Webhook"
                elif wtype == 2:
                    wtypestr = "Channel Follower Webhook"
                elif wtype == 3:
                    wtypestr = "Application Webhook"
                else:
                    wtypestr = "Unknown Webhook Type"
                
                util.log("info", f"General Webhook Information:")
                util.log("info", f"Name: {data['name']}")
                util.log("info", f"Type: {wtype} ({wtypestr})")
                util.log("info", f"ID: {data['id']}")
                util.log("info", f"Token: {data['token']}")
                util.log("info", f"Avatar: {data['avatar']}")
                util.log("info", f"Guild ID: {data['guild_id']}")
                util.log("info", f"Channel ID: {data['channel_id']}")
                util.log("info", f"Application ID: {data['application_id']}")
                util.log("info", f"Avatar: {data['avatar']}")
                if wtype in [1, 2]:
                    print("\n")
                    util.log("info", f"User Information:")
                    util.log("info", f"Username: {data['user']['username']}")
                    util.log("info", f"Discriminator: {data['user']['discriminator']}")
                    util.log("info", f"ID: {data['user']['id']}")
                    util.log("info", f"Avatar: {data['user']['avatar']}")
                    util.log("info", f"Public Flags: {data['user']['public_flags']}")
                if wtype == 2:
                    print("\n")
                    util.log("info", f"Source Information:")
                    util.log("info", f"Guild ID: {data['source_guild']['id']}")
                    util.log("info", f"Guild Name: {data['source_guild']['name']}")
                    util.log("info", f"Guild Icon: {data['source_guild']['icon']}")
                    util.log("info", f"Guild ID: {data['source_guild']['id']}")
                    util.log("info", f"Channel ID: {data['source_channel']['id']}")
                    util.log("info", f"Channel Name: {data['source_channel']['name']}")

                print("\n")
                input(util.log("info", "Press enter to continue...", False))
                continue
            
            elif option == 5:
                username = input(util.log("info", "Enter new username: ", False))
                if username == "":
                    util.log("info", "No new username found, not proceeding...")
                else:
                    response, e = await webhook.update({"username": username})
                    if response:
                        util.log("success", "Successfully updated webhook.")
                    else:
                        util.log("error", f"An error has occured: {e}.")
                        
                print("\n")
                input(util.log("info", "Press enter to continue...", False))

            elif option == 0:
                util.clear()
                break
            
if __name__ == "__main__":
    asyncio.run(main())