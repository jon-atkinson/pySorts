import { ResponsiveLine } from "@nivo/line";
import { tokens } from "../theme";
import { useTheme } from "@mui/material";

const LineChart = ({ isDashboard = false, data = null }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <ResponsiveLine
      data={data}
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.darkPastelGreen[100],
            },
          },
          legend: {
            text: {
              fill: colors.darkPastelGreen[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.darkPastelGreen[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.darkPastelGreen[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.darkPastelGreen[100],
          },
        },
        tooltip: {
          container: { color: colors.primary[500] },
        },
      }}
      // colors={isDashboard ? { datum: "color" } : { scheme: "nivo" }}
      margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
      xScale={{ type: "point" }}
      yScale={{
        type: "linear",
        min: "0",
        max: "auto",
        stacked: false,
        reverse: false,
      }}
      xFormat=" <-1.100"
      axisTop={null}
      axisRight={null}
      axisBottom={null}
      axisLeft={{
        legend: isDashboard ? undefined : "time (s)",
        legendOffset: -50,
        legendPosition: "middle",
      }}
      enableGridX={false}
      enableGridY={false}
      colors={{ scheme: "category10" }}
      enablePoints={false}
      pointBorderWidth={2}
      enableTouchCrosshair={true}
      useMesh={true}
      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 0,
          translateY: 0,
          itemsSpacing: 0,
          itemDirection: "left-to-right",
          itemWidth: 80,
          itemHeight: 20,
          itemOpacity: 0.75,
          symbolSize: 12,
          symbolShape: "circle",
          symbolBorderColor: "rgba(0, 0, 0, .5)",
          effects: [
            {
              on: "hover",
              style: {
                itemBackground: "rgba(0, 0, 0, .03)",
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
    />
  );
};

export default LineChart;
