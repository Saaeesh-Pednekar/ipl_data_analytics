import streamlit as st
import plotly.express as px
import pandas as pd
import os 
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="IPL Dashboard", page_icon='bar_chart', layout='wide')

st.title(":bar_chart: IPL Dashboard")
st.markdown('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)

df_match_data = pd.read_csv("preprocessed_data/preprocessed_match_data.csv")
df_match_info_data = pd.read_csv("preprocessed_data/preprocessed_match_info_data.csv")

data_col = None

# data_display = st.write(df_match_info_data[df_match_info_data.columns[1:]])

# f1 = st.file_uploader(":file_folder: Upload a file", type=("csv", "txt", "xlsx", "xls"))
st.sidebar.header("Filters")
st.markdown('<style>[data-testid="stMarkdownContainer"]div.block-container{padding-top:0rem}</style>', unsafe_allow_html=True)
data_col = st.sidebar.multiselect("Select a column for viewing datafield", [df_match_info_data.columns[x] for x in range(1, len(df_match_info_data.columns))])
st.markdown('<style>[data-testid="stSidebar"]{background-color:#e6c4ff}</style>', unsafe_allow_html=True)
st.markdown('<style>[data-testid="stSelectionbox"]{margin-bottom:2rem}</style>', unsafe_allow_html=True)


if data_col == []:
    data_display = st.write(df_match_info_data[df_match_info_data.columns[1:]])
else:
    data_display = st.write(df_match_info_data[[x for x in data_col]])

# team_options1 = df_match_info_data['team1'].unique()[0]
# team_options2 = df_match_info_data['team1'].unique()[1]

# team_options1 = [x for x in df_match_info_data['team1'].unique() if x !=team_options2]
# team1 = st.sidebar.selectbox("Choose Team 1", team_options1)
# st.markdown('<style>[data-testid="stWidgetLabel"]{padding-top:0rem}</style>', unsafe_allow_html=True)
# st.sidebar.write("vs")
# team_options2 = [x for x in df_match_info_data['team2'].unique() if x !=team_options1]
# team2 = st.sidebar.selectbox("Choose Team 2", team_options2)


col1, col2 = st.columns((2))

wins_count = df_match_info_data.groupby(by = ['winner'], as_index=True)['winner'].count()
wins_count = wins_count.rename_axis("Team")
wins_count = wins_count.rename("Wins")


team_name = st.sidebar.multiselect("Select team to view performance", wins_count.index)


if team_name == []:
    pass
else:
    wins_count = wins_count[[x for x in team_name]]

with col1:
    st.subheader("Team with Most Wins")
    fig1 = px.bar(wins_count, y = 'Wins', template='seaborn', color='Wins')
    st.plotly_chart(fig1, use_container_width=True, height = 200)




if team_name == []:
    toss_decision_wins = df_match_info_data.groupby(by=['toss_decision'])['winner'].count()
    toss_decision_wins = toss_decision_wins.rename_axis("Toss Decision")
    toss_decision_wins = toss_decision_wins.rename("Wins")
else:
    filtered_team_name = df_match_info_data[df_match_info_data['winner'].isin(team_name)]
    toss_decision_wins = filtered_team_name.groupby(by=['toss_decision'])['winner'].count()
    toss_decision_wins = toss_decision_wins.rename_axis("Toss Decision")
    toss_decision_wins = toss_decision_wins.rename("Wins")

with col2:
    st.subheader("Match Wins by Toss Decision")
    # st.write(toss_decision_wins)
    fig2 = px.pie(toss_decision_wins, values=toss_decision_wins, names=toss_decision_wins.index, hole=0.65)
    fig2.update_traces(text = toss_decision_wins.index)
    st.plotly_chart(fig2, use_container_width=True, height = 200)

if team_name == []:
    filtered_runs_data = df_match_data.groupby(by=['striker'])['runs_off_bat'].sum()
else:
    filtered_runs_data = df_match_data[df_match_data['batting_team'].isin(team_name)]
    filtered_runs_data = filtered_runs_data.groupby(by=['striker'])['runs_off_bat'].sum()


runs_by_player = filtered_runs_data

runs_by_player = runs_by_player.rename_axis('Batter')
runs_by_player = runs_by_player.rename("Runs")

run_value = st.sidebar.slider("Filter by Runs", value=(runs_by_player.min(), runs_by_player.max()))

runs_by_player = runs_by_player.sort_values(ascending=False)
if run_value[0] == runs_by_player.min() and run_value[1] == runs_by_player.max():
    filtered_runs_by_player = runs_by_player
else:
    runs_by_player = runs_by_player[ runs_by_player >= run_value[0]]
    runs_by_player = runs_by_player[ runs_by_player <= run_value[1]]
    filtered_runs_by_player = runs_by_player
    
st.header("Most Runs Scored by Batter")          
color_sequence = ['green', 'salmon', 'lightgreen', 'orange']
fig3 = px.bar(filtered_runs_by_player, x=filtered_runs_by_player.index, y='Runs', color = 'Runs', template='seaborn', color_continuous_scale='viridis')
fig3.update_traces(width = 3)
st.plotly_chart(fig3, use_container_width=True, height = 500)


if team_name == []:
    filtered_wickets_data = df_match_data.groupby(by=['bowler'])['player_dismissed'].count()
else:
    filtered_wickets_data = df_match_data[df_match_data['bowling_team'].isin(team_name)]
    filtered_wickets_data = filtered_wickets_data.groupby(by=['bowler'])['player_dismissed'].count()


wicket_by_player = filtered_wickets_data
wicket_by_player = wicket_by_player.rename_axis('Bowler')
wicket_by_player = wicket_by_player.rename('Wickets')



# st.write(wicket_by_player)


wicket_value = st.sidebar.slider("Filter by Wickets", value=(wicket_by_player.min(), wicket_by_player.max()))

wicket_by_player = wicket_by_player.sort_values(ascending=False)

if wicket_value[0] == wicket_by_player.min() and wicket_value[1] == wicket_by_player.max():
    filtered_wicket_by_player = wicket_by_player
else:
    wicket_by_player = wicket_by_player[wicket_by_player >= wicket_value[0]]
    wicket_by_player = wicket_by_player[wicket_by_player <= wicket_value[1]]
    filtered_wicket_by_player = wicket_by_player

st.header("Most Wickets taken by Bowler")
fig4 = px.bar(filtered_wicket_by_player, x = wicket_by_player.index, y = 'Wickets', color='Wickets', template='seaborn')
fig4.update_traces(width = 3)
st.plotly_chart(fig4, use_container_width=True, height = 500)

if team_name == []:
    matches_played_in_venue = df_match_info_data.groupby(by=['venue'])['venue'].count()
else:
    filtered_venue_data = df_match_info_data[df_match_info_data['team1'].isin(team_name) | df_match_info_data['team2'].isin(team_name)]
    matches_played_in_venue = filtered_venue_data.groupby(by=['venue'])['venue'].count()


# st.write(matches_played_in_venue)

matches_played_in_venue = matches_played_in_venue.rename_axis('Stadium')
matches_played_in_venue = matches_played_in_venue.rename('Matches Played')

stadium_selected = st.sidebar.multiselect("Select the Stadium", matches_played_in_venue.index)
filtered_matches_played_in_venue = pd.Series()
filtered_matches_played_in_venue = filtered_matches_played_in_venue.rename("Matches Played")
filtered_matches_played_in_venue = filtered_matches_played_in_venue.rename_axis("Stadium")

if stadium_selected == []:
    pass
else:
    for x in stadium_selected:
        filtered_matches_played_in_venue[x] = matches_played_in_venue[x]
    matches_played_in_venue = filtered_matches_played_in_venue

st.header("Matches Played in Venues")
fig5 = px.bar(matches_played_in_venue, y='Matches Played', color='Matches Played', color_continuous_scale='blackbody', template='seaborn')
fig5.update_traces(width = 3)
st.plotly_chart(fig5, use_container_width=True, height = 500)


