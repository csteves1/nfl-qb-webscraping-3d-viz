import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

def scrape_player(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", {"id": "passing"})
    
    data = []
    for row in table.find("tbody").find_all("tr"):
        year = row.find("th").get_text()
        cells = [cell.get_text() for cell in row.find_all("td")]
        if cells:
            data.append([year] + cells)
    
    headers = ["Year"] + [th.get_text().strip() for th in table.find("thead").find_all("th")[1:]]
    df = pd.DataFrame(data, columns=headers)
    df.columns = df.columns.str.strip()
    df.columns = [
        "Year","Age","Team","Lg","Pos","G","GS","QBrec","Cmp","Att","Cmp%",
        "PassYds","TD","TD%","Int","Int%","1D","Succ%","Lng","Y/A","AY/A","Y/C",
        "Y/G","Rate","QBR","Sk","SackYds","Sk%","NY/A","ANY/A","4QC","GWD","AV","Awards"
    ]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["PassYds"] = pd.to_numeric(df["PassYds"], errors="coerce")
    df["TD"] = pd.to_numeric(df["TD"], errors="coerce")
    return df

# Scrape Tom Brady
brady_url = "https://www.pro-football-reference.com/players/B/BradTo00.htm"
brady_df = scrape_player(brady_url)
brady_df["Player"] = "Tom Brady"

# Scrape Lamar Jackson
lamar_url = "https://www.pro-football-reference.com/players/J/JackLa00.htm"
lamar_df = scrape_player(lamar_url)
lamar_df["Player"] = "Lamar Jackson"

# Combine both
df_all = pd.concat([brady_df, lamar_df])

# Interactive 3D scatter plot
fig = px.scatter_3d(
    df_all,
    x="Year",
    y="PassYds",
    z="TD",
    color="Player",  # color code by player
    hover_data={"Year": True, "PassYds": True, "TD": True, "Player": True},
    title="Brady vs Lamar Career Progression (Yards vs TDs)"
)

fig.show()

