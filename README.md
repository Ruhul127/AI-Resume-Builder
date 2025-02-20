# AI Resume Builder

A web application that helps users create, edit, and improve their resumes using AI-powered suggestions. Built with **Flask**, **SQLAlchemy**, and **OpenAI**, this project allows users to manage multiple resumes, export them in PDF or Word formats, and receive AI-driven tips for improvement.

---

## Features

- **User Authentication**: Register and log in to manage your resumes securely.
- **Resume Management**: Create, edit, and delete resumes.
- **AI-Powered Suggestions**: Get tailored suggestions to improve your resume content and formatting.
- **Export Resumes**: Download your resume as a PDF or Word document with a single click.
- **Resume Tips**: Access general tips for creating a strong and effective resume.
- **Responsive Design**: Works seamlessly on desktop and mobile devices.

---

## Screenshots

### Home Page
![Home Page](AI_Resume_Builder/Assets/ProjectExample1.PNG)
The landing page of the application where users can learn about features and navigate to register or log in.

### Registration Page
![Registration Page](AI_Resume_Builder/Assets/ProjectExample2.PNG)
The sign-up page where users can create a new account to access the resume builder.

### Login Page
![Login Page](AI_Resume_Builder/Assets/ProjectExample3.PNG)
The login page where returning users can access their saved resumes.

### Dashboard
![Dashboard](AI_Resume_Builder/Assets/ProjectExample4.PNG)
A user dashboard displaying all created resumes with options to edit, delete, or create a new one.

### Create Resume
![Create Resume](AI_Resume_Builder/Assets/ProjectExample5.PNG)
The resume creation page where users can input job roles, experiences, and other details.

### AI Suggestions
![AI Suggestions](AI_Resume_Builder/Assets/ProjectExample6.PNG)
An AI-powered suggestion page that provides recommendations to improve the resume.

### Resume Tips
![Resume Tips](AI_Resume_Builder/Assets/ProjectExample7.PNG)
A page with general best practices for crafting an effective resume.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy)
- **AI Integration**: OpenAI API (GPT-3.5 Turbo)
- **PDF Generation**: ReportLab
- **Word Document Generation**: python-docx
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF and WTForms

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-resume-builder.git
   cd ai-resume-builder
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Run the application to automatically create the SQLite database:
     ```bash
     python app.py
     ```

4. **Set up OpenAI API Key**:
   - Replace the placeholder OpenAI API key in `app.py` with your own:
     ```python
     OPENAI_API_KEY = "your-openai-api-key-here"
     ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. **Register or Log In**:
   - Create a new account or log in with existing credentials.

2. **Create a Resume**:
   - Navigate to the "Create Resume" page and fill in the job role and resume content.

3. **Get AI Suggestions**:
   - Click "Get AI Suggestions" to receive tailored tips for improving your resume.

4. **Export Your Resume**:
   - Export your resume as a PDF or Word document using the respective buttons.

5. **View Resume Tips**:
   - Access general resume tips on the "Resume Tips" page.

6. **Manage Resumes**:
   - View, edit, or delete your resumes from the dashboard.

---

## Folder Structure

```
ai-resume-builder/
├── app.py                # Main application file
├── Assets/               # Screenshots of project
│   ├── ProjectExample1.PNG
│   ├── ProjectExample2.PNG
│   ├── ProjectExample3.PNG
│   ├── ProjectExample4.PNG
│   ├── ProjectExample5.PNG
│   ├── ProjectExample6.PNG
│   ├── ProjectExample7.PNG
├── instance/             
│   └── Resume_Builder.db # Database for project
├── Templates/            # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── resume.html
│   ├── suggestions.html
│   ├── resume_tips.html
├── Test API/             # API Testing Scripts
│   └── OpenAI_TestAPI.py
``` 
