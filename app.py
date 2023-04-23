import streamlit as st
import pandas as pd
import plotly_express as px

# ---- Jupyter Notebooks ----


df = pd.read_csv('ds_salaries.csv')

# Taking out what's unnecessary
df.drop(df[['salary','salary_currency']], axis = 1, inplace = True)

# Converted the experience levels instead of being abreviations to the full title of what they are.
df['experience_level'] = df['experience_level'].replace('EN','Entry_junior')
df['experience_level'] = df['experience_level'].replace('MI','Mid-level')
df['experience_level'] = df['experience_level'].replace('SE','Senior')
df['experience_level'] = df['experience_level'].replace('Ex','Executive')


# ---- Streamlit Material ----

# title at top of tab
st.set_page_config(page_title="Data Science Salaries", layout='wide')

# ---- Header ----

with st.container():
    st.header("Let's Determine Data Scientist Salaries!")
    st.subheader("I am Brandi, an aspiring Data Scientist.")
    st.write("This website shows that Data Scientists at all levels can make a difference, and make a good living!")

st.dataframe(df)


# will create histogram based on: experience level and salary

list_for_hist = ['experience_level', 'salary_in_usd']

# create select box- interactive
choice_for_hist = st.selectbox('Choose experience level', list_for_hist)

# plotly histogram, where price is determined by choice in box
hist1 = px.histogram(df, x= 'salary_in_usd', color='experience_level', color_discrete_map={'Entry-level':'green',
                                                                                          'Mid-level':'red',
                                                                                          'Senior-level':'black', 
                                                                                          'Executive-level':'yellow'})

#add title
hist1.update_layout(title="<b> Salary of level by {}</b>".format(choice_for_hist))

#embed for streamlit
st.plotly_chart(hist1)

# scatter plot 

st.write( """
#### Now let's find out the percentage of Remote work, 
based on experience level and work-time status.
""")

#Remote work- based on experience level and full-time, part-time, contractor, or freelance work
list_for_scatter = ['salary_in_usd', 'remote_ratio','experience_level']
choice_for_scatter = st.selectbox('Remote work dependency', list_for_scatter)
scat1 = px.scatter(df, x='remote_ratio', y=choice_for_scatter, hover_data=['experience_level'])

scat1.update_layout(
title="<br> Remote vs {}</b>".format(choice_for_scatter))
st.plotly_chart(scat1)



