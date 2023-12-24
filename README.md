# UWT (Unnamed Webhook Tool)

## Overview

UWT, short for Unnamed Webhook Tool, is a Python script that provides a command-line interface (CLI) for managing and interacting with Discord webhooks. With UWT, users can easily send messages, spam messages, delete webhooks, retrieve webhook information, change webhook information, and log out from Discord webhooks.

## Features

- **User-Friendly Interface:** UWT offers a simple and intuitive command-line interface, making it easy for users to navigate and perform various actions.

- **Webhook Operations:** UWT supports essential webhook operations such as sending messages, spamming messages, deleting webhooks, retrieving webhook information, and updating webhook details.

- **Message Types:** Users can send both regular and embedded messages to Discord channels.

- **Validation:** UWT includes validation checks for Discord webhook URLs to ensure that users are working with valid webhooks.

- **Information Retrieval:** UWT provides detailed information about a Discord webhook, including general information, user information, and source information (for channel follower webhooks).

## Dependencies

- `discord`: A Python library for interacting with the Discord API.
- `aiohttp`: An asynchronous HTTP client for making web requests.
- `asyncio`: A library for writing concurrent code using the async/await syntax.
- `pystyle`: A utility library for styling console output.

## Installation

Before using UWT, make sure you have Python installed on your system. To install the required dependencies, run the following command:

```bash
pip install discord aiohttp asyncio pystyle
```

## Usage

1. Run the UWT script:

```bash
python uwt.py
```

2. Follow the on-screen prompts to enter your Discord webhook URL and navigate through the available options.

## Options

UWT provides the following options in its main menu:

1. **Send Message:** Send a single message to the Discord webhook.

2. **Spam Message:** Spam messages to the Discord webhook.

3. **Delete Webhook:** Delete the current Discord webhook.

4. **Webhook Information:** Retrieve detailed information about the Discord webhook.

5. **Change Webhook Information:** Update the username of the Discord webhook.

6. **Logout:** Log out from the Discord webhook.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests on the [GitHub repository](https://github.com/NotJINXZ/uwt).

## License

This project is licensed under the [APACHE LICENSE, VERSION 2.0](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Disclaimer

This tool is provided for educational and experimental purposes only. Use it responsibly and in compliance with Discord's [Terms of Service](https://discord.com/terms) and [Developer Terms of Service](https://discord.com/developers/docs/legal).

---
