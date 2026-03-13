PYTHON=.venv/bin/python


run-agent:
	$(PYTHON) -m gen_agent.agents.tavily_search_in_tool_agent

install:
	pip install -r requirements.txt

lint:
	flake8 .

format:
	black .

sort:
	isort .	
