# Startup-Analysis
 Streamlit Website: https://fu5y5sqgvdzs2e9tdmjnv8.streamlit.app/

# 📊 Startup Funding Analysis Dashboard

Welcome to the **Startup Funding Analysis Dashboard**! This interactive Streamlit app provides comprehensive insights into the startup funding landscape. Whether you're interested in overall trends, specific startups, or investor activities, this dashboard has you covered.

## Features

- **Overall Analysis**: Get an overview of total funding, maximum investments, average ticket sizes, and the number of funded startups.
- **Startup Analysis**: Dive into detailed information about specific startups.
- **Investor Analysis**: Explore detailed profiles of investors, including recent investments, preferred sectors, investment stages, and more.
![img](https://github.com/mayurdalvi5/Startup-Analysis/blob/main/practice_streamlit/Dashboard.png)
## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mayurdalvi5/Startup-Analysis.git
    cd Startup-Analysis
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

## Usage

Upon running the app, you will see a sidebar with options to select the type of analysis:

### 1. Overall Analysis

- **Total Invested Amount**: Displays the cumulative amount of funding.
- **Maximum Funding**: Shows the highest funding received by a single startup.
- **Average Funding**: Provides the average funding per startup.
- **Total Funded Startups**: Indicates the number of unique startups that received funding.
- **Month-on-Month (MoM) Graph**: Visual representation of the total or count of investments over time.

### 2. Startup Analysis

Select a startup from the dropdown menu to view its details. (Feature to be fully implemented in future updates.)

### 3. Investor Analysis

Select an investor to view:

- **Recent Investments**: A table of the latest investments by the selected investor.
- **Biggest Investments**: A bar chart showing the top investments by amount.
- **Preferred Sectors**: A pie chart displaying the sectors where the investor usually invests.
- **Preferred Stages**: A pie chart showing the investment stages favored by the investor.
- **Preferred Cities**: A pie chart of the cities where the investor predominantly invests.
- **Year-on-Year Investment**: A line chart showing the investor’s funding trends over the years.
    ![img](https://github.com/mayurdalvi5/Startup-Analysis/blob/main/practice_streamlit/investor.png)
## Data

The data used in this dashboard is sourced from `startup_cleaned.csv`. It includes information such as:

- **Date** of investment
- **Startup** name
- **Vertical** (industry sector)
- **City** of the startup
- **Amount** invested
- **Investors** involved
- **Round** of investment

## Contributing

We welcome contributions to enhance the features and functionality of this dashboard. Please fork the repository and submit a pull request with your changes.


## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out at [mayurdalvi.5@gmail.com].

---

*Happy Analyzing!* 🚀
