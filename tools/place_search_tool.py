import os 
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool(api_key = os.environ["TAVILY_API_KEY"])
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup all tools for the place search tool
        """
        @tool 
        def search_attractions(place:str) -> str:
            """
            Search attractions of a place
            """
            print ("@TOOL : search_attractions is being used")
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    print (f"Following are the attractions of {place} as suggested by google: {attraction_result}")
                    return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                print (f"Following are the attractions of {place} as suggested by tavily: {tavily_result}")
                return f"Google cannot find the details. \nFollowing are the attractions of {place}: {tavily_result}"
            
        @tool 
        def search_restaurants(place:str) -> str:
            """
            Search restaurants of a place 
            """
            print ("@TOOL : search_restaurants is being used")
            try:
                result = self.google_places_search.google_search_restaurants(place)
                if result:
                   
                    print(f"Following are the restaurants of {place} as suggested by google: {result}")
                    return f"Following are the restaurants of {place} as suggested by google: {result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants (place)
                print(f"Google cannot find the details. \nFollowing are the restaurants of {place}: {tavily_result}")
                return f"Google cannot find the details. \nFollowing are the restaurants of {place}: {tavily_result}"
            
        @tool
        def search_activities(place:str) -> str:
            """
            Search activities of a place
            """
            print ("@TOOL : search_activities is being used")
            try:
                result = self.google_places_search.google_search_activity (place)
                if result:
                    print ("@TOOL : search_activities is being used")
                    print(f"Following are the activities of {place} as suggested by google: {result}")
                    return f"Following are the activities of {place} as suggested by google: {result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity (place)
                print (f"Google cannot find the details. \nFollowing are the activities of {place}: {tavily_result}")
                return f"Google cannot find the details. \nFollowing are the activities of {place}: {tavily_result}"
            
        @tool
        def search_transportation(place:str) -> str:
            """
            Search transportation of a place
            """
            print ("@TOOL : search_transportation is being used")
            try:
                result = self.google_places_search.google_search_transportation (place)
                if result:
                    print ("@TOOL : search_transportation is being used")
                    print(f"Following are modes of transportation available in {place} as suggested by google: {result}")
                    return f"Following are modes of transportation available in {place} as suggested by google: {result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation (place)
                print (f"Google cannot find the details. \nFollowing are the transportation of {place}: {tavily_result}")
                return f"Google cannot find the details. \nFollowing are the transportation of {place}: {tavily_result}"
            
        return [search_attractions, search_restaurants, search_activities, search_transportation] 


