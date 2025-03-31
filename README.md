# Spotify Data Pipeline

This project aims to build a data pipeline for Spotify listening history, from extraction to analysis. Currently, the data extraction and transformation components are complete.

## Project Status

-   **Data Extraction:** Completed. Extracts listening history data from the Spotify API.
-   **Data Transformation:** Completed. Transforms the raw JSON data into a structured format suitable for further analysis.
-   **Data Storage:** To be implemented. Will store the transformed data in a database or data warehouse.
-   **Data Analysis:** To be implemented. Will perform analysis on the listening history data to gain insights.
-   **Data Visualization:** To be implemented. Will visualize the analysis results.

## Completed Features

-   **JSON Transformation:** The `transform_data` function in `transform_data.py` efficiently converts the raw Spotify API JSON response into a list of dictionaries, with each dictionary representing a played track. This includes extracting relevant track, album, and artist information.

## To Be Implemented

-   **Database Integration:**
    - Choose a suitable database (e.g., PostgreSQL, MySQL, SQLite) or data warehouse (e.g., BigQuery, Redshift).
    - Implement code to store the transformed data into the chosen database/data warehouse.
    - Design the database schema to efficiently store and query the data.
-   **Data Analysis:**
    - Develop SQL queries or Python scripts to analyze the listening history data.
    - Examples of analysis:
        - Top artists and tracks.
        - Listening patterns over time.
        - Album popularity.
        - Context analysis (playlist, album, etc).
    - Consider using libraries like Pandas for data manipulation and analysis.
-   **Data Visualization:**
    - Use libraries like Matplotlib, Seaborn, or Plotly to create visualizations of the analysis results.
    - Examples of visualizations:
        - Bar charts of top artists.
        - Line plots of listening activity over time.
        - Pie charts of genre distribution.
-   **Error Handling and Logging:**
    -  Implement robust error handling to catch and log any issues during the pipeline's execution.
    - Use a logging library to record relevant information.
-   **Automation:**
    - Automate the data pipeline using tools like Apache Airflow or Prefect to schedule and manage the data flow.
    - This will ensure the pipeline runs regularly and automatically.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/spitzer4/spotify-listening-etl
    cd spotify-listening-etl
    ```
2.  **Install dependencies:**
    ```bash
    # If necessary, create a virtual environment
    python -m venv venv
    source venv/bin/activate # (Linux/macOS)
    venv\Scripts\activate # (Windows)

    # Install any required python libraries. add them to a requirements.txt file.
    pip install -r requirements.txt
    ```
3.  **Run the extract data script.**
	```bash
    python extract_spotify_data.py
    ```
4.  **Run the transformation script:**
    ```bash
    python transform_data.py
    ```
4.  **Configure Spotify API Credentials:**
    -   You will need to obtain Spotify API credentials (client ID and client secret) from the Spotify Developer Dashboard.
    -   Store these credentials securely (e.g., as environment variables or in a configuration file).
5.  **Database setup:**
    -   Setup your database of choice.
    -   Configure the database connection in your code.
6.  **Future steps:**
    -   Complete the remaining implementation steps according to the "To Be Implemented" section.
