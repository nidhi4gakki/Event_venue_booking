from google.adk.tools import google_search
from google.adk.agents import Agent

external_info_agent = Agent(
    name="external_info_agent",
    model="gemini-2.0-flash",
    description="Specializes in searching the web for external or up-to-date campus news, policies, or event information using the built-in Google Search tool.",
    instruction="""You are a campus information specialist. Always use the google_search tool to find external information before responding.
        the purpose is get external information, like campus policy updates or unexpected closures, that might affect a booking request.
                        """ ,
    tools=[google_search]
)