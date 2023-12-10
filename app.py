import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

#Load Lottie
def load_lottie(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	else:
		return r.json()

#Assets 
lottie_animation = load_lottie("https://assets1.lottiefiles.com/packages/lf20_e9agpwqm.json")
css_file = "style/style.css"
icon = "images/brand/Icon.png"
link = "https://www.youtube.com/channel/UClWfHFKqd-KYEVo5t0uC33w"
img_locomotive = Image.open("images/arts/Locomotive.png")
img_castle = Image.open("images/arts/Castle.png")

#Local CSS
def local_css():
	with open(css_file) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Configuration
st.set_page_config(page_title = "SpaceFox", page_icon=icon, layout="wide")
local_css()

#Header-Section
with st.container():
	st.subheader("Hello, SpaceFox Here :wave:")
	st.title("Creative Hobbyist from Britain")
	st.write("I enjoy making Photoshop designs and coding fun projects with Python.")
	st.write(f"[Learn More]({link})")

#About-Section
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What is this website?")
		st.write("##")
		st.write("""
			I am aspiring to document all of the learning that I go through on my journey:
			- Creating Photoshop Logos
			- Creating photo manipulations in Photoshop
			- Coding projects with Python
			- Blogging
			""")
	with right_column:
		st_lottie(lottie_animation, height=300, key="Lottie")

#Project-Section
with st.container():
	st.write("---")
	st.header("My Work")
	st.write("##")
	img_column, txt_column = st.columns(2)
	with img_column:
		st.image(img_locomotive)
	with txt_column:
		st.subheader("3D Locomotive")
		st.write("Stunning 3D Locomotive photo manipulation with Photoshop!")
with st.container():
	img_column, txt_column = st.columns(2)
	with img_column:
		st.image(img_castle)
	with txt_column:
		st.subheader("Fantasy Castle")
		st.write("Visually pleasing fantasy castle design with Photoshop!")

#Contact-Section
with st.container():
	st.write("---")
	st.header("Get In Touch")
	st.write("##")
	#Form-Submit-Form
	contact_form = """
	<form action="https://formsubmit.co/abzwemail@gmail.com" method="POST">
		<input type="hidden" name="captcha" value="false">
		<input type="text" name="name" placeholder="Your Name" required>
		<input type="email" name="email" placeholder="Your Email" required>
		<textarea name="message" placeholder="Your Message" required></textarea>
		<button type="submit">Send</button>
	</form>
	"""
	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st.empty()

# Footer
with st.container():
	st.write("")
	st.markdown(
		"""
		<div style="text-align: center; padding: 1em;">
			&copy; 2023 SpaceFox
		</div>
		""",
		unsafe_allow_html=True
	)