import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox("Select any one", ['Overall Analysis', 'Startup', 'Investor'])

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups',num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig3)

def load_investor_detail(investor):
    st.title(investor)

    #
    st.subheader("Recent Investment")
    st.dataframe(
        df[df['investors'].apply(lambda x: investor in x)][['date', 'startup', 'vertical', 'city', 'amount']].set_index(
            'startup').head(5))

    # with col2:
    col1, col2 = st.columns(2)
    with col1:
        data = df[df['investors'].apply(lambda x: investor in x)][['startup', 'amount']].sort_values('amount',
                                                                                                     ascending=False).head(
            5)

        st.subheader("Biggest Investment")
        fig, ax = plt.subplots()
        ax.bar(data['startup'], data['amount'])
        st.pyplot(fig)
    with col2:
        st.subheader("Generally Invests in Sector ")
        data2 = df[df['investors'].apply(lambda x: investor in x)][['vertical', 'amount']].groupby('vertical')[
            'amount'].sum()
        fig1, ax = plt.subplots()
        ax.pie(data2, labels=data2.index, autopct="%0.01f")
        st.pyplot(fig1)

    col4, col5 = st.columns(2)
    with col4:
        st.subheader("Generally Invests in Stage ")
        data3 = df[df['investors'].apply(lambda x: investor in x)][['round', 'amount']].groupby('round')['amount'].sum()
        fig2, ax = plt.subplots()
        ax.pie(data3, labels=data3.index, autopct="%0.01f")
        st.pyplot(fig2)
    with col5:
        st.subheader("Generally Invests in City ")
        data4 = df[df['investors'].apply(lambda x: investor in x)][['city', 'amount']].groupby('city')['amount'].sum()
        fig3, ax = plt.subplots()
        ax.pie(data4, labels=data4.index, autopct="%0.01f")
        st.pyplot(fig3)

    df['year'] = df['date'].dt.year

    st.subheader("Year on Year Investment ")
    data5 = df[df['investors'].apply(lambda x: investor in x)][['year', 'amount']].groupby('year')['amount'].sum()
    fig4, ax = plt.subplots()
    ax.plot(data5.index, data5.values)
    st.pyplot(fig4)

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find Startup details")
    st.title("Startup Analysis")
else:
    select_investor = st.sidebar.selectbox('Select Investors', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor details")

    # st.title("Investor Analysis")
    if btn2:
        load_investor_detail(select_investor)
