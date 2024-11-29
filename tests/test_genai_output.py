from genai_app.genai_output import get_genai_output
from genai_app.config import SCENARIOS

def test_get_genai_output_valid():
    """
    Test `get_genai_output` for valid scenarios.
    """
    for scenario_id in SCENARIOS.keys():
        output = get_genai_output(scenario_id)
        assert output == SCENARIOS[scenario_id]

def test_get_genai_output_invalid():
    """
    Ensure `get_genai_output` raises ValueError for invalid scenarios.
    """
    invalid_id = max(SCENARIOS.keys()) + 1
    try:
        get_genai_output(invalid_id)
        assert False, "get_genai_output did not raise ValueError for invalid ID."
    except ValueError:
        assert True
