def convert_to_dict(columns, rows):
    return [dict(zip(columns, row)) for row in rows]