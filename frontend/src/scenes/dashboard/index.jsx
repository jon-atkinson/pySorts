import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Header from "../../components/Header";

const Dashboard = () => {
  return (
    <Box>
      <Box m="20px">
        <Header title="Dashboard" subtitle="How to Use pySorts" />
        <Typography variant="h4" padding="20px">
          {
            "Navigate the application using the sidebar on the left of the screen.\
                    The sidebar can be collapsed/expanded by clicking the icon in the top\
                    left corner of the screen."
          }
        </Typography>
        <Typography variant="h4" padding="20px">
          {
            "Compare Algorithms = run different language-algorithm combinations with\
                    the same input arrays."
          }
        </Typography>
        <Typography variant="h4" padding="20px">
          {
            "Compare Array Types = run a single language-algorithm combination with\
                    differently sorted input arrays."
          }
        </Typography>
        <Typography variant="h4" padding="20px">
          {
            "Previous Runs = graph previously run comparisons without having to\
                    recompute them from scratch"
          }
        </Typography>
        <Typography variant="h4" padding="20px">
          {"Results = View the most recently displayed run's graph."}
        </Typography>
      </Box>
    </Box>
  );
};

export default Dashboard;
