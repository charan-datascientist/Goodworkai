# genai_app/choices.py

import json
import urllib.request
from genai_app.utils.logger import logger
import time
from functools import lru_cache
from genai_app.config import CACHE_TIMEOUT, CACHED_CHOICES, CACHE_TIMESTAMP


def get_choice_data(url):
    """
    Fetch choice data from a given URL with a timeout-based caching mechanism.

    Args:
        url (str): URL to fetch choice data.

    Returns:
        dict: Valid key-value options.

    Raises:
        RuntimeError: If data cannot be fetched.
        ValueError: If JSON is invalid.
    """
    global CACHED_CHOICES, CACHE_TIMESTAMP

    current_time = time.time()

    # Check if the cache is valid
    if CACHED_CHOICES is None or (current_time - CACHE_TIMESTAMP) > CACHE_TIMEOUT:
        logger.info("Fetching fresh data from the HTTP endpoint...")
        try:
            with urllib.request.urlopen(url) as response:
                CACHED_CHOICES = json.loads(response.read().decode())
                CACHE_TIMESTAMP = current_time  # Update the cache timestamp
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
    preprocessed = {}
    for key, values in choices.items():
        preprocessed[key] = {v: matcher(v, values)[0][1] for v in values}
    logger.info("Choices data preprocessed.")
    return preprocessed
