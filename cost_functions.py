def sum_tardiness(candidate) -> int:
    total_tardiness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_tardiness += max(0, t - job.get_due_date())

    return total_tardiness


def sum_weighted_tardiness(candidate) -> int:
    total_tardiness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_tardiness += max(0, t - job.get_due_date()) * job.get_weight()

    return total_tardiness
