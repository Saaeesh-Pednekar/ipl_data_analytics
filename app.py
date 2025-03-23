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

# st.write(data_col)
if data_col == []:
    data_display = st.write(df_match_info_data[df_match_info_data.columns[1:]])
    # pass
else:
    data_display = st.write(df_match_info_data[[x for x in data_col]])
    # pass

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

# st.markdown("<style>[data-testid = 'stHorizontalBlock']div.border-select-none{border:1px solid black}</style>")
team_name = st.sidebar.multiselect("Select team to view performance", df_match_info_data['winner'].unique())

# st.write(team_name)
if team_name == []:
    pass
else:
    wins_count = wins_count[[x for x in team_name]]

with col1:
    st.subheader("Team with Most Wins")
    # st.write(wins_count.unique())
    fig1 = px.bar(wins_count, y = 'Wins', template='seaborn', color='Wins')
    st.plotly_chart(fig1, use_container_width=True, height = 200)



toss_decision_wins = df_match_info_data.groupby(by=['toss_decision'])['winner'].count()

toss_decision_wins = toss_decision_wins.rename_axis("Toss Decision")
toss_decision_wins = toss_decision_wins.rename("Wins")

with col2:
    st.subheader("Toss Decision")
    # st.write(toss_decision_wins)
    fig2 = px.pie(toss_decision_wins, values=toss_decision_wins, names=toss_decision_wins.index)
    st.plotly_chart(fig2, use_container_width=True, height = 200)


runs_by_player = df_match_data.groupby(by=['striker'])['runs_off_bat'].sum()

runs_by_player = runs_by_player.rename_axis('Batter')
runs_by_player = runs_by_player.rename("Runs")

run_value = st.sidebar.slider("Filter by Runs", value=(runs_by_player.min(), runs_by_player.max()))
st.markdown(
    """
    <style>
    div[role="slider"] div[data-baseweb="slider-thumb"] {
        background-color: red; 
    }
    div[role="slider"] div[data-baseweb="slider-track"] {
        background: linear-gradient(to right, red, red);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
filtered_runs_by_player = pd.Series()
# st.write(run_value[1])
runs_by_player = runs_by_player.sort_values(ascending=False)
if run_value[0] == runs_by_player.min() and run_value[1] == runs_by_player.max():
    filtered_runs_by_player = runs_by_player
else:
    # for runs in runs_by_player:
    #     if runs >= run_value[0] and runs<= run_value[1]:
    runs_by_player = runs_by_player[ runs_by_player > run_value[0]]
    runs_by_player = runs_by_player[ runs_by_player < run_value[1]]
    filtered_runs_by_player = runs_by_player
    
            

fig3 = px.bar(filtered_runs_by_player, x=filtered_runs_by_player.index, y='Runs', color='Runs', template='seaborn')
fig3.update_traces(width = 3)
st.plotly_chart(fig3, use_container_width=True, height = 300)
# st.sidebar()