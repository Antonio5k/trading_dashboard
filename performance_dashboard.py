import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf
from streamlit_chat import message


# Constants
GREETING = "<h1 style='text-align: center; color: lightblue;'>Hello Antonio,</h1>"
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

# Your data
data = {
    'Trades': list(range(1, 11)),
    'Profit': [-580.0, -380.0, -580.0, -540.0, -266.0, -364.0, 160.0, 112.0, -528.0, -416.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Change the sign of the 'Profit' column
df['Profit'] *= -1

# Calculate adjusted profits
df['Adjusted Profit'] = START_BALANCE - df['Profit'].cumsum()

# Set the background color to navy blue
plt.rcParams['axes.facecolor'] = '#020E1C'

# Plot the 'Adjusted Profit'
ax = df.plot(x='Trades', y='Adjusted Profit', kind='line', color='lightblue', title='Performance')

# Change the legend text color to light blue
legend = ax.legend('$')
for text in legend.get_texts():
    text.set_color('lightblue')

# Add a y label titled 'Profit'
ax.set_ylabel('Profit')

# Change the grid color to transparent gray and only show horizontal lines
ax.grid(axis='y', color='gray', alpha=0.5)

# Change the color of the dots to '#6AD4F5'
ax.plot(df['Trades'], df['Adjusted Profit'], 'o', color='#6AD4F5')

# Change the color of the plot's foreground to match the inside of the plot
plt.rcParams['text.color'] = '#062340'
plt.rcParams['axes.labelcolor'] = '#062340'
plt.rcParams['xtick.color'] = '#062340'
plt.rcParams['ytick.color'] = '#062340'

# Format y-axis as dollar
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 

# Use Streamlit's pyplot() function to display the plot
st.pyplot(plt.gcf())
plt.close()



# Sidebar
st.sidebar.title('Portfolio')

for stock in STOCKS:
    data = yf.Ticker(stock)
    hist = data.history(period="1d")
    close_today = hist['Close'][0]
    close_yesterday = data.history(period="2d")['Close'][0]
    change_percent = ((close_today - close_yesterday) / close_yesterday) * 100
    change_percent = round(change_percent, 5)  # round to 3 hundred-thousandths
    color = 'green' if change_percent > 0 else 'red'
    if st.sidebar.markdown(f"<a style='display:block;text-align:center;' href='your_link_here'>{stock}: {'🔼' if change_percent > 0 else '🔽'} <span style='color:{color};'>{change_percent}%</span></a>", unsafe_allow_html=True):
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
