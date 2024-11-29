# genai_app/main.py

from concurrent.futures import ThreadPoolExecutor
from genai_app.config import CONFIG, SCENARIOS, CHOICES_URL
from genai_app.genai_output import get_genai_output
from genai_app.choices import get_choice_data, preprocess_choices
from genai_app.utils.matcher import infer_key
from genai_app.utils.logger import logger
from genai_app.utils.validator import validate_scenario

def process_scenario(scenario, choices, config):
    """
    Process a single GenAI scenario.

    Args:
        scenario (int): Scenario ID.
        choices (dict): Valid key-value options.
        config (dict): Configuration settings.
    """
    try:
        validate_scenario(scenario, len(SCENARIOS))
        genai_output = get_genai_output(scenario)
        fixed_output = {}
        output_message = ""

        for k, v in genai_output.items():
            inferred_key, inferred_value, score, original_key = infer_key(
                k, v, choices, config["matching_method"], config["threshold"]
            )
            fixed_output[inferred_key] = inferred_value
            if original_key:
                output_message += f"Inferred key '{original_key}' as '{inferred_key}'.\n"
            if score < config["threshold"]:
                output_message += f"Inferred value '{v}' as '{inferred_value}'.\n"

        logger.info(f"Scenario {scenario} processed: {fixed_output}")
        logger.debug(output_message)

    except Exception as e:
        logger.error(f"Error processing scenario {scenario}: {e}")

def process_all_scenarios():
    """Process all GenAI scenarios."""
    try:
        choices = get_choice_data(CHOICES_URL)
        preprocessed_choices = preprocess_choices(
            choices, lambda v, values: infer_key(v, values, CONFIG["matching_method"], CONFIG["threshold"])
        )
        with ThreadPoolExecutor() as executor:
            executor.map(lambda s: process_scenario(s, preprocessed_choices, CONFIG), range(len(SCENARIOS)))
    except Exception as e:
        logger.error(f"Error processing all scenarios: {e}")

if __name__ == "__main__":
    process_all_scenarios()
