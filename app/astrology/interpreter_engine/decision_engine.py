from datetime import datetime

def get_current_dasha(dashas):
    now = datetime.utcnow()

    for md in dashas:
        if md["start"] <= now <= md["end"]:
            return md["mahadasha"]

    return None


def evaluate_career_decision(chart, dashas):
    score = 0
    reasons = []

    # 🔹 1. Current Dasha
    current_dasha = get_current_dasha(dashas)

    if current_dasha in ["Jupiter", "Sun", "Mars"]:
        score += 2
        reasons.append(f"{current_dasha} Mahadasha supports action and growth")

    elif current_dasha in ["Saturn"]:
        score -= 1
        reasons.append("Saturn Mahadasha may cause delay or slow progress")

    elif current_dasha in ["Rahu", "Ketu"]:
        score -= 2
        reasons.append(f"{current_dasha} Mahadasha brings uncertainty and instability")

    # 🔹 2. 10th House Strength
    for planet, data in chart.items():
        if data.get("house") == 10:
            score += 1
            reasons.append(f"{planet} in 10th house supports career focus")

    # 🔹 3. Saturn Influence (delay factor)
    if "Saturn" in chart and chart["Saturn"]["house"] == 7:
        score -= 1
        reasons.append("Saturn influence indicates delays in external opportunities")

    # 🔹 4. Final Decision
    if score >= 2:
        decision = "YES"
        confidence = "High"
    elif score >= 0:
        decision = "WAIT"
        confidence = "Medium"
    else:
        decision = "NO"
        confidence = "Low"

    return {
        "decision": decision,
        "confidence": confidence,
        "score": score,
        "reasons": reasons
    }