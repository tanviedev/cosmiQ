from app.full_chart_pipeline import generate_full_chart

if __name__ == "__main__":

    data = generate_full_chart(
        dob="2005-10-01",
        time="15:57:00",
        timezone="Asia/Kolkata",
        lat=19.0760,
        lon=72.8777
    )

    print("\n--- CHART ---\n")
    for p, d in data["chart"].items():
        print(p, d)

    print("\n--- DRISHTI ---\n")
    for line in data["drishti"]:
        print(line)

    print("\n--- DASHAS ---\n")
    for md in data["dashas"]:
        print(md["mahadasha"], md["start"], md["end"])