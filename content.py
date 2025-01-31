import google.generativeai as genai
import os , json
from dotenv import load_dotenv
load_dotenv()

POST_PROMPT = """
Generate a compelling LinkedIn post for me, Murtaza Zaidi, a backend developer specializing in Python, Flask, and scalable web applications.

🎯 **Project Overview**  
Recently, I built a backend system that **[describe achievement or impact]** using:  
🔹 **Tech Stack**: Python, Flask, [Other Key Technologies]  
🔹 **Challenge**: [Briefly mention problem solved]  
🔹 **Solution**: [How I tackled it]  
🔹 **Outcome**: [Key results—performance, scalability, efficiency]  

Make the post **authentic, concise, and insightful** to engage professionals in the tech industry.  
✅ **End with a thought-provoking question** to encourage discussion.  
✅ Use **clear, professional language**—avoid excessive promotion.  
✅ Add **relevant hashtags** naturally to enhance visibility.  

⚡ Keep it within **160 characters**, engaging, and impactful. No filler text, only high-value content!  
"""


IMAGE_PROMPT = """
Generate a detailed **image prompt** for an AI image generator.  

The image should **visually represent the project’s key technologies and problem-solving aspects** in a **modern, engaging** way.  

### **Key Elements**  
- Highlight relevant **tech stack** (e.g., Python, Flask, APIs, databases)  
- Illustrate **workflow**, architecture, or automation in an intuitive way  
- Use **colorful yet professional** aesthetics  
- Keep it **clean, modern, and developer-friendly**  

### **Customization Based on Project Type**  
- If the project is **API-based**, focus on **API interactions & data flow**  
- If it's an **AI-powered project**, include **machine learning or automation elements**  
- If it's **web development**, show **backend/frontend communication**  

Ensure the **image prompt is clear and structured** so that an AI model can generate a **high-quality, visually appealing** image.  
Avoid generic descriptions and focus on **specific elements that make the project unique**.
Make it concise and to the point.  
Make the image on the basis of post content: 
"""

def generate_post_meta():
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    post_content = model.generate_content(POST_PROMPT)
    img_prompt = model.generate_content(IMAGE_PROMPT + post_content.text)
    return ({"post_content": post_content.text,"image_prompt":img_prompt.text})

# print("POST",generate_post_meta()["post_content"])
# print("IMAGE",generate_post_meta()["image_prompt"])