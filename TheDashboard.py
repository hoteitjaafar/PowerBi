import streamlit as st

st.title('Hello')
st.write("Please press on the below link to view Jaafar Hoteit's PowerBi Dashboard")
st.write("Note that the dashboard is dynamic; pressing on a dashboard element, such as an area on the map, will change displayed measures accordingly.")
st.markdown('https://app.powerbi.com/reportEmbed?reportId=8e8d2831-e6a5-4737-832f-ec1ebb4154fa&autoAuth=true&ctid=c7ba5b1a-41b6-43e9-a120-6ff654ada137&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXdlc3QtZXVyb3BlLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9', unsafe_allow_html=True)
