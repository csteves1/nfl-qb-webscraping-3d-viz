import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

def scrape_nfl_player(url, player_name):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    table = soup.find("table", class_="d3-o-table")
    if table is None:
        print(f"ERROR: No stats table found for {player_name}")
        return pd.DataFrame()

    rows = table.find("tbody").find_all("tr")

    data = []
    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]
        if len(cols) > 0:
            data.append(cols)

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

    df = pd.DataFrame(data, columns=headers)

    # DEBUG: Print headers
    print(f"\n=== HEADERS FOR {player_name} ===")
    print(df.columns.tolist())
    print("================================\n")

    # NFL.com uses YEAR, YDS, TD
    keep_cols = ["YEAR", "YDS", "TD"]
    df = df[keep_cols]

    # Clean numeric fields
    df["YEAR"] = pd.to_numeric(df["YEAR"], errors="coerce")
    df["YDS"] = pd.to_numeric(df["YDS"].str.replace(",", ""), errors="coerce")
    df["TD"] = pd.to_numeric(df["TD"], errors="coerce")

    df["Player"] = player_name
    return df


# NFL.com URLs
brady_url = "https://www.nfl.com/players/tom-brady/stats/career"
lamar_url = "https://www.nfl.com/players/lamar-jackson/stats/career"

# Scrape both players
brady_df = scrape_nfl_player(brady_url, "Tom Brady")
lamar_df = scrape_nfl_player(lamar_url, "Lamar Jackson")

# Combine
df_all = pd.concat([brady_df, lamar_df], ignore_index=True)

# Drop missing values
df_all = df_all.dropna(subset=["YEAR", "YDS", "TD"])

# Plot
fig = px.scatter_3d(
    df_all,
    x="YEAR",
    y="YDS",
    z="TD",
    color="Player",
    hover_data={"YEAR": True, "YDS": True, "TD": True, "Player": True},
    title="Brady vs Lamar Career Progression (Yards vs TDs)"
)

fig.show()