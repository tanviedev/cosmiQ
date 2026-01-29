# app/astrology/report_formatter.py

def format_drishti_report(interpretations):
    print("\n--- DRISHTI INTERPRETATION ---\n")

    for item in interpretations:
        print(
            f"{item['from']} aspects {item['to']} → "
            f"{item['meaning']}"
        )
