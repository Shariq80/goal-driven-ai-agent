import os
import ollama

ALLOWED_BASE_DIR = "data"

def _is_safe_path(path: str) -> bool:
    fullPath = os.path.abspath(path)
    basePath = os.path.abspath(ALLOWED_BASE_DIR)
    return fullPath.startswith(basePath)

def list_files(path: str):
    """
    List files in a directory. Safety: restricted to ALLOWED_BASE_DIR.
    """
    if not _is_safe_path(path):
        raise PermissionError("Access outside allowed directory")
    
    if not os.path.exists(path):
        return []
    
    return [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

def read_file(path: str):
    if not _is_safe_path(path):
        raise PermissionError("Access outside allowed directory")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def summarize_text(text: str, model="mistral"):
    prompt = (
        "Summarize the following text clearly and concisely:\n\n"
        f"{text}"
    )

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    message = response.get("message")
    return message.content if hasattr(message, "content") else str(message)

def write_file(path: str, content: str):
    if not _is_safe_path(path):
        raise PermissionError("Access outside allowed directory")
    
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        return "Completed"