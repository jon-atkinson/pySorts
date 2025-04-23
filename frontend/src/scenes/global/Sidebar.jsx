import { useState } from "react";
import {
  Sidebar as ProSidebar,
  Menu,
  MenuItem,
  sidebarClasses,
} from "react-pro-sidebar";
import { Box, IconButton, Typography, useTheme } from "@mui/material";
import { Link } from "react-router-dom";
import { tokens } from "../../theme";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import FunctionIcon from "@mui/icons-material/Functions";
import DataArrayIcon from "@mui/icons-material/DataArray";
import StorageOutlinedIcon from "@mui/icons-material/StorageOutlined";
import Info from "@mui/icons-material/Info";
import TimelineOutlinedIcon from "@mui/icons-material/TimelineOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";

const Item = ({ title, to, icon, selected, setSelected }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const active = selected === title;
  console.log(`theme is ${JSON.stringify(theme)}`);
  return (
    <MenuItem
      active={active}
      style={{
        // color: active ? colors.gray[400] : colors.darkPastelGreen[100],
        color: active ? colors.gray[400] : colors.ghostWhite[500],
        backgroundColor: theme.palette.accent,
      }}
      onClick={() => setSelected(title)}
      icon={icon}
      component={<Link to={to} />}
    >
      <Typography>{title}</Typography>
    </MenuItem>
  );
};

const Sidebar = ({ selected, setSelected }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <ProSidebar
      collapsed={isCollapsed}
      rootStyles={{
        height: "100vh",
        position: "sticky",
        [`.${sidebarClasses.container}`]: {
          backgroundColor: `${theme.palette.accent}`,
        },
        borderRightWidth: "0px",
      }}
    >
      <Menu iconShape="square">
        {/* Logo and Menu Icon */}
        <MenuItem
          onClick={() => setIsCollapsed(!isCollapsed)}
          icon={isCollapsed ? <MenuOutlinedIcon /> : undefined}
          style={{
            margin: "10px 0 20px 0",
            color: colors.darkPastelGreen[100],
            backgroundColor: theme.palette.accent,
          }}
        >
          {!isCollapsed && (
            <Box
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              ml="15px"
            >
              <Typography variant="h3" color={colors.darkPastelGreen[100]}>
                pySorts
              </Typography>
              <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                <MenuOutlinedIcon />
              </IconButton>
            </Box>
          )}
        </MenuItem>

        {/* Menu Items */}
        <Box paddingLeft={isCollapsed ? undefined : "10%"}>
          <Item
            title="Dashboard"
            to="/"
            icon={<HomeOutlinedIcon />}
            selected={selected}
            setSelected={setSelected}
          />

          <Typography
            variant="h6"
            color={colors.darkPastelGreen[900]}
            sx={{ m: "15px 0 5px 20px" }}
          >
            Data
          </Typography>
          <Item
            title="Compare Algorithms"
            to="/algorithms"
            icon={<FunctionIcon />}
            selected={selected}
            setSelected={setSelected}
          />
          <Item
            title="Compare Array Types"
            to="/sortedness"
            icon={<DataArrayIcon />}
            selected={selected}
            setSelected={setSelected}
          />
          <Item
            title="Previous Runs"
            to="/previous"
            icon={<StorageOutlinedIcon />}
            selected={selected}
            setSelected={setSelected}
          />
          <Typography
            variant="h6"
            color={colors.darkPastelGreen[900]}
            sx={{ m: "15px 0 5px 20px" }}
          >
            Pages
          </Typography>
          <Item
            title="About pySorts"
            to="/about"
            icon={<Info />}
            selected={selected}
            setSelected={setSelected}
          />
          <Typography
            variant="h6"
            color={colors.darkPastelGreen[900]}
            sx={{ m: "15px 0 5px 20px" }}
          >
            Chart
          </Typography>
          <Item
            title="Results"
            to="/graph"
            icon={<TimelineOutlinedIcon />}
            selected={selected}
            setSelected={setSelected}
          />
        </Box>
      </Menu>
    </ProSidebar>
  );
};

export default Sidebar;
