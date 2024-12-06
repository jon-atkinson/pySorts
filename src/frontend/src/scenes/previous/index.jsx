import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";

import Header from "../../components/Header";

const Previous = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box>
      <Header
        title="Previous"
        subtitle="Previous comparisons run by the tool"
      />
      <Box>
        <DataGrid />
      </Box>
    </Box>
  );
};
