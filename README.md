# Expense Tracker (Blind Mode)

A simple, fun, and secure console-based Python application to track group expenses and find out who spent the most — without anyone seeing others' inputs!

Perfect for:
- Splitting bills with friends
- Office lunch tracking
- Family expense competitions
- Learning Python fundamentals

## Features 

- **Blind Mode**: Each person's input is hidden from others (screen cleared after each entry)
- **Custom ASCII Art Logo**: Professional-looking console interface
- **Clean Code Structure**: Functions separated, readable comments
- **Tie Handling**: Preserves first winner in case of equal spending
- **User-Friendly Prompts**: Clear instructions and input validation

## Concepts Learned

- Python dictionaries (key-value data storage)
- While loops and condition-based flow control
- Functions and return values
- Input normalization using `.lower()`
- Basic algorithm for finding a maximum value in a dataset
- Modular code design (separating logic from UI)


## How It Works

1. The program prompts users to enter:
   - The name of the person who spent money
   - The amount spent
2. Each entry is saved into a dictionary
3. Users can continue adding expenses until they type `no`
4. Once finished, the program identifies and displays:
   - The person who spent the most
   - The total amount they spent
