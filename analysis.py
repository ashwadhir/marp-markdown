import marimo

__generated_with = "0.1.0"
app = marimo.App()

@app.cell
def __():
    import marimo as mo
    
    # Technical Consultant Identity
    # Email: 22f2000771@ds.study.iitm.ac.in
    return mo,

@app.cell
def __(mo):
    # CELL 1: Interactive Input
    # We create a slider widget to control a variable 'multiplier'.
    # This is the independent variable in our analysis.
    slider = mo.ui.slider(start=1, end=100, step=1, value=10, label="Select Multiplier")
    
    # Output the slider to the UI
    slider
    return slider,

@app.cell
def __(slider):
    # CELL 2: Dependent Calculation
    # This cell depends on the 'slider' object from the previous cell.
    # Data Flow: Slider Input -> Calculation -> 'result' variable
    
    input_value = slider.value
    
    # We calculate a simple relationship: y = x * 1.5
    result = input_value * 1.5
    return input_value, result

@app.cell
def __(input_value, mo, result):
    # CELL 3: Dynamic Markdown Output
    # This cell depends on the calculated 'result'.
    # It updates the text automatically when the slider changes.
    
    mo.md(
        f"""
        ## Interactive Analysis Dashboard
        
        Based on your selection of **{input_value}**, the projected value is:
        
        # {result}
        
        ---
        **Analyst:** 22f2000771@ds.study.iitm.ac.in
        """
    )
    return

if __name__ == "__main__":
    app.run()
