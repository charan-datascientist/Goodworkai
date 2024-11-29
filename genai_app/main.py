from genai_app.config import CONFIG, SCENARIOS
from genai_app.genai_output import get_genai_output
from genai_app.choices import get_choice_data, preprocess_choices
from genai_app.utils.matcher import infer_key
from genai_app.utils.logger import logger


def process_scenario(scenario, choices, config):
    """
    Process a single GenAI scenario.

    Args:
        scenario (int): Scenario ID.
        choices (dict): Valid key-value options.
        config (dict): Configuration settings.
    """
    logger.info(f"Processing scenario {scenario}...")
    genai_output = get_genai_output(scenario)
    fixed_output = {}
    output_message = ""

    for k, v in genai_output.items():
        if k in choices:
            # If the key is recognized, infer the value
            inferred_value, score = infer_key(v, choices[k], config["matching_method"], config["threshold"])
            fixed_output[k] = inferred_value
            if score < config["threshold"]:
                output_message += f"Infering key value from {v} to {inferred_value}\n"
        else:
            # If the key is not recognized, infer the key and value
            possible_keys = {
                possible_key: infer_key(v, choices[possible_key], config["matching_method"], config["threshold"])
                for possible_key in choices.keys()
            }
            best_key, (best_value, score) = max(possible_keys.items(), key=lambda x: x[1][1])
            fixed_output[best_key] = best_value
            output_message += f"We do not recognise the key {k}: infering the key as {best_key}\n"
            if score < config["threshold"]:
                output_message += f"Infering key value from {v} to {best_value}\n"

    logger.info(f"Scenario {scenario} processed successfully.")
    logger.info(f"\nScenario {scenario}")
    logger.info(f"Fixed Output: {fixed_output}")
    logger.info(f"Output Message:\n{output_message}")


def process_all_scenarios():
    """
    Process all GenAI scenarios.
    """
    logger.info("Starting to process all scenarios...")
    try:
        # Fetch and preprocess choices with caching
        logger.info("Fetching choices...")
        choices = get_choice_data()
        logger.info("Preprocessing choices...")
        preprocessed_choices = preprocess_choices(
            choices, lambda value, values: infer_key(value, values, CONFIG["matching_method"], CONFIG["threshold"])
        )

        # Process each scenario sequentially
        for scenario in range(len(SCENARIOS)):
            process_scenario(scenario, preprocessed_choices, CONFIG)

        logger.info("All scenarios processed successfully.")
    except Exception as e:
        logger.error(f"Error processing scenarios: {e}")



if __name__ == "__main__":
    process_all_scenarios()
