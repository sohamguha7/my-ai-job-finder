import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read your CV
with open("cv.txt", "r", encoding="utf-8") as f:
    cv_text = f.read()

# Example job (you can change this later)
job_description = """
Operations Manager in Kolkata.
Need team handling, customer service, vendor management.
"""

prompt = f"""
Compare this CV with job description.
Give match score from 0-100.
Explain in 2 lines.

CV:
{cv_text}

JOB:
{job_description}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
