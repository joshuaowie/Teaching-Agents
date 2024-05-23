# Teaching-Agents
# Agent Workflow for Generating Educational Content
## Overview
This project demonstrates a workflow capable of generating questions and answers on a specific subject or topic using the  CrewAI agent frameworks in Python. The workflow involves three main agents: the Researcher, the Writer, and the Examiner, each with distinct roles to ensure comprehensive educational content creation.

The project leverages models from LM Studio, specifically the OpenHermes model, capped at 7 billion parameters, to generate and process the content.

## Agents
Researcher: This agent searches and develops ideas for teaching someone new to the subject.
Writer: This agent uses the Researcher’s ideas to write a piece of text explaining the topic. It also is sometimes asked to rewrite clarified texts by the examiner agent to aid the examiner in better doing its tasks.
Examiner: This agent crafts 2-3 test questions to evaluate the understanding of the created text, along with the correct answers.

## Testing and Results
The Subject/Topic "Dangers of Artificial Intelligence-materials" was used as an example to test the agent workflow

The results for each agent task are saved in text files in the format of: 
Researcher Agents Task Result: "subject-ideas.txt"
Writer Agents Task Result: "subject-materials.txt"
Examiner Agents Task Result: "subject-test.txt"

## Project Structure
README.md
app.py
requirements.txt
Dangers of Artificial Intelligence-ideas.txt
Dangers of Artificial Intelligence-materials.txt
Dangers of Artificial Intelligence-test.txt
