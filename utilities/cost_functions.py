# Tardiness
def sum_tardiness(candidate) -> float:
    total_tardiness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_tardiness += max(0, t - job.get_due_date())

    return total_tardiness


def sum_weighted_tardiness(candidate) -> float:
    total_tardiness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_tardiness += max(0, t - job.get_due_date()) * job.get_weight()

    return total_tardiness


def total_tardy_jobs(candidate) -> int:
    t = 0
    tardy_jobs = 0

    for job in candidate:
        t += job.get_processing_time()
        if t > job.get_due_date():
            tardy_jobs += 1

    return tardy_jobs

def weighted_total_tardy_jobs(candidate) -> int:
    t = 0
    tardy_jobs = 0

    for job in candidate:
        t += job.get_processing_time()
        if t > job.get_due_date():
            tardy_jobs += job.get_weight()

    return tardy_jobs


def maximum_tardiness(candidate) -> float:
    t = 0
    max_tardiness = 0

    for job in candidate:
        t += job.get_processing_time()
        tardiness = max(0, t - job.get_due_date())
        max_tardiness = max(max_tardiness, tardiness)

    return max_tardiness


# Completion Time
def maximum_completion_time(candidate) -> float:
    t = 0

    for job in candidate:
        t += job.get_processing_time()

    return t


def sum_completion_time(candidate) -> float:
    t = 0
    total_completion_time = 0

    for job in candidate:
        t += job.get_processing_time()
        total_completion_time += t

    return total_completion_time


# Lateness
def sum_lateness(candidate) -> float:
    total_lateness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_lateness += t - job.get_due_date()

    return total_lateness


def sum_weighted_lateness(candidate) -> float:
    total_lateness = 0
    t = 0

    for job in candidate:
        t += job.get_processing_time()
        total_lateness += (t - job.get_due_date()) * job.get_weight()

    return total_lateness

def maximum_lateness(candidate) -> float:
    t = 0
    max_lateness = 0

    for job in candidate:
        t += job.get_processing_time()
        lateness = t - job.get_due_date()
        max_lateness = max(max_lateness, lateness)

    return max_lateness
