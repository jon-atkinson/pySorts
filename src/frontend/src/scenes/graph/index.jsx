import { Box } from "@mui/material";
import LineChart from "../../components/LineChart";
import Header from "../../components/Header";

const Graph = ({graphData}) => {
  if (graphData === null) {
    graphData = [{color: "black", data: [{x: 0, y: 0}], id: "empty"}];
  }

  return (
    <Box m="20px">
      <Header title="Results" subtitle="Selected/Most Recent Run" />
      <Box height="75vh">
        <LineChart data={graphData} />
      </Box>
    </Box>
  );
};

export default Graph;
