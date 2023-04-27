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
    st.header("Let's Determine Data Science field Salaries!")
    st.subheader("I am Brandi, an aspiring Data Scientist.")
    st.write("This website shows that Data Scientists at all levels can make a difference, and make a good living!")

st.dataframe(df)


st.subheader( """Now let's find out Salary in comparison to company size, based on experience level and work-time status
""")


#will create histogram based on: experience level and salary

list_for_hist = ['Entry_Junior', 'Mid_level', 'Senior', 'Executive']

st.write("Click on the experience level boxes in the legend, to turn off or on the experience levels for salaries.")

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


check_l = "Choose"



if check_l:
    st.checkbox('(L) Large companies', True)
    df_select_l = df.query("company_size == 'L'")
    figure3 = px.scatter(df_select_l, y='salary_in_usd', labels= {'index':'Individual surveyors who work at different size companies'}, hover_data=None)
    st.plotly_chart(figure3)
elif st.checkbox('(M) Medium companies', True):
    df_select_m = df.query("company_size == 'M'")
    figure4 = px.scatter(df_select_m, y='salary_in_usd', labels= {'index':'Individual surveyors who work at different size companies'}, hover_data=None)
    st.plotly_chart(figure4)
elif st.checkbox('(S) Small companies', True):
    df_select_s = df.query("company_size == 'S'")
    figure5 = px.scatter(df_select_s, y='salary_in_usd', labels= {'index':'Individual surveyors who work at different size companies'}, hover_data=None)
    st.plotly_chart(figure5)
    


st.write("""
This project shows the historical collected data of salary and details of data scientist worker.  
This helps users to understand their potential salaries if they are to work in the field.  
""")
