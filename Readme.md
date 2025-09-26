Project: EduPulse – The Parent AI Agent for Student Progress - Hackathon project
    Goal: Build a CLI/notebook tool that queries education data (Snowflake), analyzes it with AI agents (CrewAI), and generates rich narrative reports (Writer) based on structured + unstructured data.

Project Requirement: 

Parents or teacher should be able to see the daily progress and recommendations. AI based pattern recommendations.
The parent should be able to see daily progress details of kid's work. 
They should be able to see if kid need help for specific subject or component in specific subject.

Need to see KPIs at daily, weekly, monthly, semester wise, annually.

The student data needs to be collected and stored for every subject, every year with analytics and personal recommendations. So that parents/teachers can get recommendations on career path for the student as they progress school grades.

If the videos of their science project or other curricular activities are uploaded they should be able to see suggestions from LLM for their career path or more activities kid should be focusing on?

Ensure: Subject are broken down with components in detail for the student to focus on.

Roles for the project: Parent and Tutor


👥 Team Breakdown – 4 People, 4 Roles
1. The Data Engineer – “The Snowflake Whisperer”
Goal: Ingest + organize multimodal student data in Snowflake.
Tasks:
    • Set up Snowflake schema: Student basic information, Assessments, Grades, Media Metadata
    • Write SQL to simulate data ingestion from:
        ○ ParentVue (grades, attendance)
        ○ iReady (scores, progress)
        ○ Google Drive (lesson plan summaries, PDFs)
        ○ LandingAI (media metadata)

2. The AI Agent Engineer – “The Crew Chief”
Goal: Build CrewAI agents that explore Snowflake and answer parent questions.
Tasks:
    • Define agent personas (e.g., “Parent Assistant”)
    • Create prompt logic for:
        ○ Daily summaries (“How is my child doing today?”)
        ○ Weekly analysis (“What trends should I know?”)
        ○ Subject strength queries (“Which subject is their strongest?”)
    • Integrate with Snowflake using SQL toolkits

3. The Narrative Specialist – “The Word Wizard”
Goal: Use Writer (or LLM) to turn raw analytics into empathetic parent-friendly narratives.
Tasks:
    • Take sample data from agent output
    • Build prompt templates like:
        ○ "Write a weekly student progress summary in a warm, encouraging tone."
        ○ "Generate a career suggestion summary based on performance and interests."
    • Format final output into Markdown + export as PDF

4. The Demo Master – “The Showrunner”
Goal: Pull everything together into a killer CLI demo or notebook.
Tasks:
    • Design CLI commands: summarize, generate-report, etc.
    • Add simple UX polish (colors, emojis, clean layout)
    • Script and record the 1-minute walkthrough
    • Handle packaging, README, and GitHub polish
