
import os
import sys
#os.system("pip install aiohttp")
os.system("pip install jishaku")
os.system("pip install requests")
import ast
import inspect
import re
import time
import asyncio
import aiohttp
import discord
import requests
import jishaku
import time
from discord.ext import commands
os.system("clear")

f = open("alive.txt", "r")
# launch = f.read()
# if launch == "true":
#    print("starting sniper")
# else:
#   sys.exit()



ip = requests.get('https://api.ipify.org/').text
print(ip)
vanity_list = []
delay = 0
sleep = 0
console = "960162042503917658"
guild = "959795104372125756"
shards = 1 


#os.system("clear")


tkn = ""
prefix = "."




# sniper 1 - 

intents = discord.Intents.all()
intents.members = True
intents.messages = True
headers = {'Authorization': "Bot {}".format(tkn), 'X-Audit-Log-Reason': 'clapped by risinplayz'}
client = commands.AutoShardedBot(shard_count=shards, command_prefix=prefix, case_insensitive=True, intents=intents)

client.remove_command('help')
client.load_extension('jishaku')



@client.event 
async def on_command_error(ctx, error): 
  return
  
  
  
@client.event
async def on_ready():
  print("READYYYYYYYY")  
  
  
@client.event
async def on_connect():
  guild_ = client.get_guild(int(guild))
  code__ = await guild_.vanity_invite()
  code_ = code__.code
  print(code_)
  if str(code_) in vanity_list:
    sys.exit()
  snipe_msg = ""
  for day in vanity_list:
    snipe_msg += f"• {day}\n" 
  conn = aiohttp.TCPConnector(limit=10)
  async with aiohttp.ClientSession(headers=headers, connector=conn) as session:
    async with session.post(f"https://canary.discord.com/api/v9/channels/{console}/messages", json={'content': '>>> websocket connected.\nProxy: '+ip+'\n__Sniping List__-\n'+snipe_msg}) as ok:
      print(ok.status)
    for idk in range(999999999999999999999):
        await asyncio.sleep(delay)
        #idkk = time.perf_counter()
        startz = time.perf_counter()
        for vx in vanity_list:
          await asyncio.sleep(sleep)
          async with session.get(f"https://canary.discord.com/api/v9/invites/{vx}") as v:
            #print(v.status)
              if v.status == 429:
                 async with session.post(f"https://canary.discord.com/api/v9/channels/{console}/messages", json={'content': '@everyone got rate limited, sleeping for 30s.'}) as ok:
                   print(ok.status)
                   time.sleep(30)
              elif v.status == 200:
                print('\033[92m'+"[+] Attempt " + str(idk) + " status: 200 | "+vx) 
                
              elif v.status == 404:
                  async with session.patch(f"https://discord.com/api/v9/guilds/{guild}/vanity-url", json={'code': vx}) as r: 
                      if r.status == 200:
                        
                        async with session.post(f"https://discord.com/api/v9/channels/{console}/messages", json={'content': '@everyone vanity sniped.\n'+'https://discord.gg/'+vx}) as ok:
                          print(ok.status) 
                  
                          f = open("alive.txt", "w"); f.write("false"); f.close(); sys.exit()
                     
                          sys.exit()
              else:
                print(v.status)
        endz = time.perf_counter()
        count = endz - startz
        print(f"[~] Took {count} seconds.") 
        if count < 1:
          print("[-] Sleeping for 0.9 seconds.")
          await asyncio.sleep(0.9)




  
  
  
            

client.run(tkn)
