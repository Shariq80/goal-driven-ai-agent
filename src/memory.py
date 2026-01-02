class Memory:
    def __init__(self):
        self.data = {
            "files": [],
            "summaries": {},
            "last_file": None,
            "last_content": None,
            "saved_files": [],
            "completed": False,
        }

    def update(self, action, result):
        tool = action["tool"]

        if tool == "filesystem.list_files":
            self.data["files"] = result

        elif tool == "filesystem.read_file":
            self.data["last_file"] = action["args"]["path"]
            self.data["last_content"] = result
        
        elif tool == "text.summarize":
            file_path = self.data["last_file"]
            self.data["summaries"][file_path] = result
        
        elif tool == "filesystem.write_file":
            note_path = action["args"]["path"] \
                .replace("data/summaries", "data/notes") \
                .replace(".md", ".txt")
            self.data["saved_files"].append(note_path)

        elif tool == "memory.complete":
            self.data["completed"] = True

    def dump(self):
        return self.data
