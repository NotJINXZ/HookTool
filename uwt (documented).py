import discord
from aiohttp import ClientSession
from asyncio import run as Run
from platform import system as System
from pystyle import Colors, Center
from time import sleep as Sleep
from time import strftime
import os
from re import compile
from json import load, dump

class Utilities:
    def log(self, log_type: str, message: str, should_print: bool = True):
        """Log messages with different types.

        Args:
            log_type (str): Type of log message (info, warn, success, error).
            message (str): The log message.
            should_print (bool, optional): Whether to print the log message. Defaults to True.

        Raises:
            ValueError: If an invalid log type is provided.

        Returns:
            str: The formatted log message.
        """
        
        options = {
            "info": f"{Colors.gray}[{Colors.blue}!{Colors.gray}]{Colors.reset}",
            "warn": f"{Colors.gray}[{Colors.yellow}?{Colors.gray}]{Colors.reset}",
            "success": f"{Colors.gray}[{Colors.green}+{Colors.gray}]{Colors.reset}",
            "error": f"{Colors.gray}[{Colors.red}-{Colors.gray}]{Colors.reset}",
        }
        
        if log_type not in options:
            raise ValueError("Invalid type for logging.")
        output = f"{options[log_type]} {Colors.gray}[{Colors.reset}{strftime('%H:%M:%S')}{Colors.gray}]{Colors.reset}: {message}"

        if should_print:
            print(output)
            return
        else:
            return output
    
    def clear(self, message: str = None):
        """Clear the console screen.

        Args:
            message (str, optional): Message to print after clearing. Defaults to None.

        Raises:
            RuntimeError: If clearing the screen is not supported on the current system.
        """
        
        system = System()
        if system in ["Linux", "Darwin"]:  # Unix/Linux/MacOS
            os.system('clear')
        elif system == "Windows":
            os.system('cls')
        else:
            raise RuntimeError(f"Clearing the screen is not supported on {system}.")
        
        if message:
            print(message)
        return

    def title(self, title: str = None):
        """Set the terminal title on various platforms.

        Args:
            title (str): The new title for the terminal.

        Raises:
            RuntimeError: If setting the terminal title is not supported on the current system.
        """
        system = System()
        if system == "Windows":
            os.system(f'title {title}')
        elif system in ["Linux", "Darwin"]:  # Unix/Linux/MacOS
            print(f"\033]0;{title}\007", end='', flush=True)
        else:
            pass
            #raise RuntimeError(f"Setting the terminal title is not supported on {system}.")
    
    def menu(self, *args):
        """Create a text menu.

        Returns:
            tuple: A tuple containing the formatted text menu and a list of menu items.
        """
        
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
        """Initialize the WHT class with a Discord webhook URL.

        Args:
            webhook_url (str): Discord webhook URL.
        """
        
        self.webhook_url = webhook_url
    
    
    async def send(self, **kwargs):
        """Send a message to the Discord webhook.

        Returns:
            tuple: A tuple containing a boolean indicating success and an error message (if any).
        """
        
        try:
            async with ClientSession() as session:
                webhook: discord.Webhook = discord.Webhook.from_url(self.webhook_url, session=session)
                await webhook.send(**kwargs)
            return True, None
        except Exception as e:
            return False, e
        
    async def validate(self, webhook_url: str = None):
        """Validate a Discord webhook URL.

        Args:
            webhook_url (str, optional): Discord webhook URL to validate. Defaults to None.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        
        webhook_url = webhook_url or self.webhook_url

        if not compile(r'^https://(?:ptb\.|canary\.)?discord\.com/api/webhooks/').match(webhook_url):
            return False
        
        
        async with ClientSession() as session:
            try:
                async with session.get(webhook_url) as response:
                    await session.close()
                    return True if response.status == 200 else False
            except Exception:
                return False
            
    async def delete(self, webhook_url: str = None):
        """Delete a Discord webhook.

        Args:
            webhook_url (str, optional): Discord webhook URL to delete. Defaults to None.

        Returns:
            tuple: A tuple containing a boolean indicating success and an error message (if any).
        """
        
        webhook_url = webhook_url or self.webhook_url
     
        async with ClientSession() as session:
            try:
                async with session.delete(webhook_url) as response:
                    await session.close()
                return True, None
            except Exception as e:
                return False, e
            
    async def get(self, webhook_url: str = None):
        """Retrieve information from a Discord webhook.

        Args:
            webhook_url (str, optional): Discord webhook URL to get information from. Defaults to None.

        Returns:
            dict: JSON data containing information from the webhook.
        """
        
        webhook_url = webhook_url or self.webhook_url
     
        async with ClientSession() as session:
            try:
                async with session.get(webhook_url) as response:
                    await session.close()
                    return await response.json()
            except Exception as e:
                return None

    async def update(self, new_data: dict, webhook_url: str = None):
        """Update a Discord webhook with new data.

        Args:
            new_data (dict): New data to update the webhook.
            webhook_url (str, optional): Discord webhook URL to update. Defaults to None.

        Returns:
            tuple: A tuple containing a boolean indicating success and an error message (if any).
        """
        
        webhook_url = webhook_url or self.webhook_url

        async with ClientSession() as session:
            try:
                async with session.patch(webhook_url, json=new_data) as response:
                    await session.close()
                return True, None
            except Exception as e:
                return False, e
    
message = None

async def main():
    global message
    util = Utilities()
    
    util.clear(util.log("info", "Loading...", False))
    ### Loading shit will go here ###
    util.title(f"UWT - Not logged in")
    os.makedirs("saves", exist_ok=True)
    os.makedirs("saves\\embeds", exist_ok=True)
    os.makedirs("saves\\plaintext", exist_ok=True)
    util.clear()
    
    while True:
        # util.clear()
        util.title(f"UWT - Logging in...")
        webhook = WHT(input(util.log("info", "Enter your webhook url: ", False)))
        if webhook.webhook_url != "bypass":
            if not await webhook.validate():
                util.log("error", "The webhook you provided is invalid.")
                continue
            else:
                data = await webhook.get()
                util.title(f"UWT - Logged in as {data['name']}")
            

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
                Sleep(2.5)
            
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
                        Sleep(2.5)
                        
                    if option in [1, 2]:
                        while True:
                            choice = input(Center.XCenter(util.log("info", "Would you like to load a saved message? (y/n): ", False), 50)).lower()
                            if choice == "y":
                                break
                            elif choice == "n":
                                break
                        
                        util.clear()
                        if choice == "y":
                            path = "saves\\plaintext" if option == 1 else "saves\\embeds"

                            while True:
                                menu1, options1 = util.menu(*os.listdir(path), "Go Back")
                                util.clear()
                                print(Center.Center(menu1, 50) + "\n "*3)
                                try:
                                    option1 = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50))) - 1
                                except ValueError:
                                    option1 = "Invalid Placeholder"
                                if option1 not in range(len(options1)):
                                    util.clear()
                                    print(Center.Center(menu1, 50) + "\n "*3)

                                    print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                                    Sleep(2.5)
                                    continue
                                                        
                                with open(os.path.join(path, os.listdir(path)[option1]), "r+") as file:
                                    util.clear()
                                    message = load(file)
                                    ignored = ["type"]
                                    for a in message:
                                        if a in ignored:
                                            continue
                                        
                                        util.log("info", f"{a}: {message[a]}")
                                    
                                    file.close()
                                    print("\n")
                                    
                                while True:
                                    choice = input(util.log("warn", "Is this the correct message? (y/n): ", False), 50).lower()
                                    if choice == "y":
                                        break
                                    elif choice == "n":
                                        continue
                    
                    if option == 1:
                        if not message:
                            content = input(util.log("info", "Message Content: ", False))
                            while True:
                                choice = input(util.log("info", "Would you like to save this message for future use? (y/n): ", False)).lower()
                                if choice == "y":
                                    file = "saves\\plaintext\\{}.json".format(len(os.listdir('saves\\plaintext')))
                                    with open(file, "w") as w:
                                        data = {}
                                        data["content"] = content
                                        dump(data, w)
                                        w.close()
                                    break
                                elif choice == "n":
                                    break
                        else:
                            content = message["content"]
                            
                        response, e = await webhook.send(content=content)
                        if response:
                            util.log("success", "Successfully sent message.")
                        else:
                            util.log("error", f"An error has occured: {e}.")
                    
                    elif option == 2:
                        if not message:
                            embed = discord.Embed()
                            embed.title = input(util.log("info", "Embed Title: ", False))
                            embed.description = input(util.log("info", "Embed Description: ", False))
                            content = input(util.log("info", "Message Content: ", False))
                            while True:
                                choice = input(util.log("info", "Would you like to save this message for future use? (y/n): ", False)).lower()
                                if choice == "y":
                                    file = "saves\\embeds\\{}.json".format(len(os.listdir('saves\\embeds')))
                                    with open(file, "w") as w:
                                        data = embed.to_dict()
                                        data["content"] = content
                                        dump(data, w)
                                        w.close()
                                    break
                                elif choice == "n":
                                    break
                        else:
                            embed = discord.Embed().from_dict(message)
                            content = message["content"]
                        
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
                    message = None
                    util.clear()
                    menu, options = util.menu("Regular Message", "Embeded Message", "Go Back")
                    print(Center.Center(menu, 50) + "\n "*3)
                    
                    try: option = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50)))
                    except ValueError: option = "Invalid Placeholder"
                    
                    if option not in range(len(options)):
                        util.clear()
                        print(Center.Center(menu, 50) + "\n "*3)
            
                        print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                        Sleep(2.5)
                                
                    if option in [1, 2]:
                        while True:
                            choice = input(Center.XCenter(util.log("info", "Would you like to load a saved message? (y/n): ", False), 50)).lower()
                            if choice == "y":
                                break
                            elif choice == "n":
                                break
                        
                        util.clear()
                        if choice == "y":
                            path = "saves\\plaintext" if option == 1 else "saves\\embeds"

                            while True:
                                menu1, options1 = util.menu(*os.listdir(path), "Go Back")
                                util.clear()
                                print(Center.Center(menu1, 50) + "\n "*3)
                                try:
                                    option1 = int(input(Center.XCenter(util.log("info", "Enter your option: ", False), 50))) - 1
                                except ValueError:
                                    option1 = "Invalid Placeholder"
                                if option1 not in range(len(options1)):
                                    util.clear()
                                    print(Center.Center(menu1, 50) + "\n "*3)

                                    print(Center.XCenter(util.log("error", "That option is not valid, Please try again.", False), 50))
                                    Sleep(2.5)
                                    continue
                                                        
                                with open(os.path.join(path, os.listdir(path)[option1]), "r+") as file:
                                    util.clear()
                                    message = load(file)
                                    ignored = ["type"]
                                    for a in message:
                                        if a in ignored:
                                            continue
                                        
                                        util.log("info", f"{a}: {message[a]}")
                                    
                                    file.close()
                                    print("\n")
                                    
                                while True:
                                    choice = input(util.log("warn", "Is this the correct message? (y/n): ", False), 50).lower()
                                    if choice == "y":
                                        break
                                    elif choice == "n":
                                        continue
                    
                    if option == 1:
                        while True:
                            try: 
                                iterations = int(input(util.log("info", "Number of messages to send: ", False)))
                                break
                            except: pass
                        
                        if not message:
                            content = input(util.log("info", "Message Content: ", False))
                            while True:
                                choice = input(util.log("info", "Would you like to save this message for future use? (y/n): ", False)).lower()
                                if choice == "y":
                                    file = "saves\\plaintext\\{}.json".format(len(os.listdir('saves\\plaintext')))
                                    with open(file, "w") as w:
                                        data = {}
                                        data["content"] = content
                                        dump(data, w)
                                        w.close()
                                    break
                                elif choice == "n":
                                    break
                        else:
                            content = message["content"]
                            
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
                        
                        if not message:
                            embed = discord.Embed()
                            embed.title = input(util.log("info", "Embed Title: ", False))
                            embed.description = input(util.log("info", "Embed Description: ", False))
                            content = input(util.log("info", "Message Content: ", False))
                            while True:
                                choice = input(util.log("info", "Would you like to save this message for future use? (y/n): ", False)).lower()
                                if choice == "y":
                                    file = "saves\\embeds\\{}.json".format(len(os.listdir('saves\\embeds')))
                                    with open(file, "w") as w:
                                        data = embed.to_dict()
                                        data["content"] = content
                                        dump(data, w)
                                        w.close()
                                    break
                                elif choice == "n":
                                    break
                        else:
                            embed = discord.Embed().from_dict(message)
                            content = message["content"]
                        
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
                while True:
                    choice = input(util.log("warn", "Are you sure you want to delete this webhook? (y/n): ", False)).lower()
                    if choice == "y":
                        break
                    elif choice == "n":
                        break
                if choice == "y": 
                    response, e = await webhook.delete()
                    if response:
                        util.log("success", "Successfully deleted webhook.")
                        input(util.log("info", "Press enter to continue...", False))
                        break

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
                util.log("info", f"Guild ID: {data['guild_id']}")
                util.log("info", f"Channel ID: {data['channel_id']}")
                util.log("info", f"Application ID: {data['application_id']}")
                util.log("info", f"Avatar: {data['avatar']} (https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}.png)")
                if wtype in [1, 2]:
                    print("\n")
                    util.log("info", f"User Information:")
                    util.log("info", f"Username: {data['user']['username']}")
                    util.log("info", f"Discriminator: {data['user']['discriminator']}")
                    util.log("info", f"ID: {data['user']['id']}")
                    util.log("info", f"Avatar: {data['user']['avatar']} (https://cdn.discordapp.com/avatars/{data['user']['id']}/{data['user']['avatar']}.png)")
                    util.log("info", f"Public Flags: {data['user']['public_flags']}")
                if wtype == 2:
                    print("\n")
                    util.log("info", f"Source Information:")
                    util.log("info", f"Guild ID: {data['source_guild']['id']}")
                    util.log("info", f"Guild Name: {data['source_guild']['name']}")
                    util.log("info", f"Guild Icon: {data['source_guild']['icon']} (https://cdn.discordapp.com/icons/{data['source_guild']['id']}/{data['source_guild']['icon']}.png)")
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
    Run(main())