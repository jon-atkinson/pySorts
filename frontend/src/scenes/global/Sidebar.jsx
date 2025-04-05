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
import HelpOutlinedIcon from "@mui/icons-material/HelpOutlined";
import TimelineOutlinedIcon from "@mui/icons-material/TimelineOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";

const Item = ({ title, to, icon, selected, setSelected }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const active = selected === title;
  return (
    <MenuItem
      active={active}
      style={{
        color: active ? colors.blueAccent[400] : colors.grey[100],
        backgroundColor: colors.primary[400],
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
          backgroundColor: `${colors.primary[400]}`,
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
            color: colors.grey[100],
            backgroundColor: colors.primary[400],
          }}
        >
          {!isCollapsed && (
            <Box
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              ml="15px"
            >
              <Typography variant="h3" color={colors.grey[100]}>
                pySorts
              </Typography>
              <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                <MenuOutlinedIcon />
              </IconButton>
            </Box>
          )}
        </MenuItem>
        {/* User */}
        {/* {!isCollapsed && (
          <Box mb="25px">
            <Box display="flex" justifyContent="center" alignItems="center">
              <img
                alt="profile-user"
                width="100px"
                height="100px"
                src={`../../assets/sadMario.jpg`}
                style={{ cursor: "pointer", borderRadius: "50%" }}
              />
            </Box>
            <Box textAlign="center">
              <Typography
                variant="h2"
                color={colors.grey[100]}
                fontWeight="bold"
                sx={{ m: "10px 0 0 0" }}
              >
                Jon Atkinson
              </Typography>
              <Typography variant="h5" color={colors.greenAccent[500]}>
                User
              </Typography>
            </Box>
          </Box>
        )} */}

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
            color={colors.grey[600]}
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
            color={colors.grey[600]}
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
            color={colors.grey[600]}
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
