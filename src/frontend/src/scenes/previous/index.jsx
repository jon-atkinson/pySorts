import { Box, Typography, useTheme, Button } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useEffect, useState } from "react";
import {useNavigate} from "react-router-dom";
import axios from "axios";
import { tokens } from "../../theme";
import Header from "../../components/Header";

const Previous = ({setGraphData}) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const navigate = useNavigate();

  const [previous, setPrevious] = useState([]);

  useEffect(() => {
    const fetchPrevious = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/history");
        const data = response.data;

        const formatted = data.comparisons.map((comparison, index) => ({
          id: index + 1,
          runId: comparison.id,
          description: `Run ${index + 1}: ${comparison.type}`,
        }));

        setPrevious(formatted)
      } catch (error) {
        console.error("Failed to fetch previous: ", error);
      }
    };

    fetchPrevious();
  }, []);

  const transformData = (response = null) => {
    if (response.type === "compare-algorithms") {
      return response.data.map((item) => {
        const algorithm = item[0];
        const language = item[1];
        const algorithmId = `${algorithm} (${language})`;
        const dataPoints = item[2].map(([x, y]) => ({
          x: String(x),
          y: y,
        }));
        
        return {
          id: algorithmId,
          color: colors.greenAccent[100],
          data: dataPoints,
        };
      });
    } else {
      console.log(response);
      return response.data.map((item) => {
        const arrayType = item[0];
        const dataPoints = item[1].map(([x, y]) => ({
          x: String(x),
          y: y,
        }));

        return {
          id: arrayType,
          color: colors.greenAccent[100],
          data: dataPoints,
        }
      });
    }
  }

  const handleGraphClick = async (id) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/comparison/${id}`);
      const data = response.data;

      console.log("data: ", data)
      setGraphData(transformData(data));
      navigate("/graph");
    } catch (error) {
      console.error("Error fetching comparison data: ", error);
    }
  };

  const columns = [
    { field: "id", headerName: "ID", width: 100 },
    // internal id, for debugging
    // {
    //   field: "runId",
    //   headerName: "Run ID",
    //   flex: 1,
    // },
    {
      field: "description",
      headerName: "Description",
      flex: 2,
    },
    {
      field: "graph",
      headerName: "Graph",
      width: 150,
      renderCell: (params) => (
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleGraphClick(params.row.runId)}
        >
          Graph
        </Button>
      ),
    },
  ];

  return (
    <Box m="20px">
      <Header
        title="Previous Runs"
        subtitle="List of Available Runs to Graph"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .MuiDataGrid-columnHeader": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        <DataGrid rows={previous} columns={columns} />
      </Box>
    </Box>
  );
};

export default Previous;
