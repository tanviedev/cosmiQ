# app/astrology/drishti_rules.py
"""
Classical Graha Drishti Interpretation Rules
--------------------------------------------
These meanings are based on traditional Vedic astrology principles.
They describe how the ASPECTING planet modifies the ASPECTED planet.
Sign, house, dignity, conjunctions are applied later as modifiers.
"""

DRISHTI_RULES = {

    "Sun": {
        "general": (
            "authority, vitality, ego, self-expression, leadership, father, soul purpose"
        ),
        "effects": {
            "Moon": (
                "conflict between ego and emotions, sense of duty overriding emotional needs, "
                "strong desire to lead emotionally, fluctuating inner confidence"
            ),
            "Mars": (
                "high ambition, assertive leadership, competitive spirit, courage backed by authority, "
                "potential dominance or authoritarian tendencies"
            ),
            "Mercury": (
                "sharp intellect with ego involvement, authoritative speech, strong opinions, "
                "risk of intellectual arrogance"
            ),
            "Jupiter": (
                "righteous leadership, moral authority, mentor-like personality, strong ethical stance"
            ),
            "Venus": (
                "ego involvement in relationships, desire for admiration in love, artistic pride"
            ),
            "Saturn": (
                "struggle between authority and discipline, delayed recognition, responsibility-heavy leadership"
            ),
            "Rahu": (
                "obsession with status, fame-seeking behavior, distorted self-image"
            ),
            "Ketu": (
                "detached ego, spiritual authority, reduced worldly ambition"
            )
        }
    },

    "Moon": {
        "general": (
            "mind, emotions, intuition, nurturing, adaptability, psychological well-being"
        ),
        "effects": {
            "Sun": (
                "emotional dependence on authority figures, fluctuating confidence, need for validation"
            ),
            "Mars": (
                "emotionally reactive behavior, impulsive decisions, emotional courage or anger"
            ),
            "Mercury": (
                "high emotional intelligence, communicative sensitivity, overthinking tendencies"
            ),
            "Jupiter": (
                "emotionally wise, nurturing teacher-like mindset, optimistic emotional nature"
            ),
            "Venus": (
                "romantic sensitivity, emotional attachment in relationships, artistic imagination"
            ),
            "Saturn": (
                "emotional restraint, seriousness, maturity through hardship, reserved emotional expression"
            ),
            "Rahu": (
                "mental restlessness, anxiety, emotional confusion, unconventional emotional patterns"
            ),
            "Ketu": (
                "emotional detachment, introspection, withdrawal from emotional dependency"
            )
        }
    },

    "Mars": {
        "general": (
            "energy, action, courage, aggression, initiative, physical vitality"
        ),
        "effects": {
            "Sun": (
                "militant leadership, strong willpower, desire to command and dominate"
            ),
            "Moon": (
                "emotional volatility, impulsive reactions, anger-driven decisions"
            ),
            "Mercury": (
                "sharp speech, argumentative intelligence, technical or engineering mindset"
            ),
            "Jupiter": (
                "righteous action, ethical warrior mentality, protection of beliefs"
            ),
            "Venus": (
                "passionate relationships, intense desires, conflict in love matters"
            ),
            "Saturn": (
                "frustrated energy, delayed action, disciplined aggression, endurance through struggle"
            ),
            "Rahu": (
                "reckless actions, obsession-driven aggression, risk-taking behavior"
            ),
            "Ketu": (
                "withdrawn aggression, spiritualized energy, internalized anger"
            )
        }
    },

    "Mercury": {
        "general": (
            "intellect, communication, logic, analysis, commerce, adaptability"
        ),
        "effects": {
            "Sun": (
                "authoritative speech, strong opinions, leadership through communication"
            ),
            "Moon": (
                "emotionally intelligent communication, fluctuating thought patterns"
            ),
            "Mars": (
                "sharp tongue, debating skills, argumentative nature"
            ),
            "Jupiter": (
                "philosophical thinking, teaching ability, scholarly communication"
            ),
            "Venus": (
                "artistic communication, poetic speech, charm in expression"
            ),
            "Saturn": (
                "serious thinking, methodical speech, cautious communication"
            ),
            "Rahu": (
                "manipulative speech, clever deception, unconventional ideas"
            ),
            "Ketu": (
                "introverted thinking, research-oriented mind, minimal speech"
            )
        }
    },

    "Jupiter": {
        "general": (
            "wisdom, expansion, ethics, protection, teachers, fortune, guidance"
        ),
        "effects": {
            "Sun": (
                "wise leadership, moral authority, respected mentor figure"
            ),
            "Moon": (
                "emotional wisdom, nurturing counselor, optimistic mindset"
            ),
            "Mars": (
                "ethical action, protection of dharma, disciplined courage"
            ),
            "Mercury": (
                "scholarly intellect, teaching abilities, philosophical reasoning"
            ),
            "Venus": (
                "balanced relationships, value-based love, generosity in affection"
            ),
            "Saturn": (
                "structured belief system, practical wisdom, conservative philosophy"
            ),
            "Rahu": (
                "misguided beliefs, exaggerated optimism, distorted moral compass"
            ),
            "Ketu": (
                "spiritual wisdom, detachment from material teaching, moksha orientation"
            )
        }
    },

    "Venus": {
        "general": (
            "love, relationships, beauty, comfort, luxury, art, pleasure"
        ),
        "effects": {
            "Sun": (
                "desire for admiration in love, ego-driven relationships"
            ),
            "Moon": (
                "emotional romance, nurturing love, strong attachment tendencies"
            ),
            "Mars": (
                "intense passion, sexual magnetism, volatile relationships"
            ),
            "Mercury": (
                "charming speech, flirtation, artistic communication"
            ),
            "Jupiter": (
                "moral values in relationships, respectful partnerships"
            ),
            "Saturn": (
                "delayed relationships, seriousness in love, karmic partnerships"
            ),
            "Rahu": (
                "unconventional relationships, intense desires, obsession with pleasure"
            ),
            "Ketu": (
                "detachment from sensual pleasure, spiritualized love"
            )
        }
    },

    "Saturn": {
        "general": (
            "discipline, delay, responsibility, karma, endurance, structure"
        ),
        "effects": {
            "Sun": (
                "humbling of ego, delayed authority, responsibility-heavy leadership"
            ),
            "Moon": (
                "emotional maturity through hardship, emotional restraint"
            ),
            "Mars": (
                "controlled aggression, delayed action, perseverance through obstacles"
            ),
            "Mercury": (
                "serious intellect, cautious speech, methodical thinking"
            ),
            "Jupiter": (
                "conservative wisdom, disciplined belief system, slow spiritual growth"
            ),
            "Venus": (
                "delayed love, karmic relationships, seriousness in pleasure"
            ),
            "Rahu": (
                "fear-driven obsession, anxiety about stability, karmic ambition"
            ),
            "Ketu": (
                "detachment through hardship, isolation leading to wisdom"
            )
        }
    },

    "Rahu": {
        "general": (
            "obsession, illusion, amplification, material hunger, unconventional paths"
        ),
        "effects": {
            "Sun": (
                "obsession with fame, distorted identity, hunger for recognition"
            ),
            "Moon": (
                "emotional instability, anxiety, mental amplification"
            ),
            "Mars": (
                "reckless aggression, impulsive risk-taking"
            ),
            "Mercury": (
                "manipulative intelligence, clever deception, unconventional thinking"
            ),
            "Jupiter": (
                "distorted guidance, false teachers, over-ambition"
            ),
            "Venus": (
                "intense desires, taboo relationships, indulgence"
            ),
            "Saturn": (
                "fear of instability, obsessive control, karmic pressure"
            ),
            "Ketu": (
                "identity confusion, sudden detachment cycles"
            )
        }
    },

    "Ketu": {
        "general": (
            "detachment, isolation, spirituality, moksha, past-life mastery"
        ),
        "effects": {
            "Sun": (
                "detached ego, spiritual authority, loss of worldly ambition"
            ),
            "Moon": (
                "emotional withdrawal, introspection, spiritual sensitivity"
            ),
            "Mars": (
                "withdrawn aggression, internalized energy, ascetic discipline"
            ),
            "Mercury": (
                "research-oriented intellect, silence, intuitive thinking"
            ),
            "Jupiter": (
                "spiritual wisdom, moksha orientation, detachment from doctrine"
            ),
            "Venus": (
                "disinterest in sensual pleasure, refined spiritual love"
            ),
            "Saturn": (
                "detachment through hardship, isolation leading to enlightenment"
            ),
            "Rahu": (
                "sudden breaks from obsession, karmic release cycles"
            )
        }
    }
}
