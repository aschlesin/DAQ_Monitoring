import json

import streamlit as st

from oncdw import ONCDW

st.set_page_config(layout="wide", page_title="Accelerometer and Tiltmeter at NEPTUNE")
# custom css
st.markdown(
    """
    <style>
        /* Sidebar CSS */
        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
            gap: 0rem;
        }

        section[data-testid="stSidebar"] h2 img {
            height: 2rem;
        }

        section[data-testid="stSidebar"] h3 img {
            height: 1.5rem;
            padding-left: 1rem;
        }

        section[data-testid="stSidebar"] hr {
            margin: 1.5rem auto;
        }

        /* Body Badge CSS */

        h2 img {
            height: 2.5rem;
        }

        h3 img {
            height: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


print("Running the file.....................")
devices = json.load(open("./Acc_TOC.json"))
# devices = json.load(open("./toc_reduced.json"))

client = ONCDW()

st.title("BPR Monitoring Dashboard")

with st.sidebar:
    st.title("Device List")

    for device in devices:
        client.ui.sidebar_header_location(device)
        client.ui.sidebar_header_device(device)
        for sensor in device["sensors"]:
            client.ui.sidebar_subheader_sensor(sensor)
        st.divider()


for device in devices:
    client.ui.header_location(device)
    client.ui.header_device(device)
    
    # # Data Preview png
    # st.subheader("Data Preview plot")
    # col1, col2 = st.columns(2)
    # with col1:
    #     client.widget.data_preview(device, 3, plot_number=1)
    # with col2:
    #     client.widget.data_preview(device, 3, plot_number=2)

    # Archive file table
    st.subheader("Archive file table")
    client.widget.table_archive_files(device)

    # Time series two sensors
    st.subheader("Time series")
    sensor1, sensor2 = (
        device["sensors"][0],
        device["sensors"][1],
    )
    col1, col2 = st.columns(2, gap="large")
    with col1:
        client.ui.subheader_sensor(sensor1)
    with col2:
        client.ui.subheader_sensor(sensor2)

    client.widget.time_series_two_sensors(sensor1, sensor2,last_days=2)