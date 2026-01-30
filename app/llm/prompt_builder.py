from pathlib import Path

PROMPT_DIR = Path(__file__).parent / "prompts"


def load_prompt(name: str) -> str:
    """
    Loads a prompt template from the prompts directory.
    """
    return (PROMPT_DIR / name).read_text(encoding="utf-8")


def build_prompt(template_name: str, data: dict) -> str:
    """
    Fills a prompt template using engine-provided data.
    """
    template = load_prompt(template_name)
    return template.format(**data)
