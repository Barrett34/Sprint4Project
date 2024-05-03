import streamlit as st
import plotly.express as pex
import plotly.figure_factory as ff
import pandas as pd

st.header('Vehicle Sales US EDA & SDA Study')

st.write('In this project, we will conduct a statistical and explorative data analysis of the vehicles sold in the US. The data comes from a cars advertisement dataset in a .csv file. ')

vehicle_csv_path = 'vehicles_us.csv'

vehicles_df = pd.read_csv(vehicle_csv_path)
st.dataframe(vehicles_df)

mean_cost_by_model_yr = vehicles_df.groupby(['model_year']).agg(mean_price=('price','mean')).sort_index().sort_values(by='mean_price', ascending=False)
mean_price_by_yr_his = pex.histogram(mean_cost_by_model_yr, x = 'mean_price', title='Mean Price By Year Histogram', labels={
    "mean_price":"Mean Price"
})
mean_price_by_model_yr_scatter = pex.scatter(mean_cost_by_model_yr,  y="mean_price", title='Mean Price by Model Year', labels={
                     "mean_price": "Mean Price",
                     "model_year": "Model Year",
                 })

mean_cost_by_condition = vehicles_df.groupby('condition').agg(mean_price=('price','mean')).sort_index().sort_values(by='mean_price', ascending=False)
mean_price_by_condition_bar = pex.bar(mean_cost_by_condition, y="mean_price", title='Mean Price of Vehicle vs Vehicle Condition', labels={
    "mean_price":"Mean Price",
    "condition":"condition"
})

year_to_filter = st.slider('model_year', min_value=int(vehicles_df['model_year'].min()), max_value=int(vehicles_df['model_year'].max()), value=int(df['year'].min()))

# Filtering the DataFrame based on the selected year
filtered_df = vehicles_df[vehicles_df['model_year'] == year_to_filter]

# Then display the filtered data (or perform other operations)
st.write(filtered_df)

st.subheader('Mean Price By Model Year')

show_scatterplot = st.checkbox('Scatterplot', value=True)

if show_scatterplot:
    st.write(mean_price_by_model_yr_scatter)
else:
    st.write(mean_price_by_yr_his)


st.subheader("Mean Price by Condition Year")
st.write(mean_price_by_condition_bar)

st.subheader("Study Conclusion")
st.write('After conducting our study, we have found some interesting insights. We discovered that some older vehicles from the 1950s and 1960s actually are highly valued as compared to most of the modern vehicles of today. This was shown in our scatterplot that compares the mean price and model year. 1952 had the highest mean cost. However, it is safe to assume due to the amount of available vehicles from the 1950s that are still available, this may be why the vehicles from that era are so highly valued.We also discovered that the vehicles prices that occur the most in the US are valued between 5k - 10k, with the least being 35k - 40k. This could be due to people selling their old vehicles that they no longer want or use. That would be an interesting study.Lastly, we discovered that the relationship between the vehicle condition and pricing are correlated. If the condition is newer, then the pricing for the vehicle is most likely going to be higher than a vehicle with an older condition. ')