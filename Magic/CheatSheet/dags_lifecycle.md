## Dags lifcycle

- **Scheduler reads /opt/airflow/dags  periodically** (depends on where u have dags folder, the path may change)

- **Scheduler leads the DAG file into an in-memory region (called DagBag)**

- **Scheduler checks import errors**

- **Scheduler serializes Dags (turns them into bundles) and write them to airflow metadata database**

```sql
ETL_DB=# select * from dag_bundle
ETL_DB-# ;;
-[ RECORD 1 ]-------+------------
name                | dags-folder
active              | t
version             | 
last_refreshed      | 
signed_url_template | 
template_params     | {}
```

- **Webserver queries the serialized DAG bundles from the metadata database**

-

