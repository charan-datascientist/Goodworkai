from fuzzy_match import match


def infer_key(value, choices, method, threshold):
    """
    Infer the best match for a given value and choices.

    Args:
        value (str): Input value to match.
        choices (list): List of valid options.
        method (str): Matching method.
        threshold (float): Confidence threshold.

    Returns:
        tuple: Best match, score.
    """
    best_match, score = match.extract(value, choices, match_type=method)[0]
    return best_match, score
