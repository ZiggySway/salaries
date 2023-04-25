import streamlit as st
import pandas as pd
import plotly_express as px


# ---- Jupyter Notebooks ----




df = pd.read_csv('ds_salaries.csv')

# Clean data
df.drop(df[['salary','salary_currency']], axis = 1, inplace = True)


df['experience_level'] = df['experience_level'].replace('EN','Entry_junior')
df['experience_level'] = df['experience_level'].replace('MI','Mid-level')
df['experience_level'] = df['experience_level'].replace('SE','Senior')
df['experience_level'] = df['experience_level'].replace('Ex','Executive')

df.duplicated().sum()
df = df.drop_duplicates()


# ---- Streamlit Material ----

# title at top of tab
#st.set_page_config(page_title="Data Science Salaries", layout='wide')

# ---- Header ----

with st.container():
    st.header("Let's Determine Data Scientist Salaries!")
    st.subheader("I am Brandi, an aspiring Data Scientist.")
    st.write("This website shows that Data Scientists at all levels can make a difference, and make a good living!")

st.dataframe(df)




#will create histogram based on: experience level and salary

list_for_hist = ['Entry_Junior', 'Mid_level', 'Senior', 'Executive']

#create select box- interactive
#choice_for_hist = st.selectbox('Choose experience level', list_for_hist)

st.write("### Click on the experience level boxes in the legend, to turn off/on the experience levels for salaries. ###")

#plotly histogram, where price is determined by choice in box
figure = px.histogram(df, x= 'salary_in_usd', color='experience_level', color_discrete_map={'Entry_Junior':'red', 
                                                                                          'Mid_level':'green', 
                                                                                          'Senior':'black', 
                                                                                          'Executive':'yellow'})

#add title
figure.update_layout(title="<b> Experience level Salary</b>".format(list_for_hist))

#embed for streamlit
st.plotly_chart(figure)
figure.show()


# scatter plot 

st.write( """
#### Now let's find out Salary in comparison to company size, based on experience level and work-time status
""")

#Remote work- based on experience level and full-time, part-time, contractor, or freelance work
#list_for_scatter = ['salary_in_usd']
#choice_for_scatter = st.selectbox('Remote work dependency', list_for_scatter)


figure2 = []
#px.scatter(df, x='salary_in_usd')

"""""
def function(df):
    x_label = st.selectbox('Choose X-Axis Value', options=df['salary_in_usd'])
    y_label = st.selectbox('Choose Y-Axis Value', options=df['company_size'])

    figure2 = px.scatter(df, x=x_label, y=y_label)

    figure2.update_layout(title="<br> Salary depiction</b>")
    st.plotly_chart(figure2)
"""""

"""""
one_value_company_size = df['company_size'] == "M"
two_value_company_size = df['company_size'] == "M"

x_label = st.selectbox('Choose X-Axis Value', options=df['employee_residence'])
y_label = st.selectbox('Choose Y-Axis Value', options=df['company_size'])
figure2 = px.scatter(df['salary_in_usd'], x='salary_in_usd', y=y_label)
"""
option = st.selectbox(
    'Choose company size : (S)Small, (M)Medium, (L)Large',
    ('S', 'M', 'L'))

st.write(figure2, option)


figure2.update_layout(
title="<br> Salary depiction based on factors</b>")
st.plotly_chart(figure2)




st.write("""
This project shows the historical collected data of salary and details of data scientist worker.  
This helps users to understand their potential salaries if they are to work in the field.  
""")
