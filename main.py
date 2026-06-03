
from sys import argv
from google_genai import GoogleGenai
from sqlite_con import SqliteCon

if __name__ == '__main__':

    user_query = " " . join(argv[1:])

    print(f"User Question: '{user_query}'\n")

    try:

        # Generate the query string using the LLM
        generated_sql = GoogleGenai().generate_sql(user_query)

        print(f"Generated SQL Query:\n{generated_sql}\n")

        print("Generated SQL Query Data: \n")
        for row in SqliteCon().execute(generated_sql):
            print(row)

    except Exception as e:

        print(f"Error occurred: {e}")

    finally:
        SqliteCon().close()
