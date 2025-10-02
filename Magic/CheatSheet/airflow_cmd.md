### List import errors

```bash
airflow dags list-import-errors
```

### list available dags

```bash
airflow dags list
```

### generate report 

```bash
airflow dags report
```

### force dag refresh

```bash
airflow dags reserialize
````

### list runs for a dag

```bash
airflow dags list-runs <<dag_name>>
```

### list task from a dag

```bash
airflow tasks list <<dag_name>>
```

### check state of a task from a dag on a run

```bash
airflow tasks state <<dag_name>> <<task_id>> <<run_id>>
```
