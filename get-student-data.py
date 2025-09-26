import snowflake.connector
import pandas as pd

def get_student_data(student_id):
    conn = snowflake.connector.connect(
        user="USER",
        password="PASS",
        account="ACCOUNT",
        warehouse="WH",
        database="EDUPULSE",
        schema="PUBLIC"
    )
    cur = conn.cursor()
    cur.execute(f"""
        SELECT SUBJECT, SCORE, MAX_SCORE, DATE
        FROM ASSESSMENTS
        WHERE STUDENT_ID = {student_id}
        ORDER BY DATE DESC
        LIMIT 10
    """)
    df = pd.DataFrame(cur.fetchall(), columns=[c[0] for c in cur.description])
    conn.close()
    return df
