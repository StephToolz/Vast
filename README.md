# 🛠️ Project Overview
This project is a simple Python-based automation tool designed to send periodic "+rep" messages to a specific Discord channel using Discord Webhooks.
By utilizing the same technology found in the Image Logger project
, this bot sends custom payloads to a server-side endpoint, allowing for automated feedback or messaging.
**Key Features**
Webhook Integration: Uses Discord's official webhook API for sending messages
.
Randomized Messages: Selects from a list of common "rep" terms (e.g., legit, fast, trusted).
Scheduled Intervals: Automated to send a message every 5 minutes (or a custom interval).
# 📂 Repository Structure
Based on the deployment standards for Python projects
, your repository should look like this:
/api
rep_bot.py (The main logic)
requirements.txt (Necessary Python libraries)
README.md (This documentation)
# 🚀 Setup & Deployment
1. Discord Webhook Setup
To allow the bot to send messages, you need to create a webhook in your Discord server
:
Go to Server Settings > Integrations.
Click Create Webhook.
Copy the Webhook URL and paste it into your rep_bot.py file.
**2. Deployment on Vercel**
To keep the bot running (as described in sources for web-hosted scripts
):
Connect your GitHub account to Vercel.
Import this repository.
_Note: Since Vercel is primarily for serverless functions
, you may need a trigger or a persistent environment (like a VPS) to ensure the 5-minute loop runs indefinitely without timing out._
