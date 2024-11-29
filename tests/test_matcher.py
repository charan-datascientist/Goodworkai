from fuzzy_match import match
from genai_app.utils.matcher import infer_key

def test_infer_key_recognized_key():
    """
    Test infer_key for recognized key with high confidence.
    """
    value = "State_1"
    choices = ["State_1", "State_2", "State_3"]
    method = "jaro_winkler"
    threshold = 0.9
    best_match, score = infer_key(value, choices, method, threshold)
    assert best_match == "State_1"
    assert score >= threshold

def test_infer_key_partial_match():
    """
    Test infer_key for partial match with valid choices.
    """
    value = "Stat_1"
    choices = ["State_1", "State_2", "State_3"]
    method = "jaro_winkler"
    threshold = 0.7
    best_match, score = infer_key(value, choices, method, threshold)
    assert best_match == "State_1"
    assert threshold <= score < 1.0

def test_infer_key_low_confidence():
    """
    Test infer_key with a value that doesn't meet the threshold.
    """
    value = "Stat_X"
    choices = ["State_1", "State_2", "State_3"]
    method = "jaro_winkler"
    threshold = 0.8
    best_match, score = infer_key(value, choices, method, threshold)
    assert score < threshold





