# Modules
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

animes_dict = pickle.load(open('animes_dict.pkl','rb'))
animes = pd.DataFrame(animes_dict)
@st.cache() # tells streamlit that whenever a function is called, it needs to check a few things
def recommend(anime): # Main function
    # Uses the pkl files which contains the cleaned dataset for the algorithm
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    index = animes[animes["Name"] == anime]["index"].values[0]
    # enumarate allows us to loop over a list of itmes while keeping track of the index value in a separate variable
    # lambda creates an anonymous inline function
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # Empty list for storing filtered data based on user's input
    recommended_anime_names = []
    recommended_anime_summary = []
    recommended_anime_startYear = []
    recommended_anime_endYear = []
    recommended_anime_finished = []
    recommended_anime_episodes = []
    recommended_anime_type = []
    recommended_anime_studios = []
    recommended_anime_tags = []
    for i in distances[1:6]:
        # Appends the filtered outcome to the empty lists
        recommended_anime_names.append(animes.iloc[i[0]].Name)
        recommended_anime_summary.append(animes.iloc[i[0]].Synopsis)
        recommended_anime_finished.append(animes.iloc[i[0]].Finished)
        recommended_anime_startYear.append(animes.iloc[i[0]].StartYear)
        recommended_anime_endYear.append(animes.iloc[i[0]].EndYear)
        recommended_anime_episodes.append(animes.iloc[i[0]].Episodes)
        recommended_anime_type.append(animes.iloc[i[0]].Type)
        recommended_anime_studios.append(animes.iloc[i[0]].Studios)
        recommended_anime_tags.append(animes.iloc[i[0]].Tags)

    return recommended_anime_names,recommended_anime_summary,recommended_anime_finished,recommended_anime_startYear,recommended_anime_endYear,recommended_anime_episodes,recommended_anime_type,recommended_anime_studios,recommended_anime_tags


# Anything with "st." acts like an HTML tag that displays tiles, text, image, etc.

# Titles and headings
st.title('Anime Recommender')
st.caption('By Tu Dinh')
st.write('Based on your interests, we will provide suggestions related to your pick.')
# Anime image
image = Image.open('banner.jpg') 
st.image(image, use_column_width=True)
# Select box
selected_anime = st.selectbox(
'So, which Anime did you enjoy?',
(animes['Name'].values))
# A gimmick to tell users that suggestions will be based on their input
st.write('Suggestions will be based on:',selected_anime)


if st.button('Recommend'):
    # Loading screen
    with st.spinner(text='In progress'):
         recommendations,summary,finished,startYear,endYear,episodes,type,studios,tags = recommend(selected_anime)
         # Output
         for i in range(5): 
             st.title(f"{i+1})"+"Title  :  "+str(recommendations[i]))
             st.write("Summary  : ")
             st.write(str(summary[i]))
             st.write("Type : "+str(type[i]))
             st.write("Finished: "+str(finished[i]))
             st.write("Start year / End year : "+str(startYear[i])+ " - " +str(endYear[i]))
             st.write("Episodes : "+str(episodes[i]))
             st.write("Studio(s) : "+str(studios[i]))
             st.write("Tags :  "+str(tags[i]))


