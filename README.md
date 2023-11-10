# SRA Coursework

## How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the program

```
Optimal Schedule Discovery

positional arguments:
  {tabu_search,vn_search}
                        Select a scheduler
  {sum_tardiness,sum_weighted_tardiness}
                        Cost function to evaluate candidate schedules

optional arguments:
  -h, --help            show this help message and exit
  --tabu_list_size TABU_LIST_SIZE
                        Tabu list size for Tabu Search
  --gamma GAMMA         Gamma value
  --iterations ITERATIONS
                        Number of iterations for Tabu Search
  --verbose             Verbose mode
  --output_file OUTPUT_FILE
                        Save schedule to output file
  --graph_schedule      Graph optimal schedule
  --problem {ClassProblem1,ClassProblem2,CourseworkProblem}
                        Problem to solve
  --input_problem_file INPUT_PROBLEM_FILE
  ```

Please note that the `--problem` and the `--input_problem_file` arguments are mutually exclusive. This means that you can either specify a pre-defined problem to solve or provide an input file to parse and solve.

### 3. Example

```bash
python run_scheduler.py tabu_search sum_tardiness --iterations 1000000 --input_problem_file input.json --graph_schedule --output_file run1
```