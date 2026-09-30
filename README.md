# Comparative Analysis of Shell Scripting and Programming Languages for Log Data Processing

## 📌 Project Overview

This project presents a comparative performance analysis of different scripting and programming approaches for processing and analyzing system/log monitoring data.

The project uses a structured logging and monitoring dataset and implements the same or similar data-processing tasks using:

* 🐚 Bash
* 🔎 AWK
* 🟣 Perl
* 🐍 Python

The experiments evaluate execution performance, processing latency, timing behavior, and other measurable characteristics across different tasks.

---

## 🎯 Objectives

The main objectives of this project are:

1. To analyze a structured log-monitoring dataset.
2. To implement data-processing tasks using Bash, AWK, Perl, and Python.
3. To compare the execution performance of different approaches.
4. To measure execution time and latency.
5. To analyze real-time log-processing behavior.
6. To generate experimental results and visualizations.
7. To identify performance differences between scripting and programming approaches.

---

## 📂 Repository Structure

```text
github_upload/
│
├── 📁 dataset/
│   └── logging_monitoring_anomalies.csv
│
├── 📁 scripts/
│   ├── bench_one.py
│   │
│   ├── t1_bash.sh
│   ├── t1_awk.sh
│   ├── t1_perl.pl
│   ├── t1_python.py
│   │
│   ├── t2_bash.sh
│   ├── t2_grepsed.sh
│   ├── t2_perl.pl
│   ├── t2_python.py
│   │
│   ├── t3_bash.sh
│   ├── t3_awk.sh
│   ├── t3_perl.pl
│   ├── t3_python.py
│   │
│   ├── t4_bash.sh
│   ├── t4_awk.sh
│   ├── t4_perl.pl
│   ├── t4_python.py
│   │
│   ├── t5_sort.sh
│   ├── t5_awk.sh
│   ├── t5_perl.pl
│   ├── t5_python.py
│   │
│   └── 📁 realtime/
│       ├── run_exp3.sh
│       ├── producer.py
│       ├── python_monitor.py
│       ├── stamper.py
│       └── analyze_latency.py
│
├── 📁 results/
│   ├── bench_results.json
│   ├── loc_results.json
│   └── rt_latency_results.json
│
└── 📁 diagram/
    ├── latency_dist.png
    ├── tradeoff.png
    ├── loc_grouped.png
    ├── timing_grouped.png
    ├── latency_bar.png
    └── speedup.png
```

---

## 📊 Dataset

### Dataset Name

**Logging and Monitoring Anomalies Dataset**

### File

```text
dataset/logging_monitoring_anomalies.csv
```

The dataset contains structured log-monitoring and anomaly-related information.

### Main Attributes

| Attribute            | Description                       |
| -------------------- | --------------------------------- |
| Timestamp            | Date and time of the event        |
| Anomaly_ID           | Unique anomaly identifier         |
| Anomaly_Type         | Type of detected anomaly          |
| Severity             | Severity level                    |
| Status               | Current status of the anomaly     |
| Source               | Source of the event               |
| Alert_Method         | Method used to generate the alert |
| Response_Time_ms     | Response time in milliseconds     |
| Resolution_Time_min  | Resolution time in minutes        |
| Affected_Services    | Number of affected services       |
| User_Role            | Role of the user                  |
| CPU_Usage_Percent    | CPU utilization                   |
| Memory_Usage_MB      | Memory utilization                |
| Disk_Usage_Percent   | Disk utilization                  |
| Network_In_KB        | Incoming network traffic          |
| Network_Out_KB       | Outgoing network traffic          |
| Login_Attempts       | Number of login attempts          |
| Failed_Transactions  | Number of failed transactions     |
| Anomaly_Duration_sec | Duration of anomaly               |
| Service_Type         | Type of service                   |
| Alert_Count          | Number of alerts                  |
| Retry_Count          | Number of retries                 |
| Escalation_Level     | Escalation level                  |

---

## 🧪 Experimental Tasks

The project contains multiple experimental tasks implemented using different technologies.

### Task 1

Analysis of anomaly severity/count information using:

* Bash
* AWK
* Perl
* Python

### Task 2

Text/log processing using:

* Bash
* grep/sed
* Perl
* Python

### Task 3

Additional log/data-processing operations using:

* Bash
* AWK
* Perl
* Python

### Task 4

Comparative processing using:

* Bash
* AWK
* Perl
* Python

### Task 5

Sorting and processing operations using:

* Shell
* AWK
* Perl
* Python

---

## ⚡ Performance Benchmarking

The file:

```text
scripts/bench_one.py
```

is used for benchmarking individual experimental tasks.

The benchmarking process measures:

* Mean execution time
* Minimum execution time
* Maximum execution time
* Standard deviation
* Number of experimental runs
* Timeout conditions

The results are stored in:

```text
results/bench_results.json
```

---

## 🔴 Real-Time Processing Experiment

The `scripts/realtime/` directory contains scripts for real-time log-processing experiments.

### Components

**producer.py**

Generates/streams log records for the experiment.

**stamper.py**

Adds timing information to processed records.

**python_monitor.py**

Provides Python-based monitoring functionality.

**analyze_latency.py**

Analyzes latency-related experimental results.

**run_exp3.sh**

Runs the real-time processing experiment using the selected technology/filter.

---

## 📈 Results

Experimental results are stored in JSON format under:

```text
results/
```

### Result Files

```text
bench_results.json
loc_results.json
rt_latency_results.json
```

These files contain the measurements generated during the experiments.

---

## 📊 Visualizations

The `diagram/` directory contains the generated figures.

### Available Figures

* `latency_dist.png` — Latency distribution
* `tradeoff.png` — Performance trade-off analysis
* `loc_grouped.png` — Lines-of-code comparison
* `timing_grouped.png` — Execution timing comparison
* `latency_bar.png` — Latency comparison
* `speedup.png` — Speedup comparison

---

## 🛠️ Technologies Used

| Technology                | Purpose                                     |
| ------------------------- | ------------------------------------------- |
| Bash                      | Shell scripting and command-line processing |
| AWK                       | Text and structured-data processing         |
| Perl                      | Scripting and data processing               |
| Python                    | Data processing and benchmarking            |
| Linux/Unix Shell          | Command-line experimentation                |
| JSON                      | Experimental result storage                 |
| CSV                       | Dataset storage                             |
| Matplotlib/Plotting Tools | Visualization                               |

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>
```

### 2. Check the Dataset

```bash
cd dataset
ls
```

The dataset file is:

```text
logging_monitoring_anomalies.csv
```

### 3. Run a Python Experiment

From the appropriate directory:

```bash
python3 scripts/t1_python.py
```

### 4. Run a Shell Experiment

```bash
bash scripts/t1_bash.sh
```

### 5. Run an AWK Experiment

```bash
bash scripts/t1_awk.sh
```

### 6. Run a Perl Experiment

```bash
perl scripts/t1_perl.pl
```

> **Note:** Update the dataset path inside the scripts if the script is executed from a different working directory.

---

## 📁 Important Files

### Dataset

```text
dataset/logging_monitoring_anomalies.csv
```

### Benchmarking

```text
scripts/bench_one.py
```

### Real-Time Experiment

```text
scripts/realtime/run_exp3.sh
```

### Results

```text
results/bench_results.json
results/loc_results.json
results/rt_latency_results.json
```

### Figures

```text
diagram/
```

---

## 🔬 Research Applications

This repository can be used for research related to:

* Shell Programming
* System Log Processing
* Log Analysis
* Performance Benchmarking
* Real-Time Data Processing
* Anomaly Monitoring
* Scripting Language Comparison
* Linux/Unix-Based Data Processing

---

## 📌 Reproducibility

The repository contains the dataset, source scripts, experimental result files, and generated diagrams required to reproduce and inspect the experiments.

For reproducibility, experiments should be performed on the same or a comparable Linux/Unix environment and with consistent hardware/software configurations.

---

## 👩‍💻 Author

**Priyanka Patel**

Department of Computer Science

---

## 📜 License

This project is intended for academic and research purposes.

Please verify the applicable dataset and software licenses before redistribution or commercial use.
