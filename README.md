<!-- # GTD Terrorism Data Analysis with Hadoop MapReduce

This project analyzes the Global Terrorism Database (GTD) using Hadoop MapReduce and visualizes the top 10 countries with the most terrorist attacks.

## Files

- `preprocess_gtd.py` – Preprocessing script
- `mapper.py` – MapReduce mapper script
- `reducer.py` – MapReduce reducer script
- `gtd_output.txt` – Output file from HDFS
- `top_countries.py` – Python script to parse results and visualize top 10 countries
- `top10_countries.csv` – CSV result of the top 10
- `top10_countries.png` – Plot saved as PNG

## Steps to setup Hadoop in Ubuntu

> Refer: [phoenixNAP Hadoop Setup Guide](https://phoenixnap.com/kb/install-hadoop-ubuntu)

1. Install JDK on Ubuntu

2. Setup Hadoop User and configure SSH

3. Download and install Hadoop on Ubuntu

4. Single Node Hadoop deployment

5. Format HDFS NameNode

6. Start Hadoop cluster

7. Access Hadoop from Browser

## Download and clean data

1. Download the dataset from Kaggle: [https://www.kaggle.com/datasets/START-UMD/gtd](https://www.kaggle.com/datasets/START-UMD/gtd)  

2. Run `preprocess_gtd.py` to clean the dataset and remove header values.
```bash
python3 preprocess_gtd.py
```

## Steps to Run

### 1. Upload dataset to HDFS
```bash
hdfs dfs -mkdir -p /gtd_input
hdfs dfs -put gtd_clean.csv /gtd_input/
```
### 2. Run MapReduce Job

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /gtd_input/gtd_clean.csv \
  -output /gtd_output \
  -mapper mapper.py \
  -reducer reducer.py
```
### 3. Get Output from HDFS

```bash
hdfs dfs -get /gtd_output/part-00000 gtd_output.txt
```
### 4. Visualize with python

```bash
python3 top_countries.py
```
### 5. Setup Python Requirements (If not installed)

```bash
sudo apt install python3-pip
pip3 install --user pandas matplotlib
```
## Results

Output -> top10_countries.csv 

By visualizing this data we can show where the top 10 countries with the most terrorist attacks.

Result is shown in top10_countries.png file with the counts.
 -->

# 🌍 GTD Terrorism Data Analysis with Hadoop MapReduce 🚀

This project analyzes the **Global Terrorism Database (GTD)** using Hadoop MapReduce and creates a visualization of the **top 10 countries** with the most terrorist attacks. 📊

## 📂 Files

- `preprocess_gtd.py` – 🧹 Preprocessing script to clean the dataset
- `mapper.py` – 🔄 MapReduce mapper script
- `reducer.py` – 🔢 MapReduce reducer script
- `gtd_output.txt` – 📄 Output file from HDFS
- `top_countries.py` – 📈 Python script to parse results and visualize top 10 countries
- `top10_countries.csv` – 📑 CSV result of the top 10 countries
- `top10_countries.png` – 🖼️ Plot saved as PNG

## 🛠️ Steps to Set Up Hadoop in Ubuntu

> 📚 Refer: [phoenixNAP Hadoop Setup Guide](https://phoenixnap.com/kb/install-hadoop-ubuntu)

1. ☕ **Install JDK** on Ubuntu
2. 🔑 **Set up Hadoop User** and configure SSH
3. 📥 **Download and install Hadoop** on Ubuntu
4. 🖥️ **Single Node Hadoop deployment**
5. 💾 **Format HDFS NameNode**
6. ▶️ **Start Hadoop cluster**
7. 🌐 **Access Hadoop from Browser**

## 📥 Download and Clean Data

1. 🌐 Download the dataset from Kaggle: [Global Terrorism Database](https://www.kaggle.com/datasets/START-UMD/gtd)
2. 🧹 Run `preprocess_gtd.py` to clean the dataset and remove header values:

```bash
python3 preprocess_gtd.py 
```

## 🚀 Steps to Run
### 1. 📤 Upload Dataset to HDFS
```bash
hdfs dfs -mkdir -p /gtd_input
hdfs dfs -put gtd_clean.csv /gtd_input/
```
### 2. 🏃 Run MapReduce Job

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /gtd_input/gtd_clean.csv \
  -output /gtd_output \
  -mapper mapper.py \
  -reducer reducer.py
```
### 3. 📥 Get Output from HDFS

```bash
hdfs dfs -get /gtd_output/part-00000 gtd_output.txt
```
### 4. 📊 Visualize with python

```bash
python3 top_countries.py
```
### 5. 🛠️ Setup Python Requirements (If not installed)

```bash
sudo apt install python3-pip
pip3 install --user pandas matplotlib
```
## 🎉 Results

Output => `top10_countries.csv` 

By visualizing this data we can show where the top 10 countries with the most terrorist attacks.

Result is shown in `top10_countries.png` file with the counts.




