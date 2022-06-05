# anime_recommender_app
Anime recommender project using the framework "Streamlit"

Detailed explanation:

User has a dropdown/search box option where they can pick or search any anime titles from the “Anime-Planet” database. After clicking the recommend button, the screen
will display a list of 5 shows related to the user’s input. In short, this program recommends shows or movies based on collaborative filtering and the theme is, in this
case, Anime shows/movies. So the goal of the program is to provide the user an outcome of shows or movies that have similar synopsis, titles, or tags from their favorite
or watched Animes. To achieve this machine learning goal, we have to go back to the previously mentioned “collaborative filtering” method. It’s an algorithm that offers
relevant suggestions based on user behavior. It can also use a content based system which utilizes similar ratings or likes to give similar suggestions as well. Before
we even apply those methods, we have to sort out the dataset first. To sort out and clean the data from the Anime-Planet database, we must import packages/modules that
will help us with the process. First and most important is we will use pandas to do the data processing with the csv files. Next we import the OS module to give us
functionality to our operating system like accessing file paths to a certain csv file. Then with sklearn we are going to import countvectorizer and cosine similarity.
These two modules specifically will be the main component of the so-called “suggestion” program. CountVectorizer is used to transform a given text into a vector on the
basis of the frequency of each word that occurs in the entire text. Using the vectors, cosine similarity is a method used to measure the difference between two non zero
vectors of an inner product space. It also measures the similarity between the vectors, for example, the program will use elements from columns such as name, synopsis,
tags, etc. After cleaning and sorting the data we will use a 3rd party python framework software called Streamlit to build a quick and easy UI frontend design. To use
Streamlit we will import the Streamlit module as well as miscellaneous modules like Pillow to import images to aid the appearance for the website. There will be one
function called “recommend” that will utilize the new dataset through a pkl file and will throw in the filtered input into empty lists. For example,
“recommended_anime_names = []” will be used to display the title of the Anime through Streamlit’s framework (st.title(f"{i+1})"+"Title  :  "+str(recommendations[i])) ).
