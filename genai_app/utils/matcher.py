# app/utils/matcher.py

from fuzzy_match import match
from genai_app.utils.logger import logger

def infer_key(k, v, choices, method, threshold):
    """
    Infer the correct key and value from the GenAI output using lexical matching.
    """
    try:
        if k in choices:
            # Recognized key: Perform value matching
            fixed_value, score = match.extract(v, choices[k], match_type=method)[0]
            return k, fixed_value, score, None
        else:
            # Unrecognized key: Infer key and value
            possible_output = {
                k_possible: match.extract(v, choices[k_possible], match_type=method)[0]
                for k_possible in choices.keys()
            }
            best_k, (best_v, score) = sorted(possible_output.items(), key=lambda item: item[1][1], reverse=True)[0]
            return best_k, best_v, score, k
    except Exception as e:
        logger.error(f"Error during key-value inference: {e}")
        raise
