def count_lines(text):
    # Counting lines
    return len(text.strip().split('\n'))

def count_words(text):
    # Counting words
    return len(text.strip().split())

def count_lines_with_word(text, keyword):
    # Count lines that contain the with
    return sum(1 for line in text.strip().split('\n') if keyword.lower() in line.lower())

def print_summary(text, keyword):
    # Print summary of line count, word count, and keyword line count
    total_lines = count_lines(text)
    total_words = count_words(text)
    keyword_lines = count_lines_with_word(text, keyword)

    # Display the results
    print(f"Total number of lines       : {total_lines}")
    print(f"Total number of words       : {total_words}")
    print(f"Lines containing '{keyword}': {keyword_lines}")


# Sample multi-line input string
sample_text = """
Hello Friends This is my task_3 program on 
Strings and I am completing my Tasks
"""

# Run the summary function with keyword "test"
print_summary(sample_text, "tasks")