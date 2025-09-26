# 🧠 What is Kafka Connect?

Kafka Connect is a tool that helps you **move data in and out of Apache Kafka** easily and reliably — without writing custom code.

---

## 📦 Think of it like a data pipeline plug-and-play system:

- You have **data sources** like databases (MySQL, PostgreSQL), cloud storage (S3), or applications.
- You have **data sinks** like Elasticsearch, another database, or even a file system.
- Kafka Connect acts as a **bridge** between these sources/sinks and **Kafka topics**.

---

## 🔌 How it works:

You use **Connectors**:

- **Source Connector**: pulls data *from* a system *into* Kafka.
- **Sink Connector**: pushes data *from* Kafka *into* another system.

You configure these connectors using simple **JSON files** or **REST APIs**.

---

## 🛠️ Example

Let’s say you want to stream data from a **PostgreSQL database** to **Elasticsearch**:

1. **Source Connector** reads rows from PostgreSQL and writes them to a Kafka topic.
2. **Sink Connector** reads from that Kafka topic and writes to Elasticsearch.

✅ No need to write custom code — just configure the connectors!

---

## ✅ Benefits

- **Scalable**: Handles large volumes of data.
- **Fault-tolerant**: Automatically retries and recovers from failures.
- **Pluggable**: Many pre-built connectors available.
- **Managed**: Can run in standalone or distributed mode.

---

# 🔌 Types of Kafka Connectors

## 1. Source Connectors

These **pull data from external systems** and write it into Kafka topics.

**Examples:**
- **JDBC Source Connector** – reads from relational databases like MySQL, PostgreSQL.
- **MongoDB Source Connector** – reads from MongoDB collections.
- **Debezium Source Connector** – captures change data (CDC) from databases.
- **FileStream Source Connector** – reads data from local files.

---

## 2. Sink Connectors

These **read data from Kafka topics** and push it into external systems.

**Examples:**
- **JDBC Sink Connector** – writes to relational databases.
- **Elasticsearch Sink Connector** – sends data to Elasticsearch.
- **S3 Sink Connector** – stores Kafka data in AWS S3.
- **HDFS Sink Connector** – writes to Hadoop HDFS.

---

# 🧩 Connector Categories by Ecosystem

- **Database Connectors**: JDBC, Debezium, Cassandra, MongoDB
- **Cloud Connectors**: AWS S3, GCP BigQuery, Azure Blob Storage
- **Search & Analytics**: Elasticsearch, Snowflake
- **Messaging Systems**: MQTT, RabbitMQ
- **File Systems**: Local files, HDFS
- **Monitoring Tools**: Prometheus, Splunk

---

## 🛠️ Bonus: Custom Connectors

You can also **build your own connector** if your system isn’t supported. Kafka Connect provides a framework to implement custom logic.
