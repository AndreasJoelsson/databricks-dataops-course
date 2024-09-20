# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. connect to the UC Shared Cluster you have been assigned, and run through the cells
# MAGIC 3. Run the cells for deploying and running the dev job

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Workflows
# MAGIC
# MAGIC Workflows is on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...
# MAGIC
# MAGIC Job is the task that should be executed.
# MAGIC Job run is the execution of the defined job.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Write answer in the empty cell below.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...
# MAGIC
# MAGIC acme_transport_taxinyc_prep_dev_andreaserikwilhelmjoelsson_test1_1e576290 run
# MAGIC
# MAGIC part of the git commit short sha.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Where is the job cluster defined?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...
# MAGIC
# MAGIC Under Compute, as a sheared-job-cluster-dev

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...

# COMMAND ----------


