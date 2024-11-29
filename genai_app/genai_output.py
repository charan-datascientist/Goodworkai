# genai_app/genai_output.py

from genai_app.config import SCENARIOS

def get_genai_output(scenario: int):
    """
    Retrieve GenAI output for a given scenario.

    Args:
        scenario (int): Scenario ID to retrieve.

    Returns:
        dict: GenAI output data.

    Raises:
        ValueError: If the scenario does not exist.
    """
    if scenario not in SCENARIOS:
        raise ValueError(f"Scenario {scenario} is not defined.")
    return SCENARIOS[scenario]
