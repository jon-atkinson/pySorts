import { Box, Typography, Link, useTheme } from "@mui/material";
import { tokens } from "../theme";

const Footer = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box
      sx={{
        width: "100%",
        padding: "10px",
        textAlign: "center",
        borderTop: "1px solid rgba(0, 0, 0, 0.1)",
        mt: "auto",
      }}
    >
      <Typography variant="body2" color={colors.gray[200]}>
        {"MIT Licence - "}
        <Link
          color={colors.gray[400]}
          href="https://github.com/jon-atkinson/pySorts"
          target="_blank"
          rel="noopener noreferrer"
          underline="always"
        >
          Source Hosted on Github
        </Link>
      </Typography>
    </Box>
  );
};

export default Footer;
