def get_naming_prompt():
    return """
1. Use lowercase and underscores for spaces.
2. Avoid special characters (no !, @, #, $, %, etc).
3. Max 5-7 words if possible, skip filler like 'the', 'a'.
4. Use meaningful keywords: names, topics, categories.
5. If nothing useful in OCR, use 'untitled'.
6. Do NOT include file extension in output.
7. Assume files could be images, PDFs, docs, or notes.
"""
