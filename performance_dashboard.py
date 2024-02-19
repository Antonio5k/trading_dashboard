import pandas as pd
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts


# Constants
GREETING = "<h2 style='text-align: center; color: lightblue;'>Hello Antonio,</h2>"
PERFORMANCE = "<h4 style='text-align: center; color: lightblue;'>Your performance last week was down <span style='color: red;'>-2.2 percent</span>. I've optimized your portfolio to return a <span style='color: green;'>+5.7 percent</span> return next week. Select optimize to review and confirm these change.</h4>"
NAVBAR_STYLE = """
<style>
.stButton>button {
    width:100%;
}
</style>
"""




IMAGE_PATH = "./5k_Labs.jpg"
STOCKS = ['NVDA', 'AAPL', 'TSLA', 'AMD']
START_BALANCE = 200000

# Greeting Text
st.markdown(GREETING, unsafe_allow_html=True)
st.markdown(PERFORMANCE, unsafe_allow_html=True)

# Navigation bar
st.markdown(NAVBAR_STYLE, unsafe_allow_html=True)

# Create three equally spaced columns
col1, col2, col3, col4 = st.columns([1,1,1,1])

# Place each button in the center of its respective column
with col1:
    st.button('Home')

with col2:
    st.button('Trade')

with col3:
    st.button('Journal')

with col4:
    st.button('Optimize')

# Add an image to the sidebar
st.sidebar.image(IMAGE_PATH, width=200)

import matplotlib.ticker as mtick

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = {
    'Trades': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Profit': [-580.0, -380.0, -580.0, -540.0, -266.0, -364.0, 160.0, 112.0, -528.0, -416.0]
}

df = pd.DataFrame(data)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Trades'], 
    y=df['Profit'], 
    fill='tozeroy',
    fillcolor='rgba(173,216,230,0.3)',  # This sets the fill color to transparent light blue
    line_color='lightblue'
))

fig.update_layout(
    title='Performance',
    xaxis_title='Trades',
    yaxis_title='Profit'
)

st.plotly_chart(fig)


st.sidebar.title('Portfolio')

for stock in STOCKS:
    data = yf.Ticker(stock)
    hist = data.history(period="1d")
    close_today = hist['Close'][0]
    close_yesterday = data.history(period="2d")['Close'][0]
    change_percent = ((close_today - close_yesterday) / close_yesterday) * 100
    change_percent = round(change_percent, 5)  # round to 3 hundred-thousandths
    color = 'green' if change_percent > 0 else 'red'
    
    if st.sidebar.button(f"{stock}: {'🔼' if change_percent > 0 else '🔽'} {change_percent}%"):
        # Add your action for the button click here
        pass


# Add a section for case studies to the sidebar
st.sidebar.markdown("## Case Studies")
case_study = st.sidebar.selectbox(
    "Select a case study",
    ("Case Study 1", "Case Study 2", "Case Study 3")
)

# Display the selected case study
if case_study == "Case Study 1":
    st.sidebar.text("Details about Case Study 1.")
elif case_study == "Case Study 2":
    st.sidebar.text("Details about Case Study 2.")
else:
    st.sidebar.text("Details about Case Study 3.")

# Add a section for notes to the sidebar
st.sidebar.markdown("## Notes")
notes = st.sidebar.text_area("Enter your notes here")
