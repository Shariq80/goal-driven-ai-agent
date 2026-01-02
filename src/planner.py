import json
import re
import ollama


class Planner:
    """
    Deterministic planner.
    Decides EXACTLY ONE next atomic step based on memory.
    """

    def next_step(self, goal: str, memory: dict):

        # 1. No files yet → list files
        if not memory["files"]:
            return [{
                "step": "List note files",
                "tool": "filesystem.list_files",
                "args": {"path": "data/notes"}
            }]

        # 2. Process each file
        for file_path in memory["files"]:

            # Skip files already fully processed
            if file_path in memory["saved_files"]:
                continue

            # Read file if not read yet
            if memory.get("last_file") != file_path:
                return [{
                    "step": f"Read file {file_path}",
                    "tool": "filesystem.read_file",
                    "args": {"path": file_path}
                }]

            # Summarize if not summarized yet
            if file_path not in memory["summaries"]:
                return [{
                    "step": f"Summarize {file_path}",
                    "tool": "text.summarize",
                    "args": {"text": memory["last_content"]}
                }]

            # Save summary if not saved yet
            summary = memory["summaries"][file_path]
            output_path = file_path \
                .replace("data/notes", "data/summaries") \
                .replace(".txt", ".md")

            return [{
                "step": f"Save summary for {file_path}",
                "tool": "filesystem.write_file",
                "args": {
                    "path": output_path,
                    "content": summary
                }
            }]

        # 3. All files processed → complete
        return [{
            "step": "Mark task as completed",
            "tool": "memory.complete",
            "args": {}
        }]
