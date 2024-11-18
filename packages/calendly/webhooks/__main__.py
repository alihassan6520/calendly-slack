import os
import json
import requests
from http import HTTPStatus
from urllib.parse import parse_qs
from datetime import datetime
import pytz

def main(args):
    # Access the body of the HTTP request
    payload = args.get("payload", {})
    
    # Extract event details from the Calendly webhook payload
    try:
        invitee_name = payload.get("name", "Unknown Invitee")
        event_status = payload.get("status", "unknown")
        invitee_email = payload.get("email", "Unknown Email")
        event_location = payload.get("scheduled_event", {}).get("location", "Unknown Event")
        event_location_url = event_location.get("join_url", "")
        start_time = payload.get("scheduled_event", {}).get("start_time", "Unknown Date")
        end_time = payload.get("scheduled_event", {}).get("end_time", "Unknown Date")
        host_name = payload.get("scheduled_event", {}).get("event_memberships", [{}])[0].get("user_name", "Unknown Host")
    except KeyError as e:
        print(f"Key error: {e}")
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": json.dumps({"error": "Invalid payload structure"})
        }

    # Slack Webhook URL from environment variable
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')

    start_time_utc = datetime.fromisoformat(start_time[:-1])  
    end_time_utc = datetime.fromisoformat(end_time[:-1])
    
    eastern = pytz.timezone('America/New_York')
    start_time_local = start_time_utc.astimezone(eastern)
    end_time_local = end_time_utc.astimezone(eastern)

    # Format the dates
    formatted_start_time = start_time_local.strftime("%a %b %d, %Y %I%M %p")  # Mon Sep 23, 2024 05:00 PM
    formatted_end_time = end_time_local.strftime("%I%M %p")  # 05:30 PM

    # Combine formatted times
    final_date_string = f"{formatted_start_time} – {formatted_end_time} (EDT)"
    
    if event_status == "active":
        message = {
            "text": (
                f"Event: *{invitee_name}* and *{host_name}*\n"
                f"Date: {final_date_string}\n"
                f"Where: {event_location_url}\n"
                f"Email: {invitee_email}"
            )
        }
    elif event_status == "canceled":
        message = {
            "text": (
                f"Event Canceled: *{invitee_name}* and *{host_name}*\n"
                f"Date: {final_date_string}\n"
                f"Where: {event_location_url}\n"
                f"Email: {invitee_email}"
            )
        }

    # Send a POST request to Slack
    response = requests.post(
        slack_webhook_url,
        data=json.dumps(message),
        headers={'Content-Type': 'application/json'}
    )

    # Prepare the response
    response_body = {
        "original_body": payload,
        "slack_response_status": response.status_code,
        "slack_response_text": response.text
    }

    return {
        "statusCode": HTTPStatus.OK,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }
