import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image,ImageOps
import webbrowser

st.header("Emotion Based Music Recommendation System")
st.set_option("deprecation.showfileUploaderEncoding",False)

CNN_Model = load_model('3_Emotion_Recognition_CNN_Model.h5')
Labels = ['Calm','Happy','Sad']

Language = st.text_input("Please Select your preferred Language(If No Preference Enter None)") #Collecting the Language Prefernce of the User as Input.
Singer = st.text_input("Please Select your Favourite Singer(If No Preference Enter None)") #Collecting the Language Prefernce of the User as Input.

st.write("""
         # Emotion Based Music Recommendation
				 """)

User_Image = st.file_uploader("Please Choose an Image",type=["jpg","png"])

def load_image_and_predict(image_data,Model):
  size = (96,96)
  #image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
  img = image_data.resize(size)
  img = np.asarray(img)
  img_reshape = img[np.newaxis,...]
  prediction = Model.predict(img_reshape)
  emotion = np.argmax(prediction)
  return emotion

button = st.button("Recommend me some songs according to my mood")

#try:
#	Uploaded_Image = Image.open(User_Image)
#	st.image(Uploaded_Image,use_column_width=True)
#	val = load_image_and_predict(Uploaded_Image,CNN_Model)
#	Emotion = Labels[val]
#
#	if button:
#		link_1 = ""
#		if not(Emotion):
#			st.warning("Please let me capture your emotion properly")
#		else:
#			if Language == "None" and Singer == "None":
#				link_1 = f"https://www.youtube.com/results?search_query=+{Emotion}+songs"
#				st.write("Click the link to listen to the song [link](link_1)")
#				#st.markdown(link_1,unsafe_allow_html=True)
#				#text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + str(Emotion) + "songs"
#				#st.text(text)
#			elif Language == "None":
#				link_1 =f"https://www.youtube.com/results?search_query={Singer}+{Emotion}+songs"
#       #st.markdown(link_1,unsafe_allow_html=True)		
#        #text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + str(Singer) + str(Emotion) + "songs"
#        #st.text(text)	
#			elif Singer == "None":
#				link_1 = f"https://www.youtube.com/results?search_query=+{Language}+{Emotion}+songs"
#				st.write("Click the link to listen to the song [link](link_1)")
#			  #st.markdown(link_1,unsafe_allow_html=True)
#			  #text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + str(Language) + str(Emotion) + "songs"
#			  #st.text(text)
#			else:
#				link_1 = f"https://www.youtube.com/results?search_query=+{Language}+{Singer}+{Emotion}+songs"
#				st.write("Click the link to listen to the song [link](link_1)")
#				#st.markdown(link_1,unsafe_allow_html=True)
#				#text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + str(Language) + str(Singer) + str(Emotion) + "songs"
#				#st.text(text)

try:
	Uploaded_Image = Image.open(User_Image)
	st.image(Uploaded_Image,use_column_width=True)
	val = load_image_and_predict(Uploaded_Image,CNN_Model)
	Emotion = Labels[val]

	if button:
		text = ""
		if not(Emotion):
			st.warning("Please let me capture your emotion properly")
		else:
			if Language == "None" and Singer == "None":
				text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + "songs+to+listen+to+when+you+are+" + str(Emotion) #+  "songs"
				st.text(text)
			elif Language == "None":
				text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + "songs+to+listen+to+when+you+are+" + str(Emotion) + "+by+" + str(Singer) 
				st.text(text)
			elif Singer == "None":
				text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query=" + "songs+to+listen+to+when+you+are+" + str(Emotion) + "+in+" + str(Language)
				st.text(text)
			else:
				text = "Open the Link and Enjoy the Song : " + "https://www.youtube.com/results?search_query="  + "songs+to+listen+to+when+you+are+" + str(Emotion) + "+in+" + str(Language) + "+by+" + + str(Singer)
				st.text(text)

except:
	print("Please choose the image first!")