import mysql.connector
import openai
import streamlit as st
import re
import nltk
from nltk.tokenize import word_tokenize

# Set your OpenAI API key
openai.api_key = 'sk-proj-96WTk0dHUR7DShjc80L1T3BlbkFJWYH2EKhtzzy34vqICQCH'

# Download NLTK resources
nltk.download('punkt')

# Function to fetch candidates from the database based on job description keywords
def fetch_candidates_from_db(job_description_keywords):
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="candidates_db"
    )
    cursor = db_conn.cursor(dictionary=True)

    query = """
    SELECT name, contact_details, job_skills, experience, location, projects FROM candidates
    WHERE MATCH(job_skills, experience, projects) AGAINST (%s IN NATURAL LANGUAGE MODE)
    """
    cursor.execute(query, (job_description_keywords,))
    candidates = cursor.fetchall()
    
    cursor.close()
    db_conn.close()
    return candidates

def extract_experience(experience_str):
    match = re.search(r'(\d+)', experience_str)
    return int(match.group(1)) if match else 0

# Function to calculate the score for each candidate using the fine-tuned model
def calculate_score(candidate, job_description):
    # Extract skills required from job description
    job_skills = re.findall(r'\b(?:HTML|CSS|JavaScript|React|Angular|Python|R|TensorFlow|PyTorch|AWS|Azure|Google Cloud)\b', job_description)
    
    # Calculate the number of matching skills
    candidate_skills = candidate.get("job_skills", "").split(", ")
    matching_skills = len(set(candidate_skills) & set(job_skills))
    
    # Create a prompt for the fine-tuned model
    prompt = f"""
    Candidate Details:
    Name: {candidate['name']}
    Skills: {candidate['job_skills']}
    Experience: {candidate['experience']}
    Location: {candidate['location']}
    Projects: {candidate['projects']}
    
    Job Description:
    {job_description}
    
    Score this candidate on a scale of 0 to 100 based on the job description.
    """
    response = openai.Completion.create(
        model="ft:gpt-3.5-turbo-1106:personal::9pgH3AKW",
        prompt=prompt,
        max_tokens=10
    )
    score_text = response.choices[0].text.strip()
    score = re.search(r'\d+', score_text)
    return {
        "score": int(score.group(0)) if score else 0,
        "matching_skills": matching_skills
    }

# Function to extract details from the job description
def extract_job_description_details(job_description_text):
    skills_pattern = r'\b(?:HTML|CSS|JavaScript|React|Angular|Python|R|TensorFlow|PyTorch|AWS|Azure|Google Cloud)\b'
    skills = re.findall(skills_pattern, job_description_text)
    experience_match = re.search(r'(\d+)\s*years', job_description_text)
    experience = int(experience_match.group(1)) if experience_match else 0
    location_match = re.search(r'\b(New York|San Francisco|Los Angeles|San Jose|Seattle|Austin|Boston|Chicago|Houston|Phoenix|Dallas)\b', job_description_text)
    location = location_match.group(1) if location_match else ""

    num_candidates = extract_number_of_candidates(job_description_text)

    return {
        "skills": skills,
        "experience": experience,
        "location": location,
        "num_candidates": num_candidates
    }

def extract_number_of_candidates(job_description_text):
    match = re.search(r'\b(\d+)\s*(?:candidates?|profiles?|people|persons)\b', job_description_text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 10  # Default to 10 if no specific number is mentioned

def main():
    st.title("Candidate Matching System")

    job_description_text = st.text_area("Enter job description:")
    if st.button("Find Matching Candidates"):
        if job_description_text:
            # Extract job description details
            job_description = extract_job_description_details(job_description_text)
            job_description_keywords = " ".join(job_description_text.split())
            
            # Fetch candidates from database
            candidates = fetch_candidates_from_db(job_description_keywords)
            
            if candidates:
                # Calculate scores for each candidate
                for candidate in candidates:
                    scores = calculate_score(candidate, job_description_text)
                    candidate["score"] = scores["score"]
                    candidate["matching_skills"] = scores["matching_skills"]

                # Sort candidates based on matching skills and then by their scores
                sorted_candidates = sorted(candidates, key=lambda x: (x["matching_skills"], x["score"]), reverse=True)
                
                # Get the required number of candidates or default to 7
                num_candidates = job_description["num_candidates"]
                top_candidates = sorted_candidates[:num_candidates]
                
                st.subheader("Matching Candidates:")
                for idx, candidate in enumerate(top_candidates, start=1):
                    st.markdown(f"### Candidate {idx}")
                    st.markdown(f"**Name:** {candidate['name']}")
                    st.markdown(f"**Contact Details:** {candidate['contact_details']}")
                    st.markdown(f"**Skills:** {candidate['job_skills']}")
                    st.markdown(f"**Years of Experience:** {candidate['experience']}")
                    st.markdown(f"**Location:** {candidate['location']}")
                    st.markdown(f"**Projects:** {candidate['projects']}")
                    st.write("\n")
            else:
                st.write("No candidates found matching the job description.")
        else:
            st.write("Please enter a job description.")

if __name__ == "__main__":
    main()
