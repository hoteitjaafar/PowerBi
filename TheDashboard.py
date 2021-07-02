import streamlit as st

st.write('''Thank you for accessing the link. Please use the navigation tool to access the Desired Dashboard. 
              Thank you,
              Jaafar Hoteit.'''

select_box = st.selectbox('Navigate Here', ('PowerBi Dashboard')) 

if select_box == 'PowerBi Dashboard':
  st.markdown('https://app.powerbi.com/reportEmbed?reportId=8e8d2831-e6a5-4737-832f-ec1ebb4154fa&autoAuth=true&ctid=c7ba5b1a-41b6-43e9-a120-6ff654ada137&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXdlc3QtZXVyb3BlLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9', unsafe_allow_html=True)
         
