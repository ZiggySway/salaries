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
#### Now let's find out the level/ percentage of Remote work, 
based on experience level and work-time status
""")

#Remote work- based on experience level and full-time, part-time, contractor, or freelance work
#list_for_scatter = ['salary_in_usd']
#choice_for_scatter = st.selectbox('Remote work dependency', list_for_scatter)


figure2 = px.scatter(df, x='salary_in_usd')

def function(df):
    x_label = st.selectbox('Choose X-Axis Value', options=df['salary_in_usd'])
    y_label = st.selectbox('Choose Y-Axis Value', options=df['company_size'])

    figure2 = px.scatter(df, x=x_label, y=y_label)

    figure2.update_layout(
    title="<br> Salary depiction</b>")
    st.plotly_chart(figure2)

#hover_data=['employment_type']

    
figure2.update_layout(
title="<br> Salary depiction: {figure2}</b>")
st.plotly_chart(figure2)

figure2.show()

st.write( """
#### This project shows the historical collected data of salary and details of data scientist worker.  This helps users to understand their potential salaries if they are to work in the field.  

Remote-ratio chart shows the amount of workers working fully remote, vs half-time remote and full office workers.


The salary histogram, shows salary based on level of work experience.  It has toggle information to allow the user to interact with the chart.  To see specifically the levels separate and together.


Salary (remote-level); the scatter plot shows a scatter of salaries, and the hover content shows whether that salary is from a full-time/ FT, part-time/ PT, freelance/ FL, or contract/ CT.
""")
