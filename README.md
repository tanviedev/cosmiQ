🌌 cosmiQ — AI-Powered Vedic Astrology System

cosmiQ is a hybrid AI system that combines deterministic astrological engines with LLM-based interpretation to generate evidence-backed, non-hallucinated insights from a user’s birth chart.

Unlike typical astrology apps, cosmiQ is designed to be:

🔍 Transparent → Every answer is backed by explicit astrological reasoning
🧠 Safe AI → LLMs do not make decisions, only explain engine outputs
⚙️ Modular → Independent engines for chart, aspects, dashas, reasoning
🚀 Extensible → Built for future agents, dashboards, and real-world use
🧠 Core Philosophy

❗ LLMs should not think — they should explain

cosmiQ strictly separates:

🔹 Deterministic Engine (Truth Layer)

Computes:
Birth chart
Houses
Nakshatras
Aspects (Drishti)
Dispositors
Vimshottari Dasha

Produces numerical + categorical facts

🔹 LLM Layer (Language Layer)
Converts structured reasoning into human-readable answers
Cannot hallucinate (strict prompt guardrails)


🏗️ System Architecture

User Question
      ↓
Intent Detection (LLM / rule-based)
      ↓
Reasoning Engine (deterministic)
      ↓
Decision Engine (YES / NO / WAIT)
      ↓
Prompt Builder
      ↓
LLM (formatting only)
      ↓
Final Answer (with proof)


📂 Project Structure

cosmiQ/
│
├── app/
│   ├── astrology/
│   │   ├── birth_chart.py
│   │   ├── nakshatra.py
│   │   ├── rasi_lords.py
│   │
│   │   ├── drishtiEngine/
│   │   │   ├── aspects.py
│   │   │   ├── drishti_interpreter.py
│   │   │   ├── report_formatter.py
│   │
│   │   ├── dispositorEngine/
│   │   │   ├── chart_enricher.py
│   │
│   │   ├── vimshottariEngine/
│   │   │   ├── mahadasha.py
│   │
│   │   ├── interpreter_engine/
│   │   │   ├── reason_builder.py
│   │
│   ├── llm/
│   │   ├── astro_agent.py
│   │   ├── llm_client.py
│   │   ├── prompt_builder.py
│   │   ├── guardrails.py
│   │   ├── intent_mapper.py
│   │   ├── prompts/
│   │   │   └── base.txt
│   │
│   ├── utils/
│   │   ├── time_utils.py
│
├── test1.py  # Chart generation
├── test2.py  # Drishti interpretation
├── test4.py  # Vimshottari Dasha
├── test_chat.py  # AI chatbot interface


⚙️ Features

🪐 1. Birth Chart Engine
Calculates:
Planetary positions
Signs & degrees
Houses (Placidus / Vedic style)
Nakshatra + Pada
Adds Ascendant dynamically

🔭 2. Graha Drishti (Aspects Engine)
Computes:
Planet-to-planet aspects
House aspects
Interprets meanings:
e.g.
Moon → Rahu → mental restlessness

🔗 3. Dispositor Engine
Tracks:
Sign lord chain
Adds strength hints:
kendra, trikona, dusthana

⏳ 4. Vimshottari Dasha Engine
Computes:
Mahadasha sequence
Timeline (start → end)
Correctly aligned with Moon Nakshatra

🧠 5. Reasoning Engine (Core Intelligence)

Transforms chart into structured reasoning:
Example:
- Moon in Leo house 8 → emotional intensity
- Rahu in Pisces house 3 → mental amplification
- Current Mahadasha: Moon

⚖️ 6. Decision Engine

Evaluates real-life questions:

{
  "decision": "WAIT",
  "confidence": "Medium",
  "score": 1,
  "reasons": [...]
}

Supports:

Career timing
Opportunities
Emotional states

🤖 7. LLM Layer (Guarded AI)
Uses strict prompts
No hallucination allowed
Converts reasoning → explanation

Example Output:

1. Direct Answer:
WAIT

2. Explanation:
- Current Mahadasha: Rahu → uncertainty
- Saturn in 7th → delays
- Venus in 10th → career support exists

🚨 8. Guardrails

Prevents:

Unsupported questions
Guessing
Over-generalization

If no data:

Insufficient astrological basis to answer this.


🧪 Running the Project
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Core Modules
🔹 Birth Chart
python test1.py
🔹 Drishti
python test2.py
🔹 Dasha
python test4.py
4️⃣ Run AI Chat
python test_chat.py
🔑 LLM Setup

You can use:

Option 1: OpenAI
setx OPENAI_API_KEY "your_key_here"
Option 2: Groq (Free)

Update model in llm_client.py:

model="llama-3.1-8b-instant"
💬 Example Queries
What is influencing my overthinking?
When should I apply for internships?
How is my love life right now?
🚀 Future Roadmap
🔥 AI Enhancements
LLM-based intent detection ✅ (in progress)
Memory-based conversation
Multi-turn reasoning
📊 Data & Visualization
Real-time transit tracking
User-specific dashboards
🌍 Product Vision
Astrology assistant for decision support
Not prediction → guided reasoning system
⚠️ Disclaimer

cosmiQ is designed as a decision-support system, not a deterministic predictor.

It does not guarantee outcomes
It provides structured astrological reasoning
Final decisions remain with the user
🏆 Key Highlights (For Recruiters)
Built hybrid AI system (rule-based + LLM)
Designed guardrailed LLM architecture
Implemented modular reasoning pipelines
Focused on interpretability & safety
Avoided hallucination via strict prompt design
👩‍💻 Author

Tanvi Takle

⭐ Final Note

This project is not just an astrology tool.

It is an experiment in building safe, interpretable AI systems where:

Logic comes first, language comes second.