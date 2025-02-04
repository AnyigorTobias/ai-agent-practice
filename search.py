
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq

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
    description="You are an expert career consultant",
    instructions=[
                  "Use your superior SEO skills to search the web for solutions",
                  "Let your recommendation contain links to the each opportunity",
                  "Ensure that the recommendations have not exceeded deadline dates",
                  "search www.opportunitiesforafricans.com",
                  "search www.opportunitydesk.com",
                  
    ],
                 
    task = "Recommend the best 10 opportunitties to the user",
    expected_output = "Present your result in a tabular form. Let the recommendation move from the most suitable opportunity to the less suitable one, add the deadline dates, remember to display the dates",
    add_datetime_to_instructions = True,
    markdown=True,
    debug_mode=True,
    
    
    
    #optimize the duckduckgo search
    tools=[DuckDuckGo(search=True)], show_tool_calls=True,
    
    
    #optimize the llm
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    temperature = 0.3 )




agent.print_response("Recommend latest opportunities for a 27year old male bachelor with a degree in Chemical engineering, data science certificatiosn and interest in techbusiness and Ai startup")