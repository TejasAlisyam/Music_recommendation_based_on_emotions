import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image,ImageOps
import webbrowser

st.header("Emotion Based Music Recommendation System")
st.set_option("deprecation.showfileUploaderEncoding",False)
#@st.cache(allow_output_mutation=True)

CNN_Model = load_model('Emotion_Recognition_CNN_Model.h5')
Labels = ['Angry','Scared','Happy','Calm','Sad']

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

try:
	Uploaded_Image = Image.open(User_Image)
	st.image(Uploaded_Image,use_column_width=True)
	val = load_image_and_predict(Uploaded_Image,CNN_Model)
	Emotion = Labels[val]

	if button:
		if not(Emotion):
			st.warning("Please let me capture your emotion properly")
		else:
			if Language == "None" and Singer == "None":
				webbrowser.open(f"https://www.youtube.com/results?search_query=songs+to+listen+to+when+you+are+{Emotion}")#Always Use Formatted String.
			elif Language == "None":
				webbrowser.open(f"https://www.youtube.com/results?search_query=songs+to+listen+to+when+you+are+{Emotion}+by+{Singer}")
			elif Singer == "None":
				webbrowser.open(f"https://www.youtube.com/results?search_query=songs+to+listen+to+when+you+are+{Emotion}+in+{Language}")
			else:
				webbrowser.open(f"https://www.youtube.com/results?search_query=songs+to+listen+to+when+you+are{Emotion}+by+{Singer}+in+{Language}")
except:
	print("Please choose the image first!")