#!/usr/bin/python3

import os

def generate_invitations(template_content, attendees):

        if not isinstance(template_content, str):
                print("Error: template_content must be a string.")
                return

        if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
                print("Error: attendees must be a list of dictionaries.")
                return

        if template_content is None or attendees is None:
                print("Error: Missing template or attendees list.")
                return

        for index, attendee in enumerate(attendees, start=1):
                invitation_content = template_content.format(
                        name=attendee.get("name", "N/A"),
                        event_title=attendee.get("event_title", "N/A"),
                        event_date=attendee.get("event_date", "N/A"),
                        event_location=attendee.get("event_location", "N/A")
                )
                
                filename = f"output_{index}.txt"
                
                with open(filename, 'w', encoding="utf-8") as file:
                        file.write(invitation_content)
                print(f"Invitation générée pour : {attendee.get('name')} dans le fichier {filename}")