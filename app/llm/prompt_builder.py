from pathlib import Path

PROMPT_DIR = Path(__file__).parent / "prompts"

def load_prompt(name: str) -> str:
    return (PROMPT_DIR / name).read_text(encoding="utf-8")

def build_prompt(template_name: str, data: dict) -> str:
    template = load_prompt(template_name)
    return template.format(**data)