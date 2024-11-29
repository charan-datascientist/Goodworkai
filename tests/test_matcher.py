from genai_app.utils.matcher import infer_key

def test_infer_key_recognized_key():
    """
    Test `infer_key` for recognized keys.
    """
    choices = {"State": ["State_1", "State_2"]}
    k, v, score, orig_k = infer_key("State", "State_1", choices, "jaro_winkler", 0.9)
    assert k == "State"
    assert v == "State_1"
    assert score >= 0.9
    assert orig_k is None

def test_infer_key_unrecognized_key():
    """
    Test `infer_key` for unrecognized keys.
    """
    choices = {"State": ["State_1", "State_2"]}
    k, v, score, orig_k = infer_key("Region", "State_1", choices, "jaro_winkler", 0.9)
    assert k == "State"
    assert v == "State_1"
    assert orig_k == "Region"
