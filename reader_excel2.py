from mcp.server.fastmcp import FastMCP 
from mcp.types import Prompt
from mcp.server import Server
import pandas as pd

app = FastMCP("Excel_Reader2")
server = Server(app)
path = "C:\\Programming\\MCP_PROJECTS\\ON_MY_OWN_MCP\\Beta_Programs\\Book1.xlsx"

# Define prompts
@app.tool()
def list_prompts(key: str | None = None):
    PROMPTS = {
        "excel_summary": {
            "name": "excel_summary",
            "description": "Generate a summary of the Excel file contents using the read_excel tool.",
            "arguments": []
        },
        "Content_Summary": {
            "name": "Content_Summary",
            "description": "Provide a detailed summary of the data contained in the given URI using the read document resource.",
            "arguments": []
        }
    }
    if key is None:
        return list(PROMPTS.values())
    else:
        return PROMPTS.get(key)

# Gets the prompt details based on the key
@app.tool()
def get_prompt(Key: str) :
    prompt = list_prompts(Key)
    return prompt


# Define tool to read Excel file
@app.tool()
def read_excel(path: str = path) -> str:
    # Read the Excel file
    df = pd.read_excel(path)

    # Convert DataFrame to string for output
    return df.to_string()

def main():
    # Initialize and run the server
    app.run(transport="stdio")


if __name__ == "__main__":
    main()