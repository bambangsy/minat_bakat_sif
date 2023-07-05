import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 

question = [
    "Anda menguasai Figma/AdobeXD",
    "Anda tertarik membuat design tampilan dari Web/Mobile",
    "Anda bisa membedakan design web/mobile yang menarik dan tidak",
    "Anda sering melihat design-design UI/UX di sosial media",
    "Anda mengetahui bedanya UI dan UX",
    "Anda berminat mebuat portfolio design web/mobile",
    "Anda suka dengan analisis data",
    "Anda menguasai bahasa python",
    "Anda menguasai pemrograman dasar (Loop, Conditional, Fungsi)",
    "Anda tertarik mempelajari machine learning",
    "Anda tertarik untuk mengolah data untuk pengambilan keputusan",
    "Anda tertarik untuk mengolah data penelitian",
]
answer = [0,0,0,0,0,0,0,0,0,0,0,0]
h = ["nama",0,1,2,3,4,5,6,7,8,9,10,11,"minat"]
feature = [0,1,2,3,4,5,6,7,8,9,10,11]


for i in range(len(question)):
    answer[i]  = st.slider(question[i],1,4)
file = pd.read_csv("train.csv")
file = file.rename(columns=dict(zip(file.columns, h)))
x = file[feature]
y = file["minat"]


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x,y)

test = pd.DataFrame(data=[answer])
   

if st.button('PREDICT!'):
    y_pred = clf.predict(test)
    st.title("You're into "+ str(y_pred[0]))

else:
    st.write('')


