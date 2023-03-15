import os

config = {
}

config["key"] = os.environ["RASTIBOT_KEY"]
config["forwardId"] = int(os.environ["RASTIBOT_FORWARD_ID"])
# These 2 are not required
config["botContactPerson"] = os.environ.get("BOT_CONTACT_PERSON") or ""
config["help"] = ". For help with anything else, please ask in the TrekChallenge Telegram group."
