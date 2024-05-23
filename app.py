import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
topic = input("Enter a subject topic: ")

os.environ["OPENAI_API_BASE"] = "http://localhost:1234/v1"
os.environ["OPENAI_API_KEY"] = "lm-studio"
os.environ["OPENAI_MODEL_NAME"] = "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF"

# Define your agents with roles and goals
researcher = Agent(
    role='Research Analyst',
    goal= 'Develop ideas for teaching a student new to the subject: {Topic}',
    backstory=
    """You are an expert at an Educational Organization, skilled in researching subject topics and how to teach them.""",
    verbose=True,  # gives us more info as the agent is running
    allow_delegation=False,
    tools=[search_tool]
)

writer = Agent(
    role='Technical Writer',
    goal="Use the researcher's ideas to write a piece of text to explain the subject",
    backstory=
    """You are a Technical writer known for making complex topics interesting and easy to understand.""",
    verbose=True,
    allow_delegation=True,
)

examiner = Agent(
    role='Examiner',
    goal="Craft 2 to 3 test questions to evaluate understanding of the created text, along with the correct answers.",
    backstory=
    """You are an examiner known for crafting questions that effectively test a student's knowledge of a subject.""",
    verbose=True,
    allow_delegation=False,
)

# create tasks for agents
researcher_task = Task(
    description = "Develop ideas for teaching a student new to the subject: {Topic}. The ideas should be easy to implement and carry out by a writer",
    expected_output='A list of ideas.',
    agent=researcher,
    output_file= f'{topic}-ideas.txt'
    )

writer_task = Task(
    description = "Write a piece of text to explain the subject using the researcher's ideas. This article should be easy to understand, engaging, and positive. It should be at 1 paragraphs long.",
    expected_output='A comprehensive 1 paragraph long text explaining the subject.',
    agent=writer,
    output_file= f'{topic}-materials.txt'
    )

examiner_task = Task(
    description = "Craft 2 to 3 test questions to evaluate understanding of the created text, along with the correct answers. In other words: test whether a student has fully understood the text.",
    expected_output='A list of questions and their correct answers.',
    agent=examiner,
    output_file= f'{topic}-test.txt'
    )

# Instantiate your crew with a sequential process
crew = Crew(agents=[researcher, writer, examiner], tasks=[researcher_task, writer_task, examiner_task], verbose=2, process=Process.sequential)

print(f'Subject Topic: {topic}')
# Get your crew to work!
result = crew.kickoff(inputs={'Topic': topic})

print("###################")
print(result)

