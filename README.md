# **GenAI Filtering Application**

## **Overview**
The **GenAI Filtering Application** is a Python-based project designed to process and enhance natural language queries for retail analytics. It uses fuzzy matching techniques to infer and correct filtering parameters based on predefined choices. This system processes natural language into structured key-value pairs, ensuring accuracy and reliability in downstream analytics workflows. The project emphasizes modularity, performance optimization, and ease of maintenance.

---

# **Issues and Impact with base version**

## **Category: Efficiency**
- **Issue**: Redundant computations for key inference and matching.
  - **Impact**: Increases execution time for larger datasets.
- **Issue**: Repeated string matching for identical keys/values.
  - **Impact**: Wasteful recalculation of scores.
- **Issue**: Sequential data access in `choices`.
  - **Impact**: Slows down matching as data size grows.

---

## **Category: Readability**
- **Issue**: Core logic embedded in a loop, making it harder to follow.
  - **Impact**: Reduces clarity and makes debugging difficult.
- **Issue**: Hardcoded string matching method and threshold.
  - **Impact**: Limits flexibility for tuning or experimenting with other methods.
- **Issue**: Inconsistent variable and function naming conventions.
  - **Impact**: Reduces readability and maintainability.

---

## **Category: Reliability**
- **Issue**: Assumes `choices` and `genai_output` are always valid and complete.
  - **Impact**: Risk of runtime errors when data is malformed or missing.
- **Issue**: No error handling for invalid data or failed matches.
  - **Impact**: Reduces robustness and leads to potential crashes.
- **Issue**: Overreliance on fuzzy string matching without domain validation.
  - **Impact**: Can lead to incorrect inferences in ambiguous cases.

---

## **Category: Scalability**
- **Issue**: Nested loops and sequential access do not scale well for large datasets.
  - **Impact**: Causes performance bottlenecks as data size grows.
- **Issue**: No preprocessing of `choices` for optimized matching.
  - **Impact**: Wastes computational resources during runtime.

---

## **Category: User Feedback**
- **Issue**: Output lacks details about matching confidence or reasoning.
  - **Impact**: Users cannot assess how reliable the inferred matches are.
- **Issue**: No context provided for ambiguous or fallback inferences.
  - **Impact**: Leaves users confused about why a key or value was inferred.

---

# **New Solution Implemented & Recommendations**

## **Libraries**
The project leverages the following libraries:
- **fuzzy_match**: For performing lexical matching on input keys and values.
- **pytest**: For unit testing and ensuring code reliability.
- **urllib3**: For handling HTTP requests, specifically for fetching external choice data.
- **setuptools**: For packaging and building the application.
- **wheel**: For creating distributable Python wheels.

---


## **Project Structure**
The project is structured for clarity and modularity:

```plaintext
genai_app/                   # Root directory
├── genai_app/               # Main package
│   ├── __init__.py          # Package initializer
│   ├── genai_output.py      # Handles GenAI output processing
│   ├── config.py            # Configuration settings (thresholds, methods, etc.)
│   ├── choices.py           # Handles choice data fetching and preprocessing
│   ├── utils/               # Utility modules
│   │   ├── __init__.py
│   │   ├── matcher.py       # Fuzzy matching and key-value inference
│   │   ├── logger.py        # Logging setup
├── tests/                   # Test suite
│   ├── __init__.py          # Optional for pytest
│   ├── test_genai_output.py # Tests for genai_output.py
│   ├── test_matcher.py      # Tests for matcher.py
│   ├── test_config.py       # Tests for configuration
│   ├── test_choices.py      # Tests for choices.py
├── setup.py                 # Packaging configuration
├── pyproject.toml           # Build configuration
├── README.md                # Project documentation
├── LICENSE                  # License file
├── output.log               # logger generated output file
├── requirements.txt         # Dependency list

```

---

##  **Build & Installation Process**

## **Prerequisites**
- Python 3.7 or higher
- `pip` package manager

## **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/charan-datascientist/Goodworkai.git
   cd Goodworkai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the package**:
   ```bash
   python -m build
   ```

4. **Install the package locally**:
   ```bash
   pip install dist/genai_app-1.0.0-py3-none-any.whl
   ```

---

# **How to Run & Test in Local**

## **Run the Application**
To run the application, invoke the main script:

```bash
python -m genai_app.main
```

## **Test the Application**
Navigate to the project root and run `pytest`:

```bash
cd genai_app
pytest tests/
```

---

# **Pytest Process: What Tests Are Covered?**

1. **`test_genai_output.py`**:
   - Validates the `get_genai_output` function for recognized and unrecognized scenario IDs.

2. **`test_matcher.py`**:
   - Tests the `infer_key` function for both recognized and unrecognized keys.
   - Includes edge cases for threshold mismatches.

3. **`test_config.py`**:
   - Ensures configuration settings (`CONFIG` and `SCENARIOS`) are correctly structured.

4. **`test_choices.py`**:
   - Validates the `get_choice_data` function to ensure it fetches and parses external data correctly.
   - Tests `preprocess_choices` for proper preprocessing logic.

---

# **Enhancements: Steps for CICD using GitHub Actions**

## **Steps**
1. **Create a GitHub Actions Workflow File**:  
   Create `.github/workflows/ci.yml` in the repository.

2. **Pseudo Code for the Workflow**:

   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Code
           uses: actions/checkout@v3

         - name: Set Up Python
           uses: actions/setup-python@v4
           with:
             python-version: "3.12"

         - name: Install Dependencies
           run: |
             pip install -r requirements.txt
             pip install build

         - name: Run Tests
           run: pytest tests/

         - name: Build Package
           run: python -m build
   ```

3. **Push Workflow to GitHub**:  
   Commit and push the `.github/workflows/ci.yml` file.

---

# **Optimization & Performance Improvement Compared to Base Version**

## **Base Version**
The initial implementation relied on a less efficient approach for processing and inferring key-value pairs:
- Non-optimal loops for matching keys and values.
- No caching or preprocessing for choices data.
- Lack of modularity in the design.

## **Optimized Version**
- **Preprocessing Choices Data**:
  - Improved preprocessing logic in `choices.py` to reduce runtime overhead during inference.
  - Implemented a cache with timeout (default: 1 hour) to reduce redundant HTTP calls while ensuring data freshness

- **Enhanced Matching Logic**:
  - Introduced a modular `matcher.py` with reusable functions.
  - Leveraged faster matching algorithms for large datasets.

- **Performance Gains**:
  - Reduced matching time in complex scenarios.
  - Enhanced scalability with modular utilities.

- **Exception Handling**:
  - Added error handling for downloading choices, processing scenarios, and key-value inference.

---

# **What I Have Done for Modularity, Readability, and Maintainability**

1. **Modularity**:
   - Organized core logic into separate modules (`genai_output`, `choices`, `matcher`, etc.).
   - Created a `utils` package for reusable utility functions.

2. **Readability**:
   - Adopted PEP 8 coding standards.
   - Used meaningful function names and added comments, logs & docstrings where necessary.

3. **Maintainability**:
   - Added a robust test suite using `pytest`.
   - Centralized configuration in `config.py`.
   - Built a modular project structure to allow future enhancements without disrupting existing functionality.

---

# Recommendation 1: Cache Preprocessed Choices
Implement caching for **preprocessed_choices** alongside raw choice data to eliminate redundant computations. Once preprocessed, reuse the results within the cache timeout period, avoiding reprocessing for repeated requests. This optimization significantly improves efficiency by ensuring preprocessing happens only when raw choice data changes, reducing computational overhead in high-frequency use cases.

---

# Recommendation 2: Parallelize Using ThreadPool
Introduce parallel processing via Python’s **ThreadPoolExecutor** to accelerate preprocessing and scenario handling. By distributing tasks like similarity matching across threads, the system can process multiple keys or scenarios concurrently. This reduces total execution time, optimizes CPU utilization, and ensures faster responses, especially for large datasets or high volumes of scenarios.


```
