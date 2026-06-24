from langchain.tools  import tool
import datetime as dt

@tool
def current_date():
    """This tool displays the current date."""

    try:
        today = dt.datetime.now()
        return today
    except Exception as e:
        return f"unexpected error{e}"


all_tools = [
    current_date,
]