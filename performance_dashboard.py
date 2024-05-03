import pandas as pd
import streamlit as st
import yfinance as yf
from PIL import Image

# Constants
GREETING = "<h1 style='text-align: center; color: lightblue;'>Hello Antonio</h1>"
PERFORMANCE = "<h1 style='text-align: center; color: lightblue;'>Your performance last week resulted in <span style='color: green;'>+ 0.2 %</span></h2>"
NAVBAR_STYLE = """
<style>
.stButton>button {
    width:100%;
}
</style>
"""

IMAGE_PATH = "./5k_Labs.jpg"
STOCKS = ['NVDA', 'AAPL', 'TSLA', 'AMD']
START_BALANCE = 100000

# Greeting Text
st.markdown(GREETING, unsafe_allow_html=True)
st.markdown(PERFORMANCE, unsafe_allow_html=True)

# Navigation bar
st.markdown(NAVBAR_STYLE, unsafe_allow_html=True)

# Create three equally spaced columns
col1, col2, col3, col4 = st.columns([1,1,1,1])

# Place each button in the center of its respective column
# Remove column width constraints
st.button('Trade')
st.button('Journal')
st.button('Optimize')

# Add an image to the sidebar
st.sidebar.image(IMAGE_PATH, width=200)

import matplotlib.ticker as mtick
import plotly.graph_objects as go

data = {
    'Trades': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    'Profit': [-252.0, -12.0, 0.0, -36.0, -204.0, -156.0, -240.0, 300.0, 192.0, -240.0, 252.0, -12.0, -264.0, 576.0, 540.0, -24.0, -288.0]
}

df = pd.DataFrame(data)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Trades'], 
    y=df['Profit'], 
    fill='tozeroy',
    fillcolor='rgba(173,216,230,0.3)',  # This sets the fill color to transparent light blue
    line_color='lightgreen'
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

# Best Trade of The Week
st.title("Antonio's Best Trade this Week")

# Load and display the image
image_path = 'US30-W5212732362690859.png'  # Replace with the path to your image file
image = Image.open(image_path)
st.image(image, caption='Long Position Taken on US30 index', use_column_width=True)

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
