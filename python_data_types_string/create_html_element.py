"""
Task
----
Write a python function to create an HTML string with tags around the words.
"""


def create_html_element(element_type: str, content: str) -> str:
    """
    Function to create HTML element.

    Arguments
    ---------
        element_type (str): HTML element type like div, i, b, span, etc.
        content (str): string to be enclosed using HTML tags.

    Returns
    -------
        html_element (str): HTML element constructed from `element_type` and `content`.
    """

    html_element = "<" + element_type + ">" + content + "</" + element_type + ">"

    return html_element


if __name__ == "__main__":
    element_type = input("Enter HTML Element type:")
    content = input("Enter text content:")

    print(f"HTML Element = {create_html_element(element_type, content)}")
