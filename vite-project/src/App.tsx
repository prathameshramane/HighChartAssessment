import { useEffect, useState } from "react";
import Highcharts from "highcharts/highstock";
import HighchartsReact from "highcharts-react-official";

function App() {
  const [options, setOptions] = useState<Highcharts.Options | null>(null);

  useEffect(() => {
    prepareChart();
  }, []);

  const prepareChart = async () => {
    const data = await fetch("/data.json").then((response) => response.json());

    setOptions({
      title: {
        text: "Tata Consultancy Services Limited (TCS.NS)",
      },

      series: [
        {
          type: "candlestick",
          name: "Tata Consultancy Services Limited (TCS.NS)",
          data: data,
        },
      ],
    });
  };

  return (
    options && (
      <HighchartsReact
        highcharts={Highcharts}
        options={options}
        constructorType={"stockChart"}
      />
    )
  );
}

export default App;
