# QrCodeBot-xyZ
- This is a Discord bot that will provide a QR Code to your Axie Infinity scholars.
- This version of the bot is compatible with ronin!

- If you want to use it with Ethereum information instead:

In submitSignaure function, change "mainnet":"ronin" to "mainnet":"ethereum"

# Setup
1. Run Ubuntu on AWS ec2 instance
2. Clone the file by running:
* `git clone https://github.com/ZracheSs-xyZ/QrCodeBot-xyZ`
3. Install the requierements by running in to correct path:
* `chmod +x install-ubuntu.sh`
* `sudo ./install-ubuntu.sh`
4. Follow this tutorial to create and add a bot to your Discord Server:
* `https://discordpy.readthedocs.io/en/stable/discord.html`
5. Update the SecretStorage.py file in repo with the Token of your bot and with the information of your scholars.
6. Run the script by running in to correct path:
* `python3 ./QrCodeBot-xyZ.py`

# Step-by-step help
- Please join my Discord channel : https://discord.com/invite/837cCXPd48
- DM our Head of IT for support

# Upcoming new features
- [x] Create a QR Code Bot
- [x] Create a payout script : https://github.com/ZracheSs-xyZ/PayoutScript-xyZ
- [ ] So much more...

# bug to fix
- [x] Current time isn't displayed correcly
- [x] Fix edge case where the bot could send a wrong code
- This could've happen in extreme edge cases where a lot of scholars were asking for a code simultaniously and axie server didn't respond in a timely manner!
- This was fixed by making sure every QRCode was saved using the scholars DiscordUUID 

Please tell me if you experience any bugs...

# Donations
With your donation, I will be able to keep working on this project and add new features. 
Thank you!

* Ronin Wallet Address: ronin:a04d88fbd1cf579a83741ad6cd51748a4e2e2b6a
* Ethereum Wallet Address: 0x3C133521589daFa7213E5c98C74464a9577bEE01

# Help
If you need help with setup or you have any question, please reach out to me!

* Twitter: https://twitter.com/ZracheSs
* Discord: https://discord.com/invite/837cCXPd48
