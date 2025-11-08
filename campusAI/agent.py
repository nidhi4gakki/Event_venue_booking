from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from Manager.sub_agents.availability_checker.agent import availability_checker
from Manager.sub_agents.reservation_manager.agent import reservation_manager
from Manager.sub_agents.external_info_agent.agent import external_info_agent
from Manager.sub_agents.available_locations.agent import available_locations
from Manager.tools.tools_def import current_time 


root_agent = Agent (
    name="Manager",
    model="gemini-2.0-flash",
    description="Campus location booking Manager",
    instruction=""" 
    "You are a manager agent that is responsible for the Campus Club's Event Booking System.
 Your goal is to process user requests by delegating tasks to your specialized sub-agents and tools.
 Always delegate the task to the appropriate agent. Use your best judgement 
 to determine which agent to delegate to.
  You are responsible for delegating tasks to this manner:
  1. Analyze the user's intent: Is it a simple question, a check for availability, a booking, or a request for external info?
  2. if the user asks for any external information other than details related to booking or if the user tells to do web search,use the external_info_agent tool.
  3. if the user is checking availability, delegate to the availability_Checker.
  4. If the user is requesting a new booking, delegate to the reservation_Manager.
  5. Construct all information into a clear, helpful response. """,

  sub_agents=[availability_checker, reservation_manager, available_locations],
  tools=[AgentTool(external_info_agent),
         FunctionTool(current_time)
        ]
)