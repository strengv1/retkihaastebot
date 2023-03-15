# rastikiertelybot

Telegram bot that can be used to forward messages to a chat.
NOTE: Only works for python-telegram-bot versions 13.17 and under.

## Build instructions

Running the bot is easiest with docker. Build with:
`docker build --tag="retkihaaste" .`


Some environment variables are required:
|Variable name|Description|
|---|---|
| RASTIBOT_KEY | Telegram bot token |
| RASTIBOT_FORWARD_ID | Telegram group id where to forward checkpoint answers |
| BOT_CONTACT_PERSON | Contact info for /help command, optional|

For example, if you have a postgres docker container with name "postgres" in network "network": 

`docker run -d --network=NETWORK -e RASTIBOT_KEY="5249229291:AAFvANUsM1hnBJZBHLOjiAR5YBauAcGJlWw" -e RASTIBOT_FORWARD_ID="-1001956004884" -e BOT_CONTACT_PERSON="Contact person" retkihaastebot`

I used PostgreSQL database, but any other might work as well.

## Data
Some stuff should be changed from config/config.py

"@retkihaastebot"'s bot_token, and 2023 chat's ID:

TOKEN= "5249229291:AAFvANUsM1hnBJZBHLOjiAR5YBauAcGJlWw"

CHAT FORWARD ID = "-1001956004884" 

`docker run -d -e RASTIBOT_KEY="5249229291:AAFvANUsM1hnBJZBHLOjiAR5YBauAcGJlWw" -e RASTIBOT_FORWARD_ID="-1001956004884" retkihaaste`


* `docker run --network=NETWORK" --name="postgres" -e POSTGRES_PASSWORD="password" postgres`

	-Ajaa postgres-tietokannan salasanalla password ja nimellä postgres
	
	- --rm poistaa tän sulkemisen jälkee


** Step by step windows powershellil: **
## (aja vaiheet 1-2 Vaan kerran alussa, 3 sen jälkeen kun teki jotain muutoksia koodiin. 4-5 sillon ku ne ei pyöri heh) ##
 
1. `docker pull postgres:alpine` 
	- pitäis ilmestyy Docker desktopin imageihin
	
2. `docker network create NETWORK` 
	- vastaa jollai random stringil
		
3. `docker build --tag="retkitesti .`
	- Pitäis ilmestyy imageihin
	- Muista olla siel projektin kansios
	
4. `docker run --name postgres --network=NETWORK -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine`
	- Container pitäis syttyy vihreeks Docker desktopis
	
5. `docker run -d --network=NETWORK -e RASTIBOT_FORWARD_ID="-1001956004884" -e RASTIBOT_KEY="1532113577:AAEZpppBtNT4BoUux8LkdAVjSEesscTKJWQ" retkihaaste`
	-Aja itse botti

Voila! botin pitäis vastailla



