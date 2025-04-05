import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import Check from "@mui/icons-material/Check";

const About = () => {
  return (
    <Box>
      <Box
        sx={{
          margin: "50px",
          padding: "20px",
        }}
      >
        <Typography variant="h4" padding="20px">
          {
            "pySorts was designed to fill the gap between a textbook explanation of algorithmic\
                    complexity and websites or videos that show each animated step of a sorting algorithm."
          }
        </Typography>

        <Typography variant="h4" padding="20px">
          {
            "The goal of the app is to demonstrate what the response curve of a simple algorithm looks\
                    like when run on actual hardware, and to expose the natural variations in real\
                    runtimes to students."
          }
        </Typography>

        <Typography variant="h4" padding="20px">
          {
            "Over time more features have been added but the core purpose of the tool is still to\
                        provide a responsive view into the asymptotic runtimes of a few common algorithms."
          }
        </Typography>

        <Box padding="0 20px 20px 20px">
          <Typography variant="h4">{"Supplimental features:"}</Typography>

          <List>
            <ListItem disablePadding>
              <ListItemIcon>
                <Check />
              </ListItemIcon>
              <ListItemText primary="Compare Languages" />
            </ListItem>

            <ListItem disablePadding>
              <ListItemIcon>
                <Check />
              </ListItemIcon>
              <ListItemText primary="Compare Input Array Types" />
            </ListItem>
          </List>
        </Box>
      </Box>
    </Box>
  );
};

export default About;
