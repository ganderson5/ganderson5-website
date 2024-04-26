from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "GabeAndersonResume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GNEREAL SETTINGS ---
PAGE_TITLE = "Digital CV | Gabe Anderson"
PAGE_ICON = ":wave:"
NAME = "Gabe Anderson"
DESCRIPTION = """
Creativly, curiously, and passionately exploring ways to bring ideas to life. """

EMAIL = "anderson.gpb@gmail.com"
CONNECTIONS = {
  "LinkedIn":"https://www.linkedin.com/in/ganderson5/",
  "GitHub": "https://github.com/ganderson5",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
  st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
  PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
  st.image(profile_pic, width=230)

with col2:
  st.title(NAME)
  st.write(DESCRIPTION)
  st.download_button(
      label = "Download Resume",
      data = PDFbyte,
      file_name=resume_file.name,
      mime="application/octet-stream",
  )
  st.write("", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(CONNECTIONS))
for index, (platform, link) in enumerate(CONNECTIONS.items()):
    cols[index].write(f"[{platform}]({link})")

# ---EXPERIENCE & QUALIFICATIONS  ---
st.write("#")
st.subheader("About Me")
st.write(
    """
Hello, and welcome to my website! A little bit about me, I am a born and raised
Washingtonian currently living in Bellingham WA. I graduated from Eastern Washington Univeristy
in 2022 with a Bachelors of Science in Computer Science and a Minor in Cyber Security. 
In my free time, I love to be outside, be with friends, and be creative in many forms. 
I am a passionate learner and believe in my abilities to bring ideas to life. Please feel free 
to reach out via Linkedin or Email with any questions.
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
  """
- Programming: Java, Python, T-SQL, C++, Javascript
- Libraries: NumPy, Pandas, Matplotlib
- Framworks: React, Laravel, Flask, Streamlit
"""
)

# --- WORK HISTORY ---
st.write("#")
st.header(" Work History")
st.write("---")

# --- Koerber Supply Chain ---
st.write("##### Soltuion Consultant | Koerber Supply Chain")
st.write(" September 2022 - Present")
st.write(
  """
- Designing complex processes to improve efficiency, quality, and visibility of important customer data
- Developing data integrations to implement new pipelines throughout a warehouse management solution
- Continuously integrating enhancements and fixes into a production software solution
- Coordinating confidently with internal and external resources to assist or lead where needed
- Collaborating with customers to build an understanding of inefficiencies and an implementation to the solution
"""
)

# --- PNNL Techinical Intern ---
st.write("##### Technical Intern | Pacific Northwest National Labs")
st.write("June 2022 - August 2022")
st.write(
  """
- Developed a REST API to curate data between multiple interfaces
- Designed a responsive web application using React components and Bootstrap CSS
- Created data visualizations of chemical sensor data
- Collaborated remotely in an agile development environment with three other interns
"""
)

# --- Administration Program Specialst ---
st.write("##### Administration Program Specialist | Eastern Washington University")
st.write("September 2019 - June 2022")
st.write(
  """
- Developed webpages for the College of STEM’s internal and external websites
- Designed & implemented COVID-19 tracking system used by the university during 20-21 academic year
- Collaborated with faculty to transition work processes to an online setting during COVID-19 pandemic
"""
)

# --- Computer Science Tutor ---
st.write("##### Computer Science Tutor | Eastern Washington University")
st.write("June 2021 - July 2021")
st.write(
  """
- Assisted students in understanding fundamental coding concepts in Java, C, and OOP"""
)


