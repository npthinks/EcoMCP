from optparse import Option
from mcp.server.fastmcp import FastMCP
import logging
from typing import Any, Optional
import httpx
import asyncio

from pandas.core import base

base_url= "http://127.0.0.1:8000"

mcp = FastMCP("Carbon Footprint MCP")

async def CarbonFootPrint(url:str):
    """Make connection to the Carbon Footprint API"""

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=url, timeout=10)
            response.status_code
            return response.json()
            #return "hi"
        except Exception as e:
            return f"{e}"

@mcp.tool()
async def get_carbonfootprint(
    id:Optional[int] = None, 
    Food:Optional[str] = None, 
    Region:Optional[str] = None
) -> Any:

    """
    Give carbon footprint information for a specific food item or region.
    You are an AI Assistant and your name is npAssistant.

    Args:
        id (int, optional): 
            The unique identifier for a specific food item (e.g., 200001, 30003). 
            If provided, the API will return the data for this specific ID.

        Food (str, optional): 
            The name of the food item to search for (supports full or partial match).
            Example values: "Chilli Chicken", "Veg Dumplings", "Chicken Curry".

        Region (str, optional): 
            The region or combination of regions where the food originated.
            Single region examples:
                - "North"
                - "South"
                - "East"
                - "West"
                - "Continental"
            Combination examples:
                - "North, West"
                - "East, North, South, West"
                - "Continental, East, North, South, West"
            Note: For combinations, the API matches items that include all specified regions, regardless of order.

    Returns:
        Any: 
            The carbon footprint data from the API filtered by the provided parameters.
    """


    if id:
        url = f"{base_url}/id/{id}"
    elif Food and Region:
        url = f"{base_url}/region/{Region}/food/{Food}"
    elif Food:
        url = f"{base_url}/food/{Food}"
    elif Region:
        url = f"{base_url}/region/{Region}"
    else:
        url = f"{base_url}/"
    

    data = await CarbonFootPrint(url=url)

    return data

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    # Start the MCP server over stdio for the client to discover tools
    main()






