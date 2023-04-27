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

# ---- Header ----

with st.container():
    st.header("Let's Determine Data Scientist Salaries!")
    st.subheader("I am Brandi, an aspiring Data Scientist.")
    st.write("This website shows that Data Scientists at all levels can make a difference, and make a good living!")

st.dataframe(df)


st.write( """
#### Now let's find out Salary in comparison to company size, based on experience level and work-time status
""")


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


# new dataframe

combine_df = df.groupby('company_size')['salary_in_usd'].sum().reset_index()
combine_df

# scatter plot 

st.write( """
#### Now let's find out Salary in comparison to company size, based on experience level and work-time status
""")

#will create SCATTER



df_selected = combine_df.query("company_size == 'L'")
figure2 = px.scatter(df_selected, x= 'salary_in_usd', y='company_size')


df_select = df.query("company_size == 'L'")
figure3 = px.scatter(df_selected, x= 'salary_in_usd', y='company_size')
figure3.show()

    


# Get the number of people in each job title
#job_title_counts = filtered_scat_data.groupby('job_title').unique()
#filtered_scat_data = df[df['job_title'] == job_title]

# Create scatter plot with Plotly Express
#scatter1 = px.scatter(df_s, x=check_s, y='salary_in_usd')

#scatter1 = px.scatter(filtered_scat_data, x=job_title_counts.index, y='salary_in_usd')
#scatter1.update_layout(title="<b>Expected salary for {}</b>".format("company_size"))

# Embed in Streamlit
#st.plotly_chart(scatter1)




st.write("""
This project shows the historical collected data of salary and details of data scientist worker.  
This helps users to understand their potential salaries if they are to work in the field.  
""")
