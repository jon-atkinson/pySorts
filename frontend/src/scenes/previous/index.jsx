import { Box, useTheme, Button } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { tokens } from "../../theme";
import Header from "../../components/Header";

const Previous = ({ setGraphData }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const navigate = useNavigate();

  const [previous, setPrevious] = useState([]);

  const formatPrevious = (data) => {
    return data.comparisons.map((comparison, index) => {
      const arrayTypes = [
        ...new Set(
          comparison.algorithms?.map(([algorithm, language, arrayShape]) => {
            return arrayShape.type;
          }),
        ),
      ].join(", ");

      const algorithms =
        [
          ...new Set(
            comparison.algorithms?.map(
              ([algorithm, language, arrayShape]) =>
                `${algorithm} (${language})`,
            ),
          ),
        ].join(", ") || "N/A";

      const arrayStart = comparison.algorithms[0][2].start;
      const arrayEnd = comparison.algorithms[0][2].stop;
      const arrayStep = comparison.algorithms[0][2].step;
      const repeats = comparison.algorithms[0][2].repeats;

      return {
        id: index + 1,
        runId: comparison.id,
        comparisonType: `${comparison.type}`,
        arrayStart,
        arrayEnd,
        arrayStep,
        repeats,
        arrayTypes,
        algorithms,
      };
    });
  };

  useEffect(() => {
    const fetchPrevious = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/history");
        const formatted = formatPrevious(response.data);
        setPrevious(formatted);
      } catch (error) {
        console.error("Failed to fetch previous: ", error);
      }
    };

    fetchPrevious();
  }, []);

  const transformData = (response = null) => {
    if (response.type === "algorithm") {
      return response["data_series"].map((item) => {
        const algorithm = item["algorithm"];
        const language = item["language"];
        const algorithmId = `${algorithm} (${language})`;

        const dataPoints = item["data"].map(([x, y]) => ({
          x: String(x),
          y: y,
        }));

        return {
          id: algorithmId,
          color: colors.greenAccent[100],
          data: dataPoints,
        };
      });
    } else if (response.type === "sortedness") {
      return response["data_series"].map((item) => {
        const arrayType = item["array_type"];

        const dataPoints = item["data"].map(([x, y]) => ({
          x: String(x),
          y: y,
        }));

        return {
          id: arrayType,
          color: colors.greenAccent[100],
          data: dataPoints,
        };
      });
    } else {
      console.error("unknown graph type requested");
    }
  };

  const handleGraphClick = async (id) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/comparison/${id}`,
      );
      const data = response.data;

      setGraphData(transformData(data));
      navigate("/graph");
    } catch (error) {
      console.error("Error fetching comparison data: ", error);
    }
  };

  const handleDeleteClick = async (id) => {
    try {
      const response = await axios.delete(`http://127.0.0.1:8000/delete/${id}`);
      const formatted = formatPrevious(response.data);
      setPrevious(formatted);
    } catch (error) {
      console.error("Error deleting comparison data: ", error);
    }
  };

  const columns = [
    {
      field: "comparisonType",
      headerName: "Comparison Type",
      width: 120,
    },
    {
      field: "arrayTypes",
      headerName: "Array Types",
      flex: 2,
    },

    {
      field: "algorithms",
      headerName: "Algorithms",
      flex: 2,
    },
    {
      field: "arrayStart",
      headerName: "Array Start",
      width: 80,
    },
    {
      field: "arrayEnd",
      headerName: "Array End",
      width: 80,
    },
    {
      field: "arrayStep",
      headerName: "Array Step",
      width: 80,
    },
    {
      field: "repeats",
      headerName: "Repeats",
      width: 80,
    },
    {
      field: "graph",
      headerName: "Graph",
      width: 120,
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
    {
      field: "Delete",
      headerName: "Delete",
      width: 120,
      renderCell: (params) => (
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleDeleteClick(params.row.runId)}
        >
          Delete
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
