📘 cosmiQ

cosmiQ — A Python-based Vedic astrology engine and toolkit for computing birth charts with sidereal planetary positions, houses, nakshatras, padas, and aspects. This project lays a strong foundation for deeper astrological interpretation and AI-assisted readings.

🧠 Overview

This repository implements a core Vedic astrology computation engine:

Computes sidereal planetary positions (Lahiri ayanamsa).

Assigns whole-sign houses.

Calculates nakshatra and pada for planets.

Computes Vedic Drishti (aspects).

Provides a scaffold for AI/LLM-based natural language interpretation.

The intent is to separate mathematical astrology from explanatory text, enabling interpretive layers (via fuzzy logic or LLM) to be added later.

📦 Repository Structure
cosmiQ/
├── app/
│   ├── astrology/
│   │   ├── birth_chart.py        # Core chart math and houses
│   │   ├── nakshatra.py          # Nakshatra and pada logic
│   │   └── aspects.py            # Vedic drishti (planetary aspects)
│   └── llm/                     # LLM/AI scaffolding (prompt builders, client)
├── test1.py                     # Example: generate and display birth chart
├── test2.py                     # Example: integrate with LLM interpreter
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md                    # (You’re reading the improved version!)


There are no descriptions or topics currently set in the repo.

🚀 Features (Implemented)
🪐 Chart Computation Engine

Sidereal planetary positions using Swiss Ephemeris (pyswisseph).

Accurate handling of lunar nodes (Rahu/Ketu).

Whole-sign house assignments.

Ascendant (Lagna) calculation.

🌟 Nakshatra System

27 Nakshatras (star constellations).

4 Padas each (3°20′ segments).

Nakshatra lord identification.

These are computed for every planet and the ascendant.

👁️ Vedic Drishti Module

Classical aspects (as per Parāśari):

Planet	7th Aspect	Special Aspects
Sun	Yes	None
Moon	Yes	None
Mars	Yes	4th & 8th houses
Mercury	Yes	None
Jupiter	Yes	5th & 9th houses
Venus	Yes	None
Saturn	Yes	3rd & 10th houses
Rahu	Yes	5th & 9th houses (traditionally)
Ketu	Yes	5th & 9th houses (traditionally)

This module computes which houses and planets each graha aspects based on the chart.

📥 Installation

Clone the repository and install dependencies:

git clone https://github.com/tanviedev/cosmiQ.git
cd cosmiQ
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

📌 Usage
📊 Generate a Birth Chart

Run:

python test1.py


This prints:

Sign

Degree

House

Nakshatra

Pada

Nakshatra lord for each planet and Ascendant

🤖 LLM Interpretation (Optional)

test2.py shows how chart data can be fed into an LLM (like OpenAI’s API) for natural language reading. However, to use this you must set your API key:

export OPENAI_API_KEY="your_key_here"


or in Windows PowerShell:

setx OPENAI_API_KEY "your_key_here"

🚧 What’s Missing (Planned / Future)

The core engine works, but currently the repo does not implement:

Dasha systems (Vimshottari Mahadasha/Antardasha)

Yoga detection

Predictive interpretation rules

Frontend or API server

Persistent storage or database

These are natural candidates for the next phases of development.

🎯 Next Development Ideas

Based on the current state, you could build:

Vimshottari Dasha engine

Yogas & Significators

Fuzzy logic interpretation layer

FastAPI backend & REST endpoints

Interactive chart visualization

🛠 Contributing

Contributions are welcome! Suggested areas:

Extend the LLM prompt templates

Add yoga detection and interpretation

Build an API or GUI interface

Improve test coverage

📜 License

Check requirements.txt and file headers — no explicit LICENSE file is present. Consider adding a license (MIT, Apache, etc.).

📌 Summary

cosmiQ is a minimal but extendable Vedic astrology engine, correctly implementing sidereal calculations, whole-sign houses, nakshatras, and drishti logic. You can use it as a backend for astrology apps, AI chatbots, or research tools.
