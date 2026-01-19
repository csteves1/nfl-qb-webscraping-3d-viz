🏈 NFL Quarterback Web Scraping & 3D Visualization
This project demonstrates real web scraping, HTML parsing, and data cleaning using live NFL player statistics from NFL.com.
It compares the career passing performance of Tom Brady and Lamar Jackson using an interactive 3D Plotly visualization.
The scraper uses requests to fetch live HTML and BeautifulSoup to parse structured tables directly from the NFL website — no downloads, no manual files, and no JavaScript automation.

🚀 Features
- Live web scraping from NFL.com using requests
- HTML table extraction with BeautifulSoup
- Data cleaning & normalization with pandas
- Numeric conversion (yards, touchdowns, seasons)
- Merging multi‑player datasets
- Interactive 3D visualization using Plotly Express
- Zero manual downloads — everything is fetched and processed automatically

📡 Data Source
This project pulls real-time career stats from:
- Tom Brady:
https://www.nfl.com/players/tom-brady/stats/career (nfl.com in Bing)
- Lamar Jackson:
https://www.nfl.com/players/lamar-jackson/stats/career (nfl.com in Bing)
NFL.com provides clean, static HTML tables that can be parsed reliably without JavaScript or browser automation.

🧠 How It Works
- Send an HTTP request to the player’s NFL.com stats page
- Parse the HTML using BeautifulSoup
- Locate the stats table (<table class="d3-o-table">)
- Extract rows and headers from the table
- Clean the data
- Convert strings to numeric values
- Remove commas from yardage
- Drop missing or invalid rows
- Combine both players’ stats into a single DataFrame
- Visualize the data in a 3D scatter plot
- X-axis: Season
- Y-axis: Passing Yards
- Z-axis: Passing Touchdowns
- Color-coded by player

📦 Requirements
Install dependencies:
pip install -r requirements.txt


Required packages:
- requests
- beautifulsoup4
- pandas
- plotly

▶️ Running the Project
Run the scraper and visualization:
python webscraping.py


This will:
- Fetch live data from NFL.com
- Parse and clean the stats
- Generate an interactive 3D Plotly visualization

📊 Example Output
The visualization shows how each quarterback’s career has progressed over time in terms of:
- Passing Yards (Yds)
- Passing Touchdowns (TD)
- Season (Year)
This makes it easy to compare career trajectories between players.

🔧 Project Structure
/Web Mining
│
├── webscraping.py      # Main scraper + visualization
├── requirements.txt    # Dependencies
└── README.md           # Project documentation



🌱 Future Improvements
- Add more quarterbacks for comparison
- Scrape additional stat categories (QBR, attempts, completions)
- Add time-series visualizations
- Build a small dashboard with Plotly Dash or Streamlit
