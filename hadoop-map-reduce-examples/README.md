# Introduction
map reduce example  that is able to run on hadoop
### Run Map Reduce code locally
for example
```bash
cat ./data/light_dataset.csv |python3 ./Q4/mapper.py |python3 ./Q4/reducer.py

# result will be

################# likes retweets Twitter Web App Twitter for Android Twitter for iPhone
#Both_Candidates 535873 158881 28456 14496 20053
#Donald_Trump 362583 120214 25877 16291 19339
#Joe_Biden 566176 221989 20740 11760 18632
```

### Run Map Reduce code on Hadoop
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -file ./Q4/reducer.py -file ./Q4/mapper.py -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input /your/path/on/hdfs -output /your/path/on/hdfs
```