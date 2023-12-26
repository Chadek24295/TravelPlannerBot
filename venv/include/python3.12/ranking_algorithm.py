def rank_travel_options(df, criteria='price'):
    # Sorting based on criteria (e.g., price, time)
    if criteria == 'price':
        sorted_df = df.sort_values(by='price', ascending=True)
    elif criteria == 'time':
        sorted_df = df.sort_values(by='travel_time', ascending=True)
    else:
        sorted_df = df

    return sorted_df

# Example usage
criteria = 'price'  # or 'time'
ranked_travel_options = rank_travel_options(df_travel, criteria)
