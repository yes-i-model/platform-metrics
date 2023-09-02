# User Behavior Analytics Tool

## Description

The User Behavior Analytics Tool is a Python program designed to automate the analysis of platform usage data for quantitative UX research using the CLI. Developed during my tenure at a tech company relying on manual and qualitative UX research practices, this tool aims to provide meaningful insights and targeted statistics to enhance the organization's understanding of user behavior.

The tool takes input data in the form of CSV files containing platform usage data and generates a comprehensive set of statistics that support UX research efforts. By automating the process of extracting insights from usage data, this tool streamlines the analysis process and facilitates data-driven decision-making.

## Features

- Calculate **time spent on the platform** by users.
- Analyze the **number of pages viewed** per session.
- Track **organizations added** and changes made by users.
- Evaluate the **number of accounts created** over a specified time frame.
- Measure **task completion rates** to assess user interaction efficiency.
- Generate other **UX research supporting statistics** for informed decision-making.

## How It Works

1. **Input Data**: Provide CSV files containing platform usage data. Each file represents a set of user interactions.

2. **Data Processing**: The program processes the CSV files, extracting relevant information such as timestamps, user actions, and interactions.

3. **Statistical Analysis**: Utilizing the extracted data, the tool performs various statistical calculations to generate valuable insights into user behavior.

4. **Output Generation**: The tool compiles the calculated statistics into a comprehensive report, presenting an overview of user behavior trends and patterns.

## Reports

The `reports` folder included in this repository contains anonymized reports generated using the User Behavior Analytics Tool. These reports have been prepared to communicate metrics and insights derived from the analyzed platform usage data. To ensure security and privacy, all data within these reports has been anonymized.

Feel free to explore these reports to gain a better understanding of how the tool can help communicate meaningful information to stakeholders and support decision-making processes within the organization.

## Getting Started

Follow these steps to get started with the User Behavior Analytics Tool:

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/user-behavior-analytics.git
   ```

2. Navigate to the project directory:
   ```
   cd user-behavior-analytics
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Prepare your CSV files containing platform usage data and place them in the `data` directory.

5. Run the tool:
   ```
   python platform_usage_metrics.py
   ```

6. View the generated report in the `output` directory for insights into user behavior.


## Contributions

Contributions to the User Behavior Analytics Tool are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to submit a pull request. Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

---

By Nicolas Pascale



Connect with me on [LinkedIn](https://www.linkedin.com/in/nicolas-pascale-b19161125/) 
