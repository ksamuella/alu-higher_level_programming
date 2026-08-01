-- Lists all records with a non-null name, ordered by score (top first)
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
