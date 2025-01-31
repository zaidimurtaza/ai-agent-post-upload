# AI Agent for Automatic Post Upload on X.com

## Overview
This project is an AI-powered agent that automates the process of creating, uploading, and managing posts on X.com (formerly Twitter). By leveraging AI for content generation and Selenium for automation, this agent creates posts based on predefined prompts or conditions, uploads them with images, and schedules them for later publishing. The agent is designed to streamline content creation, boost engagement, and enhance social media presence on X.com.

## Features
- **AI Content Generation:** Utilizes a natural language processing model to generate content based on user-defined prompts or conditions.
- **Automatic Posting:** Automatically uploads generated content to your X.com account using Selenium for web automation.
- **Image Uploading:** The agent can upload images along with the posts using the Cryon service to enhance engagement.
- **Post Scheduling:** Schedule posts at specific times or trigger them based on set conditions.
- **Customizable Prompts:** Provides flexibility for users to define specific prompts to guide the AI in creating content.
- **Easy-to-Use Interface:** Simply configure the environment variables and run the script to start posting automatically.

## Tech Stack
- **Programming Language:** Python
- **AI Model:** [Specify the AI model used, e.g., OpenAI GPT, custom model, etc.]
- **Automation Tool:** Selenium (used for automating post uploads)
- **Image Uploading Service:** Cryon (for uploading images to posts)
- **Scheduling Library:** `schedule` (for managing post timings)
- **Environment Management:** `dotenv` (for managing environment variables)
- **Web Scraping:** `beautifulsoup4` (optional, for extracting additional data or media if required)

## Prerequisites
- Python 3.x
- X.com credentials (username and password)
- Cryon API key (for image uploads)
- Optional: OpenAI API key (for content generation if using GPT models)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-agent-post-upload.git
   cd ai-agent-post-upload
2. **Create a virtual environment(optional but recommended):**

```bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## Install the dependencies:

```bash
Edit
pip install -r requirements.txt
```
Set up your environment variables: Create a .env file in the root of the project and add the following keys:

makefile
```bash
Edit
USER="Your X Username"
PASSWORD="Your X Password"
CRYON_API_KEY="Your Cryon API Key"
OPENAI_API_KEY="Your OpenAI API Key"  # If using OpenAI for content generation
```
