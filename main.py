import csv
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import json

COUNTRY_ABBREVIATIONS = {
    "Argentina": "ARG",
    "Canada": "CAN",
    "Peru": "PER",
    "Chile": "CHI",
    "Ecuador": "ECU",
    "Venezuela": "VEN",
    "Mexico": "MEX",
    "Jamaica": "JAM",
    "Estados Unidos": "USA",
    "Bolivia": "BOL",
    "Uruguay": "URU",
    "Panama": "PAN",
    "Colombia": "COL",
    "Paraguay": "PAR",
    "Brasil": "BRA",
    "Costa Rica": "CRC",
}


def replace_countries_with_abbreviations(text):
    for country, abbreviation in COUNTRY_ABBREVIATIONS.items():
        text = text.replace(country, abbreviation)
    return text


def main():

    matches_path = "fixture.json"
    calendar_path = "copa_america_2024.ics"

    # new calendar
    cal = Calendar()

    # load matches file
    with open(matches_path) as json_file:
        matches = json.load(json_file)

    for match in matches:
        # Especify the event

        datetime_start = datetime.strptime(match["fecha_inicio"], "%Y-%m-%d %H:%M")
        datetime_end = datetime_start + timedelta(hours=2)
        summary = replace_countries_with_abbreviations(match["partido"])

        event = Event()
        event.add("summary", summary)
        event.add("dtstart", datetime_start)
        event.add("dtend", datetime_end)
        event.add("location", match["estadio"])

        # Add match to calendar
        cal.add_component(event)

        # Save the content to an .ics file
        with open(calendar_path, "w") as f:
            f.write(cal.to_ical().decode("utf-8"))


if __name__ == "__main__":
    main()
