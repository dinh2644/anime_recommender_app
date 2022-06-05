import pandas as pd



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#file = pd.read_csv('/home/Light/Documents/Python/recommender_app/anime.csv')
file = pd.read_csv('/Users/Light/Documents/Python/recommender_app/anime.csv')
file = file.reset_index()
file.head()

file.columns

features = ['Rating Score','Number Votes','Studios','Synopsis', 'Tags', 'Episodes']

def combined_features(row):
    return str(row["Rating Score"])+" "+ str(row["Number Votes"])+" "+ str(row["Studios"])+" "+ str(row["Synopsis"])+" "+ str(row["Tags"])+" "+ str(row["Episodes"])+" "

def get_title_from_index(index):
    return file[file["index"] == index]["Name"].values[0]
def get_index_from_title(title):
    return file[file["Name"] == title]["index"].values[0]

file["combined_feature"]=file.apply(combined_features,axis=1)
file["combined_feature"].head()

cv = CountVectorizer()
count_matrix=cv.fit_transform(file["combined_feature"])

movie_liked_by_user = "Death Note"

cosine_sim = cosine_similarity(count_matrix)

liked_movie_index = cosine_sim[get_index_from_title(movie_liked_by_user)]
similar_anime = list(enumerate(liked_movie_index))
# similar_anime_sorted = sorted(similar_anime)
similar_anime.sort(key = lambda row: row[1],reverse=True)
# print(similar_anime)

for i in range(10):
    print(get_title_from_index(similar_anime[i][0]))
    
import pickle
pickle.dump(file.to_dict(),open('./animes_dict.pkl','wb'))
similarity=cosine_sim
pickle.dump(similarity,open('./similarity.pkl','wb'))
