
# HighCharts Assessment




## Data Preparation

#### Given

The input data file was a CSV file containing the data points for TCS stock. This data has 5 parameters which are date, open, high, low, close, and volume. The date format was in "DD-MM-YYYY" and rest all fields were floating point numbers

#### Parsing data to required format

Here the CSV format is converted to the required json format as expected by the HighChart library. The logic includes the below steps:
- Reading the CSV file and iterating through each row
- Converting the date field to Unix format
- Building data array with parsed date and remaining data


#### Output

Post running the script, it will generate `data.json` file which consists of data in required format. This data will be used as the input for HighChart data. This data is stored in the public folder of the build and fetched via fetch request.

Ideal scenario would be the data coming from API.
## Run Script Locally

### Requirements
- node
- python3.8


### Running the project

Clone the project

```bash
  git clone https://github.com/prathameshramane/HighChartAssessment.git
```

Go to the project directory

```bash
  cd HighChartAssessment
```

Runing Dev

```bash
  npm run dev
```

Start will start at port 8000

```bash
  http://localhost:5173
```
