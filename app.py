import gradio as gr

def binary_search_visual(list_str, target_str):
    # Input validation
    try:
        nums = [int(x.strip()) for x in list_str.split(",")]
        target = int(target_str)
    except:
        return "Error: Please enter only numbers.", ""

    steps = []
    nums.sort()  # Binary search requires a sorted list

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        steps.append(
            f"Searching between indexes {low} and {high}. "
            f"Middle index: {mid}, value: {nums[mid]}"
        )

        if nums[mid] == target:
            steps.append(f"Found {target} at index {mid}!")
            return f"Found {target} at index {mid}", "\n".join(steps)

        elif nums[mid] < target:
            steps.append(f"{target} > {nums[mid]} → Searching right half")
            low = mid + 1
        else:
            steps.append(f"{target} < {nums[mid]} → Searching left half")
            high = mid - 1

    steps.append("Target not found.")
    return "Not found", "\n".join(steps)

# Gradio UI
with gr.Blocks(title="Binary Search Visualizer") as demo:
    gr.Markdown("# Binary Search Interactive Visualizer")

    list_input = gr.Textbox(label="Enter a list of numbers (comma-separated)")
    target_input = gr.Textbox(label="Enter the number to search")
    run_button = gr.Button("Run Binary Search")

    result_output = gr.Textbox(label="Result")
    steps_output = gr.Textbox(label="Step-by-step process", lines=12)

    run_button.click(
        binary_search_visual,
        inputs=[list_input, target_input],
        outputs=[result_output, steps_output]
    )

demo.launch()