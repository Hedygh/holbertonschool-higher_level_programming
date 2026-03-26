def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template

        placeholders = {
            "name": attendee.get("name"),
            "event_title": attendee.get("event_title"),
            "event_date": attendee.get("event_date"),
            "event_location": attendee.get("event_location")
        }

        for key, value in placeholders.items():
            replacement = str(value) if value is not None else "N/A"
            output = output.replace("{" + key + "}", replacement)

        file_name = f"output_{index}.txt"

        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(output)
        except OSError as error:
            print(f"Error writing {file_name}: {error}")