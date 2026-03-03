import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("cv.txt", "r", encoding="utf-8") as f:
    cv_text = f.read()

job_description = """
Operations Manager in Kolkata.
Need team handling, customer service, vendor management.
"""

prompt = f"""
Compare this CV and job description.

Give:
1. Match score (0-100)
2. 2 line explanation
3. 3 improvement suggestions

CV:
{cv_text}

JOB:
{job_description}
"""

response = client.models.generate_content(
    model="gemini-1.0-pro",
    contents=prompt,
)

print(response.text)
