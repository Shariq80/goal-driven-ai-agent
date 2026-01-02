from src.planner import Planner
from src.executor import Executor
from src.memory import Memory

class AIAgent:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.executor = Executor(self.memory)
    
    def run(self, goal: str):
        print(f"[Agent] Goal: {goal}")

        while True:
            step = self.planner.next_step(goal, self.memory.dump())

            if not step:
                break

            action = step[0]
            print(f"[Agent] Next Step: {action['step']}")

            result = self.executor.execute(action)
            print(f"[Agent] Result: {result}")

            self.memory.update(action, result)

            if action["tool"] == "memory.complete":
                print("[Agent] Goal Completed.")
                break

        # while not self.memory.dump()["completed"]:
        #     plan = self.planner.next_step(goal, self.memory.dump())

        #     if not plan:
        #         print("[Agent] No further actions. Goal completed.")
        #         self.memory.mark_completed()
        #         break

        #     step = plan[0]
        #     print("[Agent] Next step:", step["step"])

        #     result = self.executor.execute(step)
        #     print("[Agent] Result:", result)

        #     if step["tool"] == "filesystem.list_files":
        #         self.memory.add_files(result)
        #     elif step["tool"] == "filesystem.read_file":
        #         self.last_read_text = result
        #     elif step["tool"] == "text.summarize":
        #         filePath = step["args"].get("filePath", "unknown")
        #         self.memory.add_summary(filePath, result)
        #     elif 
        
        # print("[Agent] Final memory:")
        # print(self.memory.dump())