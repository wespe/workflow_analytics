def average(workplan):
    penalties = 0
    result = workplan.result()
    for key, value in result.items():
        if key in ['expired', 'over_time', 'small_time']:
            if key == 'small_time':
                penalties += value * 2
            else:
                penalties += value
    total = result.get('expired', 0) + result.get('not_expired', 0)
    return penalties / total
