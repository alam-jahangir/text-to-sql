# text-to-sql
A simple generative AI Text-to-SQL system demo in Python using Google Gemini and SQLite database. This demo takes a plain English question or Natural language, generates the correct SQL query, executes it, and displays the data.

# Example Command
```uv run main.py Find Red color apple```
> Output
```User Question: 'Find Red color apple'

Generated SQL Query:
SELECT id, name, color
FROM apples
WHERE color = 'Red'

Generated SQL Query Data: 

(2, 'Fuji', 'Red')
```

```uv run main.py Find sweet oranges ```
> Output:
```User Question: 'Find sweet oranges'

Generated SQL Query:
SELECT id, name, description
FROM oranges
WHERE description LIKE '%sweet%'

Generated SQL Query Data: 

(2, 'Tangelo', 'sweet and tart')
(3, 'Tangerine', 'great for sweeter juice')
(6, 'Navel Orange', 'sweet with slight bitterness')
```

