import json
import urllib.request
import time
from genai_app.config import CACHE_TIMEOUT, CACHED_CHOICES, CACHE_TIMESTAMP, CHOICES_URL
from genai_app.utils.logger import logger


def get_choice_data():
    """
    Fetch choice data with caching mechanism.

    Returns:
        dict: Valid key-value options.
    """
    global CACHED_CHOICES, CACHE_TIMESTAMP
    current_time = time.time()

    if CACHED_CHOICES is None or (current_time - CACHE_TIMESTAMP) > CACHE_TIMEOUT:
        logger.info("Fetching fresh data from the HTTP endpoint...")
        try:
            with urllib.request.urlopen(CHOICES_URL) as response:
                CACHED_CHOICES = json.loads(response.read().decode())
                CACHE_TIMESTAMP = current_time
            logger.info("Choices data retrieved successfully.")
        except urllib.error.URLError as e:
            logger.error(f"Failed to fetch choices data: {e}")
            raise RuntimeError("Failed to fetch choices data.")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {e}")
            raise ValueError("Invalid JSON format.")
    else:
        logger.info("Using cached data.")
    return CACHED_CHOICES


def preprocess_choices(choices, matcher):
    """
    Preprocess choices for fast lookups.

    Args:
        choices (dict): Valid key-value options.
        matcher (function): Matching function.

    Returns:
        dict: Preprocessed choices with scores.
    """
    logger.info("Preprocessing choices...")
    preprocessed = {}
    for key, values in choices.items():
        preprocessed[key] = {
            value: matcher(value, values)[0][1] for value in values
        }
        logger.debug(f"Preprocessed {key} with {len(values)} values.")
    logger.info("Preprocessed all choices successfully.")
    return preprocessed
