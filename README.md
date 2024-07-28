# Interactly-task-Kushal-Desai
# Candidate Matching System

This project is a candidate matching system that utilizes OpenAI's GPT-3.5-turbo model, Streamlit for the user interface, MySQL for data storage, and NLTK for natural language processing. The system allows users to input a job description and fetch the best-matched candidates from a database based on the job description details.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Set Up NLTK](#set-up-nltk)
  - [Database Configuration](#database-configuration)
  - [Set Your OpenAI API Key](#set-your-openai-api-key)
- [Running the Application](#running-the-application)
- [Using the Application](#using-the-application)
- [Code Overview](#code-overview)
  - [`fetch_candidates_from_db(job_description_keywords)`](#fetch_candidates_from_dbjob_description_keywords)
  - [`extract_experience(experience_str)`](#extract_experienceexperience_str)
  - [`calculate_score(candidate, job_description)`](#calculate_scorecandidate-job_description)
  - [`extract_job_description_details(job_description_text)`](#extract_job_description_detailsjob_description_text)
  - [`extract_number_of_candidates(job_description_text)`](#extract_number_of_candidatesjob_description_text)
  - [`main()`](#main)
- [License](#license)

## Requirements

- Python 3.8 or higher
- MySQL server
- Streamlit
- OpenAI API key
- NLTK

## Setup

### Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
