### Minified using https://python-minifier.com to increase speed. ###
### To view clean source, view [uwt (documented).py]. ###



_I='Windows'
_H='Darwin'
_G='warn'
_F='success'
_E='error'
_D=None
_C=True
_B=False
_A='info'
import discord
from aiohttp import ClientSession
from asyncio import run as Run
from platform import system as System
from pystyle import Colors,Center
from time import sleep as Sleep
from time import strftime
import os
from re import compile
from json import load,dump
import subprocess,sys
class Utilities:
	def log(self,log_type,message,should_print=_C):
		'Log messages with different types.\n\n        Args:\n            log_type (str): Type of log message (info, warn, success, error).\n            message (str): The log message.\n            should_print (bool, optional): Whether to print the log message. Defaults to True.\n\n        Raises:\n            ValueError: If an invalid log type is provided.\n\n        Returns:\n            str: The formatted log message.\n        ';options={_A:f"{Colors.gray}[{Colors.blue}!{Colors.gray}]{Colors.reset}",_G:f"{Colors.gray}[{Colors.yellow}?{Colors.gray}]{Colors.reset}",_F:f"{Colors.gray}[{Colors.green}+{Colors.gray}]{Colors.reset}",_E:f"{Colors.gray}[{Colors.red}-{Colors.gray}]{Colors.reset}"}
		if log_type not in options:raise ValueError('Invalid type for logging.')
		output=f"{options[log_type]} {Colors.gray}[{Colors.reset}{strftime('%H:%M:%S')}{Colors.gray}]{Colors.reset}: {message}"
		if should_print:print(output);return
		else:return output
	def clear(self,message=_D):
		'Clear the console screen.\n\n        Args:\n            message (str, optional): Message to print after clearing. Defaults to None.\n\n        Raises:\n            RuntimeError: If clearing the screen is not supported on the current system.\n        ';system=System()
		if system in['Linux',_H]:os.system('clear')
		elif system==_I:os.system('cls')
		else:raise RuntimeError(f"Clearing the screen is not supported on {system}.")
		if message:print(message)
	def title(self,title=_D):
		'Set the terminal title on various platforms.\n\n        Args:\n            title (str): The new title for the terminal.\n\n        Raises:\n            RuntimeError: If setting the terminal title is not supported on the current system.\n        ';system=System()
		if system==_I:os.system(f"title {title}")
		elif system in['Linux',_H]:print(f"]0;{title}\a",end='',flush=_C)
		else:0
	def menu(self,*args):
		'Create a text menu.\n\n        Returns:\n            tuple: A tuple containing the formatted text menu and a list of menu items.\n        ';text=''
		for(i,arg)in enumerate(args):
			if i!=len(args)-1:text+=f"{Colors.gray}[{Colors.green}{i+1}{Colors.gray}]{Colors.reset}: {arg}\n"
			else:text+=f"\n{Colors.gray}[{Colors.red}0{Colors.gray}]{Colors.reset}: {arg}"
		text=text.strip();return text,list(args)
class WHT:
	def __init__(self,webhook_url):'Initialize the WHT class with a Discord webhook URL.\n\n        Args:\n            webhook_url (str): Discord webhook URL.\n        ';self.webhook_url=webhook_url
	async def send(self,**kwargs):
		'Send a message to the Discord webhook.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        '
		try:
			async with ClientSession()as session:webhook=discord.Webhook.from_url(self.webhook_url,session=session);await webhook.send(**kwargs)
			return _C,_D
		except Exception as e:return _B,e
	async def validate(self,webhook_url=_D):
		'Validate a Discord webhook URL.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to validate. Defaults to None.\n\n        Returns:\n            bool: True if the URL is valid, False otherwise.\n        ';webhook_url=webhook_url or self.webhook_url
		if not compile('^https://(?:ptb\\.|canary\\.)?discord\\.com/api/webhooks/').match(webhook_url):return _B
		async with ClientSession()as session:
			try:
				async with session.get(webhook_url)as response:await session.close();return _C if response.status==200 else _B
			except Exception:return _B
	async def delete(self,webhook_url=_D):
		'Delete a Discord webhook.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to delete. Defaults to None.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        ';webhook_url=webhook_url or self.webhook_url
		async with ClientSession()as session:
			try:
				async with session.delete(webhook_url)as response:await session.close()
				return _C,_D
			except Exception as e:return _B,e
	async def get(self,webhook_url=_D):
		'Retrieve information from a Discord webhook.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to get information from. Defaults to None.\n\n        Returns:\n            dict: JSON data containing information from the webhook.\n        ';webhook_url=webhook_url or self.webhook_url
		async with ClientSession()as session:
			try:
				async with session.get(webhook_url)as response:await session.close();return await response.json()
			except Exception as e:return
	async def update(self,new_data,webhook_url=_D):
		'Update a Discord webhook with new data.\n\n        Args:\n            new_data (dict): New data to update the webhook.\n            webhook_url (str, optional): Discord webhook URL to update. Defaults to None.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        ';webhook_url=webhook_url or self.webhook_url
		async with ClientSession()as session:
			try:
				async with session.patch(webhook_url,json=new_data)as response:await session.close()
				return _C,_D
			except Exception as e:return _B,e
message=_D
async def main():
	m='source_channel';l='icon';k='username';j='Number of messages to send: ';h='saves\\embeds\\{}.json';g='Embed Description: ';f='Embed Title: ';d='saves\\plaintext\\{}.json';c='Is this the correct message? (y/n): ';b='Would you like to load a saved message? (y/n): ';Z='Embeded Message';Y='Regular Message';X='type';W='avatar';V='s';U='Successfully sent message.';T='w';S='Would you like to save this message for future use? (y/n): ';R='Message Content: ';Q='Go Back';P='uwt.exe';O='That option is not valid, Please try again.';N='Invalid Placeholder';M='Enter your option: ';L='saves\\plaintext';K='saves\\embeds';J='name';I='source_guild';H='user';G='Press enter to continue...';F='id';E='content';D='\n';C='n';B='\n ';A='y';global message;util=Utilities();util.clear(util.log(_A,'Loading...',_B))
	if getattr(sys,'frozen',_B):
		util.log(_A,'Checking Version...');github_api_url='https://api.github.com/repos/NotJINXZ/uwt/releases';version='1.0.0'
		async with ClientSession()as session:
			async with session.get(github_api_url)as response:releases=await response.json()
			if releases:
				latest_release=next((release for release in releases if not release.get('prerelease',_B)),_D)
				if latest_release and latest_release['tag_name']!=version:
					util.log(_G,'Version does not match.');asset_url=next((asset['browser_download_url']for asset in latest_release['assets']if asset[J].endswith('.exe')),_D)
					if asset_url:
						file_name=asset_url.split('/')[-1]
						async with session.get(asset_url)as response:
							data=await response.read()
							with open(file_name,'wb')as file:file.write(data)
						if os.path.exists(P):os.remove(P)
						os.rename(file_name,P);subprocess.call([P])
	util.title(f"UWT - Not logged in");os.makedirs('saves',exist_ok=_C);os.makedirs(K,exist_ok=_C);os.makedirs(L,exist_ok=_C);util.clear()
	while _C:
		util.title(f"UWT - Logging in...");webhook=WHT(input(util.log(_A,'Enter your webhook url: ',_B)))
		if webhook.webhook_url!='bypass':
			if not await webhook.validate():util.log(_E,'The webhook you provided is invalid.');continue
			else:data=await webhook.get();util.title(f"UWT - Logged in as {data[J]}")
		while _C:
			util.clear();menu,options=util.menu('Send Message','Spam Message','Delete Webhook','Webhook Information','Change Webhook Information','Logout');print(Center.Center(menu,50)+B*3)
			try:option=int(input(Center.XCenter(util.log(_A,M,_B),50)))
			except ValueError:option=N
			if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,O,_B),50));Sleep(2.5)
			if option==1:
				while _C:
					util.clear();menu,options=util.menu(Y,Z,Q);print(Center.Center(menu,50)+B*3)
					try:option=int(input(Center.XCenter(util.log(_A,M,_B),50)))
					except ValueError:option=N
					if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,O,_B),50));Sleep(2.5)
					if option in[1,2]:
						while _C:
							choice=input(Center.XCenter(util.log(_A,b,_B),50)).lower()
							if choice==A:break
							elif choice==C:break
						util.clear()
						if choice==A:
							path=L if option==1 else K
							while _C:
								menu1,options1=util.menu(*os.listdir(path),Q);util.clear();print(Center.Center(menu1,50)+B*3)
								try:option1=int(input(Center.XCenter(util.log(_A,M,_B),50)))-1
								except ValueError:option1=N
								if option1 not in range(len(options1)):util.clear();print(Center.Center(menu1,50)+B*3);print(Center.XCenter(util.log(_E,O,_B),50));Sleep(2.5);continue
								with open(os.path.join(path,os.listdir(path)[option1]),'r+')as file:
									util.clear();message=load(file);ignored=[X]
									for a in message:
										if a in ignored:continue
										util.log(_A,f"{a}: {message[a]}")
									file.close();print(D)
								while _C:
									choice=input(util.log(_G,c,_B),50).lower()
									if choice==A:break
									elif choice==C:continue
					if option==1:
						if not message:
							content=input(util.log(_A,R,_B))
							while _C:
								choice=input(util.log(_A,S,_B)).lower()
								if choice==A:
									file=d.format(len(os.listdir(L)))
									with open(file,T)as w:data={};data[E]=content;dump(data,w);w.close()
									break
								elif choice==C:break
						else:content=message[E]
						response,e=await webhook.send(content=content)
						if response:util.log(_F,U)
						else:util.log(_E,f"An error has occured: {e}.")
					elif option==2:
						if not message:
							embed=discord.Embed();embed.title=input(util.log(_A,f,_B));embed.description=input(util.log(_A,g,_B));content=input(util.log(_A,R,_B))
							while _C:
								choice=input(util.log(_A,S,_B)).lower()
								if choice==A:
									file=h.format(len(os.listdir(K)))
									with open(file,T)as w:data=embed.to_dict();data[E]=content;dump(data,w);w.close()
									break
								elif choice==C:break
						else:embed=discord.Embed().from_dict(message);content=message[E]
						response,e=await webhook.send(embed=embed,content=content)
						if response:util.log(_F,U)
						else:util.log(_E,f"An error has occured: {e}.")
					elif option==0:break
					print(D);input(util.log(_A,G,_B))
			elif option==2:
				while _C:
					message=_D;util.clear();menu,options=util.menu(Y,Z,Q);print(Center.Center(menu,50)+B*3)
					try:option=int(input(Center.XCenter(util.log(_A,M,_B),50)))
					except ValueError:option=N
					if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,O,_B),50));Sleep(2.5)
					if option in[1,2]:
						while _C:
							choice=input(Center.XCenter(util.log(_A,b,_B),50)).lower()
							if choice==A:break
							elif choice==C:break
						util.clear()
						if choice==A:
							path=L if option==1 else K
							while _C:
								menu1,options1=util.menu(*os.listdir(path),Q);util.clear();print(Center.Center(menu1,50)+B*3)
								try:option1=int(input(Center.XCenter(util.log(_A,M,_B),50)))-1
								except ValueError:option1=N
								if option1 not in range(len(options1)):util.clear();print(Center.Center(menu1,50)+B*3);print(Center.XCenter(util.log(_E,O,_B),50));Sleep(2.5);continue
								with open(os.path.join(path,os.listdir(path)[option1]),'r+')as file:
									util.clear();message=load(file);ignored=[X]
									for a in message:
										if a in ignored:continue
										util.log(_A,f"{a}: {message[a]}")
									file.close();print(D)
								while _C:
									choice=input(util.log(_G,c,_B),50).lower()
									if choice==A:break
									elif choice==C:continue
					if option==1:
						while _C:
							try:iterations=int(input(util.log(_A,j,_B)));break
							except:pass
						if not message:
							content=input(util.log(_A,R,_B))
							while _C:
								choice=input(util.log(_A,S,_B)).lower()
								if choice==A:
									file=d.format(len(os.listdir(L)))
									with open(file,T)as w:data={};data[E]=content;dump(data,w);w.close()
									break
								elif choice==C:break
						else:content=message[E]
						success=0
						for i in range(iterations):
							response,e=await webhook.send(content=content)
							if response:success+=1;util.log(_F,U)
							else:util.log(_E,f"An error has occured: {e}.")
						util.log(_A,f"Finished sending {iterations} messages. ({success} message{V if success>1 else _D} succeeded, {iterations-success} message{V if success>1 else _D} failed)");input(util.log(_A,G,_B));continue
					elif option==2:
						while _C:
							try:iterations=int(input(util.log(_A,j,_B)));break
							except:pass
						if not message:
							embed=discord.Embed();embed.title=input(util.log(_A,f,_B));embed.description=input(util.log(_A,g,_B));content=input(util.log(_A,R,_B))
							while _C:
								choice=input(util.log(_A,S,_B)).lower()
								if choice==A:
									file=h.format(len(os.listdir(K)))
									with open(file,T)as w:data=embed.to_dict();data[E]=content;dump(data,w);w.close()
									break
								elif choice==C:break
						else:embed=discord.Embed().from_dict(message);content=message[E]
						success=0
						for i in range(iterations):
							response,e=await webhook.send(content=content,embed=embed)
							if response:success+=1;util.log(_F,U)
							else:util.log(_E,f"An error has occured: {e}.")
						util.log(_A,f"Finished sending {iterations} messages. ({success} message{V if success>1 else _D} succeeded, {iterations-success} message{V if success>1 else _D} failed)");input(util.log(_A,G,_B));continue
					elif option==0:break
			elif option==3:
				while _C:
					choice=input(util.log(_G,'Are you sure you want to delete this webhook? (y/n): ',_B)).lower()
					if choice==A:break
					elif choice==C:break
				if choice==A:
					response,e=await webhook.delete()
					if response:util.log(_F,'Successfully deleted webhook.');input(util.log(_A,G,_B));break
					else:util.log(_E,f"An error has occured: {e}.");input(util.log(_A,G,_B));continue
			elif option==4:
				data=await webhook.get();print(D*3);wtype=data[X]
				if wtype==1:wtypestr='Incoming Webhook'
				elif wtype==2:wtypestr='Channel Follower Webhook'
				elif wtype==3:wtypestr='Application Webhook'
				else:wtypestr='Unknown Webhook Type'
				util.log(_A,f"General Webhook Information:");util.log(_A,f"Name: {data[J]}");util.log(_A,f"Type: {wtype} ({wtypestr})");util.log(_A,f"ID: {data[F]}");util.log(_A,f"Token: {data['token']}");util.log(_A,f"Guild ID: {data['guild_id']}");util.log(_A,f"Channel ID: {data['channel_id']}");util.log(_A,f"Application ID: {data['application_id']}");util.log(_A,f"Avatar: {data[W]} (https://cdn.discordapp.com/avatars/{data[F]}/{data[W]}.png)")
				if wtype in[1,2]:print(D);util.log(_A,f"User Information:");util.log(_A,f"Username: {data[H][k]}");util.log(_A,f"Discriminator: {data[H]['discriminator']}");util.log(_A,f"ID: {data[H][F]}");util.log(_A,f"Avatar: {data[H][W]} (https://cdn.discordapp.com/avatars/{data[H][F]}/{data[H][W]}.png)");util.log(_A,f"Public Flags: {data[H]['public_flags']}")
				if wtype==2:print(D);util.log(_A,f"Source Information:");util.log(_A,f"Guild ID: {data[I][F]}");util.log(_A,f"Guild Name: {data[I][J]}");util.log(_A,f"Guild Icon: {data[I][l]} (https://cdn.discordapp.com/icons/{data[I][F]}/{data[I][l]}.png)");util.log(_A,f"Guild ID: {data[I][F]}");util.log(_A,f"Channel ID: {data[m][F]}");util.log(_A,f"Channel Name: {data[m][J]}")
				print(D);input(util.log(_A,G,_B));continue
			elif option==5:
				username=input(util.log(_A,'Enter new username: ',_B))
				if username=='':util.log(_A,'No new username found, not proceeding...')
				else:
					response,e=await webhook.update({k:username})
					if response:util.log(_F,'Successfully updated webhook.')
					else:util.log(_E,f"An error has occured: {e}.")
				print(D);input(util.log(_A,G,_B))
			elif option==0:util.clear();break
if __name__=='__main__':Run(main())