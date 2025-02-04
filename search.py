
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from prompt import user_prompt, instruction, task, output, role

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


agent = Agent(
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
    )


agent.print_response(user_prompt)