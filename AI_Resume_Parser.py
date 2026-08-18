import json
import os

from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class ExperienceDetails(BaseModel):
    company_name: str = Field(description="Company Name of the Candidate that he has previously worked for or is Currently working for")
    role_name: str = Field(description="Role Name of the Candidate at that Company")
    start_date: str = Field(description="Start Date of the Candidate at that Company")
    end_date: str = Field(description="End Date of the Candidate at that Company")
    description: str = Field(description="Description or Summary of the Work that the Candidate has done at that Company")

class ProjectDetails(BaseModel):
    pass

class SkillDetails(BaseModel):
    pass

class EducationDetails(BaseModel):
    pass

class CandidateDetails(BaseModel):
    name: str = Field(description="Name of the Candidate")
    role_description: str = Field(description="Description of the Role and/or Field of the Candidate")
    experience: float = Field(description="Work Experience in Float/Decimal Value of the Candidate")
    email_id: str = Field(description="Email ID of the Candidate")
    mobile_no: str = Field(description="Mobile Number of the Candidate", default=None)
    linkedin_id: str = Field(description="LinkedIn Profile URL of the Candidate", defualt=None)
    github_id: str = Field(description="GitHub Profile URL of the Candidate", default=None)
    profile_summary = Field(description="Profile Summary or Description of the Candidate")
    experience_details: List[ExperienceDetails] = Field(description="List of all the Professional Experiences of Candidate")
    project_details: List[ProjectDetails] = Field(description="List of all the Project Details of the Candidate")
    skill_details: List[SkillDetails] = Field(description="List of all the Skills of the Candidate")
    education_details: List[EducationDetails] = Field(description="List of all the Education Details of the Candidate")