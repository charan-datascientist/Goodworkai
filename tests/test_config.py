from genai_app.config import CONFIG, SCENARIOS

def test_config_keys():
    """
    Ensure required keys exist in CONFIG.
    """
    assert "matching_method" in CONFIG
    assert "threshold" in CONFIG
    assert CONFIG["threshold"] > 0

def test_scenarios_structure():
    """
    Validate the structure of SCENARIOS.
    """
    for scenario_id, scenario_data in SCENARIOS.items():
        assert isinstance(scenario_id, int)
        assert isinstance(scenario_data, dict)
