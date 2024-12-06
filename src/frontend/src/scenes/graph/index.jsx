import { useState, useEffect } from "react";
import axios from "axios";
import { Box, Typography } from "@mui/material";

const Graph = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const queryBody = {
    algorithms: [
      { algorithm: "bubble sort", language: "python" },
      { algorithm: "selection sort", language: "python" },
      { algorithm: "heap sort", language: "python" },
      { algorithm: "bubble sort", language: "c" },
    ],
    low: 1,
    high: 100,
    "array type": "random",
    "number repetitions": 1,
    step: 1,
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/compare-algorithms",
          queryBody,
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );
        setData(response.data);
      } catch (err) {
        setError(err.message);
        console.log(err.message);
      }
    };
    fetchData();
  }, []);

  return (
    <Box>
      {error && <Typography color="red">An Error Occurred</Typography>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <Typography color="green">Loading...</Typography>
      )}
    </Box>
  );
};

export default Graph;
