import { Box, Button, Typography, TextField, MenuItem } from "@mui/material";
import LineChart from "../../components/LineChart";
import Header from "../../components/Header";
import { useNavigate } from "react-router-dom";
import { Formik } from "formik";
import * as yup from "yup";

const generateGaussianKernel = (size) => {
  const sigma = 1;
  const kernel = [];
  const center = Math.floor(size / 2);
  let sum = 0;

  for (let i = 0; i < size; i++) {
    const distance = i - center;
    const weight = Math.exp(-(distance ** 2) / (2 * sigma ** 2));
    kernel.push(weight);
    sum += weight;
  }

  return kernel.map((value) => value / sum);
};

const generateUniformKernel = (size) => {
  return Array(size).fill(1 / size);
};

const generateSobelKernel = (size) => {
  const center = Math.floor(size / 2);
  return Array.from({ length: size }, (_, i) => i - center);
};

const generateLaplacianKernel = (size) => {
  const kernel = Array(size).fill(-1);
  const centerIdx = Math.floor(size / 2);
  kernel[centerIdx] = size - 1;

  return kernel;
};

const kernels = [
  {
    name: "gaussian",
    label: "Gaussian",
    function: generateGaussianKernel,
  },
  {
    name: "uniform",
    label: "Uniform",
    function: generateUniformKernel,
  },
  {
    name: "sobel",
    label: "Sobel",
    function: generateSobelKernel,
  },
  {
    name: "laplacian",
    label: "Laplacian",
    function: generateLaplacianKernel,
  },
];

const Graph = ({ graphData, setGraphData }) => {
  const navigate = useNavigate();

  const validationSchema = yup.object().shape({
    kernelSize: yup
      .number()
      .max(
        graphData[0].data.length,
        "Kernel Size cannot be greater than the length of the dataset",
      )
      .min(3, "Kernel Size must be at least 3")
      .required("Kernel Size is required")
      .test({
        name: "is-odd",
        skipAbsent: false,
        test(value, ctx) {
          if (value % 2 === 0) {
            return ctx.createError({ message: "Value must be odd" });
          }
          return true;
        },
      }),
    kernelType: yup.string().required("Kernel Type is required"),
  });

  const applyConvolution = (seriesData, kernel) => {
    const halfKernelLength = Math.floor(kernel.length / 2);
    const kernelSum =
      kernel.reduce((sum, value) => sum + Math.abs(value), 0) || 1;

    const reflectIdx = (index, length) => {
      if (index < 0) {
        return -index - 1;
      } else if (index >= length) {
        return 2 * length - index - 1;
      }
      return index;
    };

    const transformedData = [];

    for (let i = 0; i < seriesData.length; i++) {
      let newY = 0;

      for (let j = 0; j < kernel.length; j++) {
        const dataIdx = i + j - halfKernelLength;
        newY +=
          seriesData[reflectIdx(dataIdx, seriesData.length)].y * kernel[j];
      }

      transformedData.push({
        ...seriesData[i],
        y: newY / kernelSum,
      });
    }

    return transformedData;
  };

  const applyFilterAllSeries = (data, kernel) => {
    for (let seriesIdx = 0; seriesIdx < data.length; seriesIdx++) {
      data[seriesIdx].data = applyConvolution(data[seriesIdx].data, kernel);
    }

    return data;
  };

  const handleSubmit = (values) => {
    const kernel = values.kernelType(parseInt(values.kernelSize, 10));
    const newData = applyFilterAllSeries(graphData, kernel);

    setGraphData(newData);
    navigate("/graph");
  };

  return (
    <Box m="20px" flex="1">
      {/* Chart */}
      <Header title="Results" subtitle="Selected/Most Recent Run" />
      <Box display="flex" height="75vh" width="100%">
        <Box flex="9" height="100%">
          <LineChart data={graphData} />
        </Box>

        {/* Convolution Filter Configuration Form */}
        <Box flex="1" textAlign="center">
          <Typography variant="h6" gutterBottom>
            Configure Kernel
          </Typography>
          <Formik
            initialValues={{ kernelSize: 3, kernelType: kernels[0].function }}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
          >
            {({
              values,
              errors,
              touched,
              handleChange,
              handleBlur,
              handleSubmit,
            }) => (
              <form onSubmit={handleSubmit}>
                <TextField
                  label="Kernel Size"
                  name="kernelSize"
                  type="number"
                  value={values.kernelSize}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  variant="outlined"
                  fullWidth
                  error={!!touched.kernelSize && !!errors.kernelSize}
                  helperText={touched.kernelSize && errors.kernelSize}
                />
                <TextField
                  label="Kernel Type"
                  name="kernelType"
                  select
                  value={values.kernelType}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  variant="outlined"
                  fullWidth
                >
                  {kernels.map((option) => (
                    <MenuItem key={option.name} value={option.function}>
                      {option.label}
                    </MenuItem>
                  ))}
                </TextField>
                <Box display="flex" justifyContent="space-around" marginTop="2">
                  <Button type="submit" color="primary" variant="contained">
                    Apply Convolution Filter
                  </Button>
                </Box>
              </form>
            )}
          </Formik>
        </Box>
      </Box>
    </Box>
  );
};

export default Graph;
