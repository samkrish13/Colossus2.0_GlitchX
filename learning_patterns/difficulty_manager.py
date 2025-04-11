# learning_patterns/difficulty_manager.py
def get_user_level(user_id, performance_data):
    average_score = sum(performance_data) / len(performance_data)
    if average_score > 80:
        return 'advanced'
    elif average_score > 50:
        return 'intermediate'
    else:
        return 'beginner'
