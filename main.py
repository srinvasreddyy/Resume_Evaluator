from pathlib import Path
import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key :
    raise ValueError("Api key is not configured in the env file")

client = Groq(api_key=api_key)

# Step 1 defining the JD parsing schema

class JD(BaseModel):
    role : str
    required_skills : list
    preffered_skills : list
    experience_required : str
    educational_qualification : str
    responsibilities : str
    additional_information : str
    timelines : str
    location_data : str

schema = JD.model_json_schema()

job_description = """
SDE I Intern , Amazon University Talent Acquisition
Job ID: 10541345 | ADCI - Karnataka
Description
Software Development Engineer 6 months Internship – 2027 (In-Person)

Introduction
At Amazon, we hire the best minds in technology to innovate and build on behalf of our customers. The intense focus we have on our customers is why we are one of the world’s most beloved brands – customer obsession is part of our company DNA. Our interns write real software and collaborate with a select group of experienced software development engineers (SDEs) who guide interns on projects that matter to our customers. As an intern, you will be matched to a manager and a mentor. You will have the opportunity to influence the evolution of Amazon technology and lead mission critical projects early in your career. Your design, code, and raw smarts will contribute to solving some of the most complex technical challenges in the areas of distributed systems, data mining, automation, optimization, scalability, and security – just to name a few. In addition to working on an impactful project, you will have the opportunity to engage with Amazonians for both personal and professional development, expand your network, and participate in activities with other interns throughout your internship. No matter the location of your internship, we give you the tools to own your project and learn in a real-world setting. Many of our technologies overlap, and you would be hard pressed to find a team that is not using Amazon Web Services (AWS), touching the catalogue, or iterating services to better personalize for customers. If this opportunity interests you, apply and come chart your own path at Amazon.

Job location
By applying to this position your application will be considered for all locations we hire for in India. This includes but is not limited to Bengaluru, Chennai, Hyderabad, Delhi, Mumbai and Pune.

Duration and Timelines
Amazon internships are full-time (40 hours/week) for 24 - 26 consecutive weeks (six months) with start dates between January - June 2027

Please note that Amazon internships require full-time commitment during the duration of the internship. During the course of internship, interns should not have any conflicts including but not limited to academic projects, classes or other internships/employment. Any exam related details must be shared with the hiring manager to plan for absence during those days. Specific team norms around working hours will be communicated by the hiring/ reporting manager at the time of commencement of internship. Candidates receiving internship will be required to submit declaration of their availability to complete the entire duration of internship duly signed by a competent authority at their University. Internship offer will be subjected to successful submission of the declaration.

Key job responsibilities
• Collaborate with experienced cross-disciplinary Amazonians to conceive, design, and bring innovative products and services to market.
• Design and build innovative technologies in a large distributed computing environment, and help lead fundamental changes in the industry.
• Create solutions to run predictions on distributed systems with exposure to innovative
technologies at incredible scale and speed.
• Build distributed storage, index, and query systems that are scalable, fault-tolerant, low cost, and easy to manage/use.
• Ability to design and code the right solutions starting with broadly defined problems.
• Work in an agile environment to deliver high-quality software.

Basic Qualifications
- Knowledge of computer science fundamentals such as object-oriented design, operating systems, algorithms, data structures, and complexity analysis
- Knowledge of programming languages such as C/C++, Python, Java or Perl
- Currently enrolled in a Bachelor’s or Master’s Degree in Computer Science, Computer Engineering, or related field at time of application -Year of Graduation 2027

Preferred Qualifications
- Previous technical internship(s).
- Experience with distributed, multi-tiered systems, algorithms, and relational databases.
- Experience in optimization mathematics such as linear programming and nonlinear optimization.
- Effectively articulate technical challenges and solutions.
- Adept at handling ambiguous or undefined problems as well as ability to think abstractly.

Our inclusive culture empowers Amazonians to deliver the best results for our customers. If you have a disability and need a workplace accommodation or adjustment during the application and hiring process, including support for the interview or onboarding process, please visit https://amazon.jobs/content/en/how-we-hire/accommodations for more information. If the country/region you’re applying in isn’t listed, please contact your Recruiting Partner.
"""

system_prompt = f"""You are a expert HR assistant ,your task is to extract the information from the job description and return it in a strictly structured JSON format according to the following schema:{schema} and give me a json output"""

system_message = {"role" : "system", "content" : system_prompt}

user_prompt = f"""extract the information from the job description {job_description}."""

user_message =  {
    "role" : "user",
    "content" : user_prompt
}

response_format = {
    "type" : "json_object"
}

response = client.chat.completions.create(
    model = "qwen/qwen3.8-27b",
    messages = [system_message, user_message],
    response_format = response_format,
    max_tokens = 512
)

answer = response.choices[0].message.content
print(answer)



# Step 2 defining the resume parsing schema

class Experience(BaseModel):
    company_name : str
    role : str
    duration : str
    description : str
    skills_used : list

class Education(BaseModel):
    Title : str
    institution : str
    duration : str
    description : str
    grades : str

class Project(BaseModel):
    Title : str
    description : str
    skills_used : list
    link : str

class Links(BaseModel):
    platform : str
    link : str

class Resume(BaseModel):
    name : str
    email : str
    phone_number : str
    social_links : list[Links]
    skills : list
    total_years_of_experience : float
    experiences : list[Experience]
    educations : list[Education]
    projects : list[Project]
    certifications : list
    additional_information : str

resume_schema = Resume.model_json_schema()

# Reading resumes

