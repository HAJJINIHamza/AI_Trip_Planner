# Trip Planner Agent 

### Description :
An Agent AI for planning a trip to any city in the world using real time data 

### Objectives :
1. Real time weather info
2. Attraction & Activity for a specific city 
3. Hotel cost for different days
4. Currency conversions
5. Itinery planning, what cities to visit and when
6. Total expenses estimation 
7. General summary of the trip

### System test screenshot 
![System test screenshot](ai_trip_planner_test_screenshot.png)

### Tools 
- Python 3.11.14

### APP RUNNING
To run app, follow these steps:

1. Install python and create a virtual environement:

    ```uv python install cpython-3.11.14-windows-x86_64-none```

    ```uv venv env --python cpython-3.11.14-windows-x86_64-none```

2. Pull code to your local machine:

    `git pull https://github.com/HAJJINIHamza/AI_Trip_Planner.git`

3. Install dependecies, better use uv then pip:

    `uv pip install -r requirements.txt`

4. Open two different terminals (command prompt)

5. Activate your virtual environement on both terminals`

    `env\Scripts\activate.bat`

    or

    `.venv\Scripts\activate`

6. On the first terminal run app API endpoint:

    ```uvicorn main:app --reload --port 8000```

7. On the second terminal run streamlit application:

    ```streamlit run streamlit_app.py```

8. Use the Agentic AI to plan your trip

### First Commands History (To buil system from scratch):

```uv python list```

```uv python install cpython-3.11.14-windows-x86_64-none```

```python list```

```uv python list```

```uv venv env --python cpython-3.11.14-windows-x86_64-none```

```env/Scripts/activate```

```python venv/Scripts/activate```

```python env/Scripts/activate```

```C:\Users\hh\projects\AI_Trip_Planner\env\Scripts\activate.bat```

```uv pip list ``` 
