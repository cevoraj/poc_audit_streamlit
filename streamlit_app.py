import streamlit as st
import time
from PIL import Image

#import streamlit_authenticator as stauth

col1, spacer, col2 = st.columns([1,6,1])

with col1:
    st.image("logo.png", width=100)

with col2:
    st.image("itau logo.png", width=100)


        
uploaded_file = st.file_uploader("Choose a file for brand audit")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
        
    # Display the image in Streamlit
    st.image(image, caption='Uploaded Image.',width=300)

    st.text_area("Campaign specific brief",value="Optional", height=100)
if uploaded_file is not None:
    if st.button("Run audit"):
        time.sleep(8)

        st.markdown("## Tone of Voice Analysis\n\nFlag: 🟧\n\n✅ Strengths:\n* Energetic Call-to-Action: The phrase 'COMPRE AGORA' is direct and energetic, encouraging immediate response, aligning well with the brand's emphasis on enthusiasm.\n* Clear Value Proposition: The statement 'PAGUE COM PIX E ECONOMIZE 7%!' is straightforward and highlights a benefit, which is effective for engaging customers.\n\n❌ Weaknesses:\n* Lack of Inspirational Language: The ad lacks the use of uplifting and motivational language that aligns with the brand's aspirational tone, missing an opportunity to inspire the audience.\n* Minimal Emotional Engagement: There are no vivid metaphors or imagery, which are recommended for creating a deeper emotional connection with the audience.\n\n**Summary**: The advertisement effectively uses an energetic tone in its call-to-action, aligning with aspects of the brand's tone of voice. However, it misses out on integrating inspirational language and emotional elements that could enhance engagement and align more with the brand's aspirational and inclusive guidelines. To better adhere to the brand's tone, incorporating motivational language and vivid imagery could be beneficial.")

        time.sleep(8)

        st.markdown("## Visual Identity Analysis\n\nFlag: 🟩 \n\n✅ Strengths: \n* The logo 'WAAW' is prominently used and positioned correctly according to the guidelines.\n* Font and color choices closely match the brand's visual identity guidelines, particularly the use of Pantone 388 C.\n* The imagery captures a music-related theme, resonating well with the brand's ethos.\n\n❌ Weaknesses:\n* No significant weaknesses are identified as the asset aligns well with the guidelines.\n\nSummary:\n\nThe asset aligns well with the brand's visual identity guide, effectively utilizing the logo, appropriate colors, and fonts. It visually communicates the brand's connection to music and lifestyle effectively.")

        time.sleep(8)

        st.markdown("## Colour Analysis\n\nFlag: 🟧\n\n✅ Strengths:\n* Strong Use of Black: The predominant use of black (#000000) aligns effectively with the brand's primary color palette, providing a modern and elegant look.\n* Consistent Yellow Tones: The use of yellow shades, such as #dee61d and #dee61b, are within reasonable proximity to the specified brand palette, helping to maintain visual alignment.\n\n❌ Weaknesses:\n* Overuse of Non-Brand Neutral Tones: There is a notable presence of various non-branded dark tones like #010101 and #020000, which could diverge from the prescribed color scheme.\n* Limited Use of Specified Secondary Colors: The asset shows limited usage of brand-specified secondary colors, which reduces brand color richness and cohesiveness.\n* Summary: The asset effectively employs black as a primary color, maintaining alignment with the brand's guidelines. However, the over-reliance on unsanctioned neutral shades and insufficient integration of other specified secondary colors could diminish overall brand visual coherence. Further refinement in color use would enhance the asset's adherence to the brand's defined color strategy.")

