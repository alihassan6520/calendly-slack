# Calendly Slack Integration using DigitalOcean Cloud Functions (Python)

This project integrates **Calendly** with **Slack** by sending messages to a Slack channel whenever a Calendly event occurs. It uses **DigitalOcean Cloud Functions** to listen for webhooks from Calendly and send notifications to Slack.

## Features

- **Calendly Webhook Integration**: Listens for events from Calendly (e.g., event creation, cancellations, etc.).
- **Slack Notifications**: Sends a formatted message to a specified Slack channel upon event creation.
- **Serverless with DigitalOcean Functions**: Deploys the application as a serverless function on DigitalOcean to handle webhook requests efficiently.

## Prerequisites

Before you start, ensure you have the following:

- A **Calendly account** with access to the Calendly API and webhook feature.
- A **Slack workspace** and an incoming webhook URL for sending messages to a Slack channel.
- A **DigitalOcean account** to deploy serverless functions.
- **Python 3.8+** installed locally for local development.
- **`pip`** for installing Python dependencies.

## Features

- **Calendly Webhook Integration**: Set up a webhook to listen to various events (e.g., `event_created`, `event_canceled`).
- **Slack Notifications**: Send formatted messages to a Slack channel with event details.
- **Serverless Deployment**: Deploy the integration to DigitalOcean Cloud Functions for scalable, event-driven processing.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/calendly-slack-integration.git
cd calendly-slack-integration


