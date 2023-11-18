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


def print_schedule_to_csv(schedule: list[Job], csv_name: str) -> None:
    with open(csv_name + ".csv", "w") as f:
        for job in schedule[:-1]:
            f.write(f"{job.get_id()}, ")
        f.write(f"{schedule[-1].get_id()}")


def print_execution_to_file(file_name: str, execution: str, params) -> None:
    with open(f"{file_name}.txt", "w") as f:
        f.write("Parameters:\n")
        for param, value in params.items():
            f.write(f"{param}: {value}\n")
        f.write(execution)
