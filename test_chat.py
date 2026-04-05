from app.full_chart_pipeline import generate_full_chart
from app.llm.interpreters.astro_agent import ask_cosmiq


if __name__ == "__main__":

    # ---------------- FULL PIPELINE ----------------

    data = generate_full_chart(
        dob="2005-10-01",
        time="15:57:00",
        timezone="Asia/Kolkata",
        lat=19.0760,
        lon=72.8777
    )

    chart = data["chart"]
    drishti = data["drishti"]
    dashas = data["dashas"]

    # ---------------- PRINT CHART ----------------

    print("\n--- VEDIC BIRTH CHART ---\n")

    for p, d in chart.items():
        print(
            f"{p:10} | "
            f"Sign: {d['sign']:11} | "
            f"Deg: {d['degree']:5} | "
            f"House: {d['house']:2} | "
            f"Nakshatra: {d['nakshatra']:15} | "
            f"Pada: {d['pada']} | "
            f"Lord: {d['nakshatra_lord']}"
        )

    # ---------------- DRISHTI ----------------

    print("\n--- GRAHA DRISHTI (ASPECTS) ---\n")

    for line in drishti:
        print(
            f"{line['from']} → {line['to']} | {line['meaning']}"
        )

    # ---------------- DASHAS ----------------

    print("\n--- VIMSHOTTARI DASHA ---\n")

    for md in dashas:
        print(
            f"{md['mahadasha']} | "
            f"{md['start'].date()} → {md['end'].date()}"
        )

    # ---------------- CHATBOT ----------------

    print("\n--- cosmiQ AI CHAT ---\n")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Ask: ")

        if question.lower() == "exit":
            print("\nGoodbye 🌙")
            break

        try:
            response = ask_cosmiq(question, chart, dashas)

            print("\n--- Answer ---\n")
            print(response)
            print("\n----------------\n")

        except Exception as e:
            print("\n⚠️ Error:", e, "\n")