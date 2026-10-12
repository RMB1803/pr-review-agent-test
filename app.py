def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query


def delete_user(user_id):
    query = f"DELETE FROM users WHERE id = {user_id}"
    return query




#NEW CHANGES MADE BY ME LESTS GO