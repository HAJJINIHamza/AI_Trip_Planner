import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #Set specific origins in prod
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query : QueryRequest):
    try : 
        print ("query :", query)
        graph = GraphBuilder(model_provider="groq")
        react_app=graph()
        #react_app = graph.build_graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)
        
        print (f"Graph saved in 'my_graph.png' at {os.getcwd()}")
        #Assuming request is a pydantic object like : {"question": "text"}
        messages = {"messages": [query.question]}
        print ("Invoking graph ... ")
        output = react_app.invoke(messages)
        print ("Agent output :", output)

        #If result is dict with messages
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content #last ai answer
        else : 
            final_output = str(output)
        return {"answer": final_output}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})