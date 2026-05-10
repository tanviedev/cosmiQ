import json
import os


# ============================================
# KB DIRECTORY
# ============================================

BASE_DIR = os.path.dirname(__file__)

KB_DIR = os.path.join(BASE_DIR, "kb")


# ============================================
# LOAD JSON FILE
# ============================================

def load_json(filename):

    path = os.path.join(KB_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================
# LOAD COMPLETE KB
# ============================================

def load_knowledge_base():

    kb = {
        "placements": load_json("placements.json"),
        "aspects": load_json("aspects.json"),
        "dashas": load_json("dashas.json"),
        "dispositors": load_json("dispositors.json"),
    }

    return kb