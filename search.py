
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.model.groq import Groq
from prompt import user_prompt, instruction, task, output, role

from phi.storage.agent.sqlite import SqlAgentStorage
storage = SqlAgentStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_file: Sqlite database file
    db_file="tmp/data.db",
)

#from pydantic import BaseModel, Field
#from typing import List, Dict, Any, Tuple, Optional
#import re
#import nltk
from dotenv import load_dotenv

# Download necessary NLTK data
#nltk.download('punkt', quiet=True)
#nltk.download('stopwords', quiet=True)

# Load environment variables
load_dotenv()


duck_agent = Agent(
    #work on the prompt template
    description=role,
    instructions=instruction,
                 
    task = task,
    expected_output = output,
    add_datetime_to_instructions = True,
    markdown=True,
    debug_mode=True,
    
    
    
    #the duckduckgo search
    tools=[DuckDuckGo(search=True)], show_tool_calls=True,
    
    
    #set and customize the LLM the llm
    model=Groq(id="llama-3.3-70b-versatile"),
    temperature = 0.2,
    
    #storage
    storage = SqlAgentStorage(table_name="duck", db_file="agents.db")
    )




google_agent = Agent(
    tools=[GoogleSearch()],
    description=role,
    instructions=instruction,
    task = task,
    expected_output= output,
    show_tool_calls=True,
    debug_mode=True,
    model=Groq(id="llama-3.3-70b-versatile"),
    temperature = 0.2,
    storage = SqlAgentStorage(table_name="google", db_file="agents.db")
)
google_agent.print_response(user_prompt, markdown=True)