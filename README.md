# rastikiertelybot

Telegram bot that can be used to forward messages to a chat.
NOTE: Only works for python-telegram-bot versions 13.15 and under.

## Build instructions with Powershell

Navigate to project folder and build with:
`docker build --tag="retkihaaste" .`

Some environment variables are required:
|Variable name|Description|
| RASTIBOT_KEY | Telegram bot token |
| RASTIBOT_FORWARD_ID | Telegram group id where to forward checkpoint answers |

`docker run -d -e RASTIBOT_KEY="XXXXX:YYYYY" -e RASTIBOT_FORWARD_ID="-XXXXXXXXX" -e retkihaastebot`

## Data
bot_token, and chat's ID:
- TOKEN= "XXXXXXX:YYYYYYYYYYY"
- CHAT FORWARD ID = "-NUMBER" 

## Step by step windows powershellil: 
(Aja vaihe 1 aina sen jälkeen kun olet tehnyt jotain muutoksia koodiin.) 
		
1. `docker build --tag="retkitesti .`
	- Pitäis ilmestyy imageihin
	- Muista olla siel projektin kansios
	
2. `docker run -d -e RASTIBOT_FORWARD_ID="-NUMBER" -e RASTIBOT_KEY="XXXXXXXX:YYYYYYYYYY" retkihaaste`
	- Aja itse botti

Voila! botin pitäis vastailla



