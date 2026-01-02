from src import tools

class Executor:
    def __init__(self, memory):
        self.memory = memory
        self.tool_map = {
            "filesystem.list_files": tools.list_files,
            "filesystem.read_file": tools.read_file,
            "filesystem.write_file": tools.write_file,
            "text.summarize": tools.summarize_text,
            "memory.complete": self.complete,
        }
    
    def complete(self):
        self.memory.data["completed"] = True
        return "Completed"

    def execute(self, step):
        toolName = step.get("tool")
        args = step.get("args", {})

        if toolName not in self.tool_map:
            return f"Tool not allowed: {toolName}"

        return self.tool_map[toolName](**args)

    # def execute(self, step):
    #     toolName = step.get("tool")
    #     args = step.get("args", {})

    #     if toolName not in self.tool_map:
    #         return f"Tool not allowed: {toolName}"
    #     elif toolName == "memory.complete":
    #         return "COMPLETED"

    #     try:
    #         return self.tool_map[toolName](**args)
    #     except Exception as e:
    #         return f"Execution error: {e}"