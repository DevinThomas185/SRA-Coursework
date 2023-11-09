import matplotlib.pyplot as plt
from Job import Job


def format_number(number: int):
    return f"{number:,}"

def print_schedule(title: str, schedule: list[Job]):
    # Set up the plot
    fig, ax = plt.subplots()

    # Plot each job as a horizontal bar
    t = 0
    for job in schedule:
        ax.barh(
            0,
            job.get_processing_time(),
            left=t,
            # height=0.5,
            label=f"Job {job.get_id()}",
            color=job.get_colour(),
        )
        t += job.get_processing_time()

    # Customize the plot
    ax.set_yticks([])  # Remove y-axis ticks
    ax.set_xlabel("Time /s")
    ax.set_title(title)

    # Add legend
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    # Show the plot
    plt.show()
