# Event_venue_booking
🎟️ Event Venue Booking — AI Agent

An AI-powered  college event venue booking system that helps users book and manage  venues through intelligent automation.
This project runs locally using ADK Web to serve an interactive browser-based interface for managing bookings with AI assistance.


---

🧠 Features

🤖 AI Agent for event venue  booking

🧩 Modular structure for managing sub-agents and tools

🌐 Local web interface using adk web

⚙️ Environment variable support with .env

📁 Organized architecture for scalability


Project Structure:
```
CampusAI/parent folder
├── manager/ root agent          
│   ├── __init__.py              
│   ├── agent.py                 
│   ├── .env                     
│   └── sub_agents/             
│       ├── __init__.py          
│       ├── availibity_checker/    
│       │   ├── __init__.py      
│       │   └── agent.py
|       |── available_locations/
|       |   ├── __init__.py      
│       │   └── agent.py
│       ├── external_info_agent/
│       │   ├── __init__.py
│       │   └── agent.py
│       ├── reservation_manager/
│       │   ├── __init__.py
│       │   └── agent.py
|   └── tools/
|       ├── __init__.py          
│       ├── tools_def/    
│       │   ├── __init__.py      
│       │   └── agent.py
|       │...
|
```


⚙️ Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/nidhi4gakki/Event_venue_booking.git
cd Event_venue_booking

2️⃣ (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies

From the campusAI folder:

pip install -r req.txt

If there’s a requirements.txt at the root, install that as well.

4️⃣ Configure Environment

Create a .env file at the project root:

OPENAI_API_KEY=your_key_here
OTHER_CONFIG=value


---

🚀 Run the Project Locally

1. Navigate to the root folder:

cd Event_venue_booking


2. Start the web server:

adk web


3. Open your browser at:

http://localhost:8000

(or whatever port is displayed in the terminal)


4. Interact with the AI Agent:

Ask to book venues, get availability, and manage events.

The system coordinates sub-agents and tools under campusAI/Manager/ for responses.





---

🧩 Folder Purpose Summary

Folder / File	Description

campusAI/	Main AI application module
campusAI/Manager/	Handles agent orchestration and management
campusAI/Manager/tools/	Contains helper functions (tools_def.py)
campusAI/Manager/sub_agents/	Houses modular AI sub-agents
.env	Stores environment variables
agent.py	Core agent setup
req.txt	Python dependencies



---

🛠️ Troubleshooting

❌ Error: adk not found → Install ADK via pip install adk.

⚠️ Missing keys or configs → Check .env file and variable names.

🐍 Python version → Use Python 3.8 or above.




