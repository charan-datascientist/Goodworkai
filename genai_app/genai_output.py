from genai_app.config import SCENARIOS


def get_genai_output(scenario: int):
    """
    Retrieve GenAI output for a given scenario.

    Args:
        scenario (int): Scenario ID.

    Returns:
        dict: GenAI output.

    Raises:
        ValueError: If the scenario is not defined.
    """
    if scenario not in SCENARIOS:
        raise ValueError(f"Scenario {scenario} is not defined.")
    return SCENARIOS[scenario]
