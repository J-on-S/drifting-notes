from mongo_client import insert_note, get_random_note

anon_id = "USER_A"

note_id = insert_note("A kind note for a stranger 🌿", anon_id)
print("Inserted:", note_id)

note = get_random_note(exclude_anon_id=anon_id)
print("Random note (excluding myself):", note)
